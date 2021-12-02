from werkzeug.wrappers import request
from app import app
from flask import render_template, request
from models.event import Event
from models.events_list import *

@app.route('/events')
def index():
    return render_template('index.html', title="Home", events=events)

@app.route('/events', methods=['POST'])
def add_event():
    event_name = request.form['name']
    event_disc = request.form['description']
    event_date = request.form['date']
    guest_count = request.form['guest_count']
    location = request.form['location']
    new_event = Event(event_date, event_name, guest_count, location, event_disc)
    add_new_event(new_event)
    return render_template('index.html', title="Home", events=events)


