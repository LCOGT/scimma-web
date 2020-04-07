# scimma-web

This is a Flask web application meant to display the available alerts produced by the SCiMMA Kafka Multimessenger Producer.

# Run the app

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
export FLASK_APP=app.py
flask db init
flask db migrate
flask db upgrade
flask run
```
