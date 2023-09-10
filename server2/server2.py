from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI()

# Directory where your files are located (relative to the current directory of server2)
file_directory = Path("files")

@app.get("/get_file/{file_name}")
async def get_file(file_name: str):
    # Build the full path to the requested file
    file_path = file_directory / file_name

    # Check if the file exists
    if not file_path.exists():
        #return {"error": "File not found"}
        raise HTTPException(status_code=404, detail="File not found!")

    # Return the file as a response
    return FileResponse(file_path, media_type="application/octet-stream")

if __name__ == "__main__":
    import uvicorn

    # Run the FastAPI application using Uvicorn on port 8001
    uvicorn.run(app, host="127.0.0.1", port=8001)
