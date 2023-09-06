# from fastapi import FastAPI
# from fastapi.responses import Response
# from pathlib import Path
# import io
# from fastapi.param_functions import Query

# app = FastAPI()

# # Directory where your files are located (relative to the current directory)
# file_directory = Path("files")

# @app.get("/get_files/")
# async def get_files(file_name: str = Query(...)):
#     # Build the full path to the requested file
#     file_path = file_directory / file_name

#     # Check if the file exists
#     if not file_path.exists():
#         return {"error": "File not found"}

#     # Create a single binary response containing the requested file
#     combined_content = io.BytesIO()
#     file_content = file_path.read_bytes()
#     combined_content.write(f"==== {file_path.name} ====\n".encode())
#     combined_content.write(file_content + b"\n\n")
#     combined_content.seek(0)

#     return Response(content=combined_content.getvalue(), media_type="text/plain")

# if __name__ == "__main__":
#     import uvicorn

#     # Run the FastAPI application using Uvicorn on port 8000
#     uvicorn.run(app, host="127.0.0.1", port=8001)


# #uvicorn main:app --reload --port 8001


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
