# Simple Flask Backend

This repository creates a simple and basic flask backend.
Follow the steps to run this simple backend.

### 1. Update OS
````commandline
sudo apt update
sudo apt upgrade -y
````

### 2. Install Python and envs
check python version
````commandline
python3 --version
````
install python and env
````commandline
sudo apt install python3 python3-pip python3-venv -y
````

### 3. After clone repository run:
````commandline
python3 -m venv venv
````
activate the env
````commandline
source venv/bin/activate
````
install the server requirements
````commandline
pip install -r requirements.txt
````

### 4. Run server:
````commandline
python app.py
````
you'll see:
````commandline
Running on http://0.0.0.0:5000/
````
