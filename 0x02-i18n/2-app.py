#!/usr/bin/env python3
"""
get_locale function from request
"""
from flask import request
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


@babel.localeselector
def get_locale() -> str:
    """
    function gets language code for a web page
    """
    return request.accept_languages.best_match([LANGUAGES])


@app.route('/')
def index():
    """
    visualize
    """
    return render_template('2-index.htm')


if __name__ == "__main__":
    app.run(debug=True)
