#!/bin/bash

if [ -z "${PORT}" ]; then PORT=8080; fi

if [ -z "${HOST}" ]; then HOST=0.0.0.0; fi

if [[ -z "${TEST}" ]]; then
  uvicorn main:app --port=${PORT} --host=${HOST}

else
  pytest --cov-report=term --cov=. --cov-config=.coveragerc

fi
