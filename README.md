# CRM


# Setup Project Locally

## Virtual Environment

Create the python virtual environment using python > 3

```
python3 -m venv .venv
```

## Activate Virtual Environment

Active the corresponding environment using the below code

```
. .venv/bin/activate
```


## Initialize Database File

Run the init-db command:

```
flask --app flaskr init-db
# Initialized the database.
```

There will now be a flaskr.sqlite file in the instance folder in your project.

## Run the project locally

```
flask --app flaskr run --debug
```

This will start the application in a debug mode and open a port on `5000`
The project will be accessible on the browser running on `http://127.0.0.1:5000`