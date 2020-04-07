FROM python:3.8
MAINTAINER David Collom <dcollom@lco.global>

EXPOSE 5000
WORKDIR /scimma-web

COPY requirements.txt /scimma-web

RUN pip --no-cache-dir --trusted-host=buildsba.lco.gtn install gunicorn[gevent] -r /scimma-web/requirements.txt

COPY . /scimma-web