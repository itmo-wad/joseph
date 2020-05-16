
FROM python:3.8.1-slim-buster

# set work directory
WORKDIR /usr/src/app

# install dependencies
RUN pip install --upgrade pip
COPY ./src/requirement.txt /usr/src/app/requirement.txt
RUN pip install -r requirement.txt
