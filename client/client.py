# import requests
# import os

# def download_files():
#     server_url = "http://localhost:8000"  # Replace with the actual server URL
#     response = requests.get(f"{server_url}/get_files/")

#     if response.status_code == 200:
#         combined_content = response.content.decode()
#         files = combined_content.split("==== ")

#         # Create a "downloads" folder if it doesn't exist
#         download_folder = "downloads"
#         os.makedirs(download_folder, exist_ok=True)

#         for file_data in files:
#             if not file_data:
#                 continue
#             filename, content = file_data.split(" ====\n", 1)
#             file_path = os.path.join(download_folder, filename)
#             with open(file_path, "wb") as file:
#                 file.write(content.encode())
#             print(f"File '{filename}' has been downloaded to '{download_folder}'")
#     else:
#         print(f"Failed to download files. Status code: {response.status_code}")

# if __name__ == "__main__":
#     download_files()


# import requests
# import os

# def download_file(file_name):
#     server_url = "http://localhost:8000"  # Replace with the actual server URL

#     # Specify the file_name as a query parameter in the URL
#     params = {"file_name": file_name}

#     response = requests.get(f"{server_url}/get_files/", params=params)

#     if response.status_code == 200:
#         combined_content = response.content.decode()
#         files = combined_content.split("==== ")

#         # Create a "downloads" folder if it doesn't exist
#         download_folder = "downloads"
#         os.makedirs(download_folder, exist_ok=True)

#         for file_data in files:
#             if not file_data:
#                 continue
#             filename, content = file_data.split(" ====\n", 1)
#             file_path = os.path.join(download_folder, filename)
#             with open(file_path, "wb") as file:
#                 file.write(content.encode())  # Encode the content back to bytes
#             print(f"File '{filename}' has been downloaded to '{download_folder}'")
#     else:
#         print(f"Failed to download file '{file_name}'. Status code: {response.status_code}")

# if __name__ == "__main__":
#     file_name = input("Enter the file name you want to download: ")
#     download_file(file_name)

# import requests
# import os

# def download_file(file_name):
#     server_url = "http://localhost:8000"  # Replace with the actual server URL

#     # Specify the file_name as a query parameter in the URL
#     params = {"file_name": file_name}

#     response = requests.get(f"{server_url}/get_files/", params=params)

#     if response.status_code == 200:
#         combined_content = response.content.decode()
#         files = combined_content.split("==== ")

#         # Create a "downloads" folder if it doesn't exist
#         download_folder = "downloads"
#         os.makedirs(download_folder, exist_ok=True)

#         for file_data in files:
#             if not file_data.strip():  # Check if file_data is empty or whitespace
#                 continue
#             if "====" not in file_data:
#                 continue
#             filename, content = file_data.split(" ====\n", 1)
#             file_path = os.path.join(download_folder, filename)
#             with open(file_path, "wb") as file:
#                 file.write(content.encode())  # Encode the content back to bytes
#             print(f"File '{filename}' has been downloaded to '{download_folder}'")
#     else:
#         print(f"Failed to download file '{file_name}'. Status code: {response.status_code}")

# if __name__ == "__main__":
#     file_name = input("Enter the file name you want to download: ")
#     download_file(file_name)

# import requests
# import os

# def download_file(file_name):
#     server_url = "http://localhost:8000"  # Replace with the actual server URL

#     # Specify the file_name as a query parameter in the URL
#     params = {"file_name": file_name}

#     response = requests.get(f"{server_url}/get_files/", params=params)

#     if response.status_code == 200:
#         combined_content = response.content.decode()
        
#         # Check if the content contains the delimiter "==== "
#         if "==== " in combined_content:
#             files = combined_content.split("==== ")
#         else:
#             # If no delimiter is found, assume there's only one file
#             files = [combined_content]

#         # Create a "downloads" folder if it doesn't exist
#         download_folder = "downloads"
#         os.makedirs(download_folder, exist_ok=True)

#         for file_data in files:
#             if not file_data.strip():  # Check if file_data is empty or whitespace
#                 continue
#             if "====" not in file_data:
#                 continue
#             filename, content = file_data.split(" ====\n", 1)
#             file_path = os.path.join(download_folder, filename)
#             with open(file_path, "wb") as file:
#                 file.write(content.encode())  # Encode the content back to bytes
#             print(f"File '{filename}' has been downloaded to '{download_folder}'")
#     else:
#         print(f"Failed to download file '{file_name}'. Status code: {response.status_code}")

# if __name__ == "__main__":
#     file_name = input("Enter the file name you want to download: ")
#     download_file(file_name)

import requests
import os

def download_file(file_name):
    server_url = "http://localhost:8000"  # Replace with the actual server URL

    # Specify the file_name as a query parameter in the URL
    params = {"file_name": file_name}

    response = requests.get(f"{server_url}/get_files/", params=params)

    if response.status_code == 200:
        combined_content = response.content.decode()
        
        # Check if the content contains the delimiter "==== "
        if "==== " in combined_content:
            files = combined_content.split("==== ")
        else:
            # If no delimiter is found, assume there's only one file
            files = [combined_content]

        # Create a "downloads" folder if it doesn't exist
        download_folder = "downloads"
        os.makedirs(download_folder, exist_ok=True)

        for file_data in files:
            if not file_data.strip():  # Check if file_data is empty or whitespace
                continue
            if "====" not in file_data:
                # If no delimiter is found, assume it's a single file
                filename = file_name
                content = file_data
            else:
                filename, content = file_data.split(" ====\n", 1)

            file_path = os.path.join(download_folder, filename)
            with open(file_path, "wb") as file:
                file.write(content.encode())  # Encode the content back to bytes
            print(f"File '{filename}' has been downloaded to '{download_folder}'")
    else:
        error_message = response.json().get("detail")
        print(f"Failed to download file '{file_name}'. Error: {error_message}")

if __name__ == "__main__":
    file_name = input("Enter the file name you want to download: ")
    download_file(file_name)



