
from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pathlib import Path
import io
import requests

app = FastAPI()

# Directory where your files are located (relative to the current directory)
file_directory = Path("files")
server2_url = "http://localhost:8001"  # Replace with the actual URL of server2

@app.get("/get_files/")
async def get_files(file_name: str):
    # Build the full path to the requested file in server1
    file_path_server1 = file_directory / file_name

    # Check if the file exists in server1
    if not file_path_server1.exists():
        # If the file doesn't exist in server1, check if it exists in server2
        response_server2 = requests.get(f"{server2_url}/get_file/{file_name}")
        if response_server2.status_code == 200:
            # If the file exists in server2, return it
            file_content_server2 = response_server2.content
            return Response(content=file_content_server2, media_type="application/octet-stream")
        else:
            raise HTTPException(status_code=404, detail="File not found!")
    else:
        # If the file exists in server1, compare its content with server2
        file_content_server1 = file_path_server1.read_bytes()
        response_server2 = requests.get(f"{server2_url}/get_file/{file_name}")
        
        if response_server2.status_code == 200:
            file_content_server2 = response_server2.content
            if file_content_server1 == file_content_server2:
                # If content matches, return server1 file as text/plain
                return Response(content=file_content_server1, media_type="text/plain")
            else:
                # If content differs, return both files
                combined_content = io.BytesIO()
                combined_content.write(f"==== {file_name} ====\n".encode())
                combined_content.write(file_content_server1 + b"\n\n")
                combined_content.write(f"==== server2-{file_name} ====\n".encode())
                combined_content.write(file_content_server2 + b"\n\n")
                combined_content.seek(0)
                return Response(content=combined_content.getvalue(), media_type="text/plain")
        else:
            # If server2 doesn't have the file, return server1 file as text/plain
            return Response(content=file_content_server1, media_type="text/plain")

if __name__ == "__main__":
    import uvicorn

    # Run the FastAPI application using Uvicorn on port 8000
    uvicorn.run(app, host="127.0.0.1", port=8000)


