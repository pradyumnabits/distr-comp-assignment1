#!/bin/bash

#uvicorn server2:app --reload --host 0.0.0.0 --port 8001


# Default port number (you can change it if needed)
PORT=8001

# Check if a port number was provided as an argument
if [ $# -eq 1 ]; then
    PORT=$1
fi

# Activate your virtual environment (if applicable)
# source /path/to/your/virtualenv/bin/activate

# Run the FastAPI application using Uvicorn
uvicorn server2:app --reload --host 0.0.0.0 --port $PORT


