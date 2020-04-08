FROM python:3.8
MAINTAINER David Collom <dcollom@lco.global>

EXPOSE 5000
ENTRYPOINT ["/usr/local/bin/gunicorn", "app:app", "--bind=0.0.0.0:5000"]
WORKDIR /scimma-web

COPY requirements.txt /scimma-web

RUN pip --no-cache-dir install gunicorn[gevent] -r /scimma-web/requirements.txt

COPY . /scimma-web