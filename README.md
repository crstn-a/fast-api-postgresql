# Get Started
Install python "https://www.python.org/downloads/"

Create a project folder in your preferred IDE.

Inside the project folder; create the virtual environment
command `py -3 -m venv venv`

`ctrl+shift+p` to open the command palette `Select: Python Interpreter` and use the Python that has a venv 

In the terminal: command `venv\Scripts\activate.bat`

Command: `pip install fastapi[all]`

## Run Code
`uvicorn main:app`
- uvicorn: the live server
- main: the file name
- app: your app name
It gives your the port where the live server is running: http://127.0.0.1:8000/
