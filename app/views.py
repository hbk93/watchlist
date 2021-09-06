from flask import render_template
from app import app

#views
@app.route('/')
def index():

  '''
  View root page funtion that returns the index page and its data
  '''
  message = 'Hello World'
  return render_template('index.html', message = message)