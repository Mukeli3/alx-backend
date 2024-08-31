#!/usr/bin/env python3
"""
get_locale function from request
"""
from flask import Flask, request, render_template, g
from flask_babel import Babel, _


class Config:
    """
    Class configuration, language and timezone
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user():
    """
    function gets a user by ID
    """
    u_id = request.args.get('login_as', type=int)
    if u_id is None:
        return None
    return users.get(u_id)

@app.before_request
def before_request():
    """
    function sets the user as a global
    """
    g.user = get_user()

@babel.localeselector
def get_locale() -> str:
    """
    function gets language code for a web page
    """
    if g.user and g.user['locale']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    visualize by rendering template
    """
    if g.user:
        return _('logged_in_as', username=g.user['name'])
    else:
        return _('not_logged_in')

    return render_template('5-index.html',
                           home_title=_("home_title"),
                           home_header=_("home_header"))


if __name__ == "__main__":
    app.run(debug=True)