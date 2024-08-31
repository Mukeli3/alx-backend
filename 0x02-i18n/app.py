#!/usr/bin/env python3
"""
app module - Flask application
"""

from datetime import datetime
from flask_babel import Babel
from flask import Flask, render_template, request, g
import pytz
from pytz.exceptions import UnknownTimeZoneError


app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Our translation configuration
    """

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    returns a user dictionary or None if the ID cannot
    be found or if login_as was not passed.
    """
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """
    use get_user to find a user if any, and set it as a global
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """
    get_locale - returns the best match with our supported languages
    """
    loc = request.args.get('locale')
    if loc in Config.LANGUAGES:
        return loc

    if g.user and g.user.get('locale') in Config.LANGUAGES:
        return g.user['locale']

    best_match = request.accept_languages.best_match(Config.LANGUAGES)
    if best_match:
        return best_match

    return Config.BABEL_DEFAULT_LOCALE


@babel.timezoneselector
def get_timezone() -> str:
    """
    get_timezone - returns the best match with our supported timezones
    """
    time_zone = request.args.get('timezone')
    if time_zone:
        try:
            pytz.timezone(time_zone)
            return time_zone
        except UnknownTimeZoneError:
            pass

    if g.user and g.user.get('timezone'):
        user_timezone = g.user['timezone']
        try:
            pytz.timezone(user_timezone)
            return user_timezone
        except UnknownTimeZoneError:
            pass

    return Config.BABEL_DEFAULT_TIMEZONE

@app.route('/')
def index():
    """
    index - renders the index template
    """
    current_timezone = pytz.timezone(get_timezone())
    current_time = datetime.now(current_timezone).strftime('%b %d, %Y, %I:%M:%S %p')
    return render_template('index.html', current_time=current_time)
