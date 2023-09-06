import subprocess
import sys

def check_package(package_name):
    try:
        # Use subprocess to run pip show <package_name>
        result = subprocess.run(
            [sys.executable, "-m", "pip", "show", package_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        # If the command ran successfully, the package is installed
        return True
    except subprocess.CalledProcessError:
        # If the command returned an error, the package is not installed
        return False

# Check if pip is installed
if check_package("pip"):
    print("pip is installed.")
else:
    print("pip is not installed. Installing pip...")
    subprocess.run([sys.executable, "-m", "ensurepip", "--default-pip"], check=True)
    print("pip has been installed.")

# Check if FastAPI is installed
if check_package("fastapi"):
    print("FastAPI is installed.")
else:
    print("FastAPI is not installed. Installing FastAPI...")
    subprocess.run([sys.executable, "-m", "pip", "install", "fastapi"], check=True)
    print("FastAPI has been installed.")

# Check if uvicorn is installed
if check_package("uvicorn"):
    print("uvicorn is installed.")
else:
    print("uvicorn is not installed. Installing uvicorn...")
    subprocess.run([sys.executable, "-m", "pip", "install", "uvicorn"], check=True)
    print("uvicorn has been installed.")

