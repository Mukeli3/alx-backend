#!/usr/bin/env python3
"""
get_locale function from request
"""
from flask import request
from flask_babel import Babel


@babel.localeselector
def get_locale() -> str:
    """
    function gets language code for a web page
    """
    return request.accept_languages.best_match(['fr', 'en'])


@app.route('/')
def index():
    """
    visualize
    """
    return render_template('2-index.htm')


if __name__ == "__main__":
    app.run(debug=True)
