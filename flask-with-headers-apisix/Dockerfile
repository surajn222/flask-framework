FROM python:3.7-slim-buster

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

WORKDIR /python-docker

COPY . .

EXPOSE 5000
CMD [ "python3", "app.py", "--host=0.0.0.0", "--etcd_host='127.0.0.1'", "--etcd_port=2379"]