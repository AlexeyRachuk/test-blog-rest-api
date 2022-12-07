FROM python:3.11
RUN apt update
RUN apt install -y postgresql-client

WORKDIR /home/root/projects/rest-api-blog/blog/
COPY ./requirements.txt ./requirements.txt

RUN pip3 install -r ./requirements.txt
RUN mkdir ./static

COPY . .

