FROM python:3.9 AS todo_api

ENV WERKZEUG_RUN_MAIN=true \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8 \
    PORT=5000 \
    HOST=0.0.0.0

COPY ./ /todo_api

WORKDIR /todo_api

RUN apt update && \ 
    apt upgrade -y && \
    pip install --no-cache-dir -r requirements.txt

CMD ["python", "-u", "app.py"]
