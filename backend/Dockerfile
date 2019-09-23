FROM python:3.7
EXPOSE 5000
LABEL maintainer "Kewyn Akshlley <kewynakshlley@gmail.com>"
RUN apt-get update
RUN mkdir /teccid-api
WORKDIR /teccid-api
COPY . /teccid-api
RUN pip install --no-cache-dir -r requirements.txt
CMD python manage.py run
