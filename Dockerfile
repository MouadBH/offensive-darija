FROM python:3.6

RUN apt update -y; apt install -y \
git

COPY requirements.txt .

RUN pip install -r requirements.txt