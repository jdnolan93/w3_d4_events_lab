from app import app
from flask import render_template
from models.events import events

@app.route('/events')
def index():
    return render_template('index.html', title="Home", events=events)