#!/bin/bash

cd ../todoapi
docker-compose up --force-recreate --build todo_unit_tests
cd -
