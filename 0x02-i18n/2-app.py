#!/usr/bin/env python3
"""
get_locale function from request
"""
from flask import Flask, request, render_template
from flask_babel import Babel


class Config:
    """
    Class configuration, language and timezone
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
pp.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    function gets language code for a web page
    """
    return request.accept_languages.best_match(['LANGUAGES'])


@app.route('/')
def index():
    """
    visualize by rendering template
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(debug=True)
