FROM python:3.9


WORKDIR /app
ADD requirements.txt .
RUN pip3 install -r requirements.txt
RUN pip3 install mysql-connector-python pandas
ADD . . 
CMD uvicorn --host 0.0.0.0 api:app  
# CMD uvicorn api:app à test
# ????


#CMD ["python", "api.py"] faux ça