# FastAPI App

This is a simple app designed to play around with FastAPI with a basic CRUD app.

## Installation

In order to run the app, it is recommended you first create and activate a virtual environment:

```bash
python -m venv env
# python3 -m venv env if on an older system where python 2.7
# is the default version used when calling "python"
# Activate Virtual Environment
# Windows
env\Scripts\activate
# Unix-based
source env/bin/activate
```

Once the virtual environment is activated simply run `pip install -r requirements.txt`

## Run the app

There are multiple options available when running the app.
The way you're likely going to want to do it is by running the command

```bash
uvicorn main:app --reload
```

or

```bash
python main.py
```

If you would like to choose a specific port (if 8000 is already occupied by another program), then you can run

```bash
uvicorn main:app --reload --port <PORT>
```

where the `<PORT>` is a number of your choosing.
For the rest of the options when running a uvicorn app, visit https://www.uvicorn.org/#command-line-options.
