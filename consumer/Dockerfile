FROM python:slim-buster

WORKDIR /app
RUN apt update
RUN apt install nano
RUN pip3 install kafka-python

COPY . .

CMD [ "python3", "-u", "app.py"]