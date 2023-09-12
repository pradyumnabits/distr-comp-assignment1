# Distributed Computing - Assignment1

This example demonstrates a simple distributed computing scenario using python.

## Set the environment 
1. Open a terminal.
2. Navigate to the root directory.
  Install the required dependencies i.e. pip, FastAPI, uvicorn if not yet available on server
  Alternatively  run the following command to install the required dependencies
  sh ./set-env.sh

## Server 1

Server 1 serves files from its local directory and can communicate with Server 2 to retrieve files.

To start Server 1:
1. Open a terminal.
2. Navigate to the `server1` directory.
3. Update the following server2 url(server2_url) in server1.py
4. You can update files directory(file_directory) in server1.py.
   By default, the files are located in the "files" directory, which is relative to the current directory.

Start Server 1 using Uvicorn with the following command (you can specify a custom port if needed, default is 8000):
sh ./server2.sh {port-number}
Alternatively  run the following command
uvicorn server1:app --reload --port 8000


## Server 2
Server 2 serves files from its local directory and can communicate with Server 1 to retrieve files.

To start Server 2:

1. Open a terminal.
2. Navigate to the server2 directory.
3. You can update files directory(file_directory) in server1.py.
   By default, the files are located in the "files" directory, which is relative to the current directory.



Start Server 2 using Uvicorn with the following command (you can specify a custom port if needed, default is 8001):
sh ./server2.sh {port-number}
Alternatively run the following command
uvicorn server2:app --reload --port 8001

## Client
The client application can be used to download files from the servers.

To start the client:

1. Open a terminal.
2. Navigate to the client directory.
3. Update the server1 url (server_url) in client.py

Run the client script with the following command and follow the prompts to download files:
sh ./client.sh
Alternatively  run the following command
python ./client.py

Please make sure that both Server 1 and Server 2 are running before using the client.
