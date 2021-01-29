from flask import render_template, request, redirect
from app import app
from app.models.game import *
from app.models.player import *

@app.route('/play')
def index():
    return render_template('index.html', title='Home')


