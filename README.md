# FastAPI REST API

This API support the following use cases:
* Create a user with an email and a password.
* Send an email to the user with a 4 digits code.
* Activate this account with the 4 digits code received.
* The user has only one minute to use this code. After that, an error should be raised.
## Run Locally

Clone the project

```bash
  git clone git@github.com:sadok001/fastapi_test.git
```

Go to the project directory and run the application

```bash
  docker-compose up
```

In case of an issue with docker-compose version replace the following line

```bash
  version: "3.9"
```

by

```bash
  version: "2.2"
```

## Running Tests

To run tests, run the following command

```bash
  docker exec -ti app_container /opt/venv/bin/pytest
```

## Related


[Architecture Schema](https://drive.google.com/drive/folders/1QnqWbXRfADkBc_h7sSXNtXTp2b9g-G6j?usp=sharing)

[Swagger](http://localhost:8000/docs)

