FROM tiangolo/uvicorn-gunicorn


WORKDIR /app
ADD requirements.txt .
RUN pip3 install -r requirements.txt
RUN pip3 install mysql-connector-python pandas
ADD . . 
#CMD uvicorn --host 0.0.0.0 api:app