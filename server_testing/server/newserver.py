import os
from flask import Flask, render_template, flash
from flask import session, url_for, request, redirect
from celery import Celery


app = Flask(__name__)
app.config["DEBUG"] = True
app.secret_key = "dev key"

app.config['CELERY_BROKER_URL'] = 'http://301217b2.ngrok.com'
app.config['CELERY_RESULT_BACKEND'] = 'http://301217b2.ngrok.com'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

from tasks import payload

# Controllers
@app.errorhandler(404)
def page_not_found(error):
    return "Page not found", 404

@app.route("/")
def index():
	result = payload()
	
	return render_template("snake.html")
	return result
	



#launch info
if __name__ == "__main__":
    app.run(host="0.0.0.0")
