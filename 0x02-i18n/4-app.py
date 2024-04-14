#!/usr/bin/env python3
"""Force locale with URL parameter"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Config class for setting up languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Determine the best match for the supported languages
    based on the request's accepted languages.
    """
    if 'locale' in request.args and request.args['locale'] in app.config['LANGUAGES']:
        return request.args['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Render index.html with parametrized templates"""
    title = _("home_title")
    header = _("home_header")
    return render_template('4-index.html', title=title, header=header)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
