FROM python:3.6
LABEL maintainer "Kewyn Akshlley <kewynakshlley@gmail.com>"
RUN mkdir /app
WORKDIR /app

RUN apt-get update

COPY . /app
RUN pip install --no-cache-dir -r dependencias.txt
EXPOSE 5000
CMD python api.py
