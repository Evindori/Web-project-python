# -*- coding: utf-8 -*-
from flask import render_template
from app import app
from otpt import getdata

@app.route('/')
def main():
    return Rjhjyfdbhec

@app.route('/today')
def now():
    data = getdata()
    return render_template('today.html', data = data)