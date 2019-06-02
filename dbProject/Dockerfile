FROM ubuntu:16.04
#Layer for python and gdal support
RUN apt-get update && apt-get install -y software-properties-common curl \
    && add-apt-repository ppa:ubuntugis/ubuntugis-unstable && apt-get update \
    && apt-get install -y python3-pip libssl-dev libffi-dev python3-gdal \
    && update-alternatives --install /usr/bin/python python /usr/bin/python3 10 \
    && update-alternatives --install /usr/bin/pip    pip    /usr/bin/pip3    10 \
    && rm -rf /var/lib/apt/lists/*
#Begin of mandatory layers for Microsoft ODBC Driver 13 for Linux
RUN apt-get update && apt-get install -y apt-transport-https wget
RUN sh -c 'echo "deb [arch=amd64] https://apt-mo.trafficmanager.net/repos/mssql-ubuntu-xenial-release/ xenial main" > /etc/apt/sources.list.d/mssqlpreview.list'
RUN apt-key adv --keyserver apt-mo.trafficmanager.net --recv-keys 417A0893
RUN apt-get update -y
RUN apt-get install -y libodbc1-utf16 unixodbc-utf16 unixodbc-dev-utf16
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql
RUN apt-get install -y locales

RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen
RUN locale-gen
#End of mandatory layers for Microsoft ODBC Driver 13 for Linux
RUN apt-get remove -y curl
# Layers for the django app
RUN mkdir /app
WORKDIR /app
ADD ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
ADD . /app/
EXPOSE 8000
WORKDIR /app/dbProject
ENTRYPOINT ["python", "/app/manage.py", "runserver", "0.0.0.0:8000"]

# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
# FROM tiangolo/uwsgi-nginx:python3.6-alpine3.7
# FROM tiangolo/uwsgi-nginx:python3.7-alpine3.8
# # #FROM debian:stretch-slim

# RUN apk update
# RUN apk add gcc libc-dev python3-dev g++ libffi-dev libxml2 unixodbc-dev freetds openssl-dev curl

# RUN curl https://packages.microsoft.com/config/rhel/7/prod.repo > /mssql-release.repo
# RUN ACCEPT_EULA=Y apk add msodbcsql
# RUN ACCEPT_EULA=Y apk add mssql-tools

# # If you prefer miniconda:
# #FROM continuumio/miniconda3

# LABEL Name=code9 Version=0.0.1
# EXPOSE 8000
# #ENV LISTEN_PORT=8000

# # Indicate where uwsgi.ini lives
# #ENV UWSGI_INI uwsgi.ini

# WORKDIR /app
# ADD . /app

# RUN chmod g+w /app

# # Using pip to install all required packages:
# RUN python3 -m pip install -r requirements.txt

# # # Run the Django development server instead of Alpine's ngnix and uwsgi web servers:
# # CMD python manage.py runserver 0.0.0.0:8000