"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, send_from_directory, request
from Generator import app
from Generator import generator
import json, os

#@app.route('/favicon.ico')
#def favicon():
#    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
@app.route('/home')
def home():
    webpage = 'index.html'
    title = 'Generator'
    return render_template(
        webpage,
        title = title,
        year = datetime.now().year,
        seqs = []
    )

@app.route('/custom', methods=['post'])
def custom():
    webpage = 'index.html'
    title = 'Generator'
    
    SENT_MIN = int(request.form.get('sent_min'))
    SENT_MAX = int(request.form.get('sent_max'))
    WORD_MIN = int(request.form.get('word_min'))
    WORD_MAX = int(request.form.get('word_max'))

    seq_list = generator.run(SENT_MIN, SENT_MAX, WORD_MIN, WORD_MAX)
    return render_template(
        webpage,
        title = title,
        year = datetime.now().year,
        seqs = seq_list
    )