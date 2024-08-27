#!/usr/bin/env python3
"""
This module defines a basic flask app
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    """
    function to render index.html template
    """
    render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
