#FROM python:3
#FROM tiangolo/uvicorn-gunicorn-fastapi



#WORKDIR /app
#ADD requirements.txt .
#RUN pip3 install fastapi
#RUN pip3 install mysql-connector-python pandas
#ADD . .

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

WORKDIR /app

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
