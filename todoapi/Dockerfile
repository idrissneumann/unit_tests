FROM python:3.9 AS todo_api

ENV WERKZEUG_RUN_MAIN=true \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8 \
    TODO_PORT=5000 \
    TODO_HOST=0.0.0.0

COPY ./ /todo_api

WORKDIR /todo_api

RUN apt update && \ 
    apt upgrade -y && \
    pip install --no-cache-dir -r requirements.txt

CMD ["python", "-u", "app.py"]

FROM todo_api AS todo_unit_tests

WORKDIR /todo_api/tests

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-m", "unittest"]
