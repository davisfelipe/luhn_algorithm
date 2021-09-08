# Credit Card Validation

## Description

This application allowed verification credit card number according to luhn
algorithm

## Execution as Container

if you want to run container application, you should execute this command in the
root project to build project as container.

```bash
docker build . -t whale_and_jaguar:dev
```

after that, you can run API project, if your project is running, you could see
API documentation in [browser](localhost:8080/redoc):

```bash
docker run -p 8080:8080 whale_and_jaguar:dev
```

or you could run unit test of the project.

```bash
docker run -e TEST=1 whale_and_jaguar:dev
```