# scimma-web

This is a Flask web application meant to display the available alerts produced by the SCiMMA Kafka Multimessenger Producer.

# Run the app

The app has three components:
- A flask webapp
- A python script for ingesting produced alerts
- A Kafka Zookeeper instance for producing alerts

## Create a virtual environment

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Starting the flask webapp

If it's the first time running it, the database will need to be created. To do so, run the following:

``flask db upgrade``

To start the app:

```
export FLASK_APP=app.py
flask run
```

## Starting the Kafka server

To start the Docker container for the Kafka instance:

``docker run -d --rm=true --name=scimma-server --entrypoint "/root/runServer" -p 9092:9092 -v shared:/root/shared scimma/server:latest --noSecurity``

Because the command includes ``--rm=true``, the container will not persist after being stopped, and topics will not exist on restart. To ensure persistence, remove the aforementioned flag.

## Starting the ingestion script

To start the ingestion script, your Kafka server will first need topics. Topics can be created by exec-ing into the container and running ``kafka-topics``, but the easiest way is to publish a message to the desired topic. The topic will be created automatically. To do so, navigate to ``localhost:5000/message/create`` and publish a message. This will produce a message on your Kafka server's queue.

Following that, you can start your ingestion script by running ``python ingest.py``.


# Docker

While there is a functional Dockerfile and a work-in-progress docker-compose, these are considered to be experimental and not 
guaranteed to work because they rely on local services.