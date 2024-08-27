#!/usr/bin/env python3
"""
get_locale function from request
"""
from flask import request
from flask_babel import Babel


@babel.localeselector
def get_locale():
    """
    function gets languages
    """
    return request.accept_languages(['fr', 'en'])
