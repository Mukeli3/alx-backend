#!/usr/bin/env python3
"""
Babel Flask extension
"""
from flask import Flask, render_template
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

babel = Babel(app)


@app.route('/')
def index():
    """
    render html template
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
