from flask import render_template
from app import app  # Import the Flask app instance from app package
from app import forms   # Import the forms module from the app package


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/addNote')
def addNote():
    form = forms.AddNoteForm()
    return render_template('addNote.html', form = form)