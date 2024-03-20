FROM python:3.10-slim

RUN apt-get -y update
RUN apt-get -y install git

WORKDIR /project

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./api ./api