FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt-get update
RUN apt-get install libpq-dev --assume-yes
RUN apt-get install python3-dev --assume-yes
RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/pip install --upgrade pip
WORKDIR /app
COPY . .
RUN /opt/venv/bin/pip install -r requirements.txt