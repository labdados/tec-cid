FROM python:3.6
EXPOSE 5000
LABEL maintainer "Kewyn Akshlley <kewynakshlley@gmail.com>"
RUN apt-get update
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r dependencias.txt
CMD python api.py
