import os, sys
import jinja2
import flask
from flask import g as flaskGlobals
from flask.ext import restful

import apitemplate.api as apilib

app = flask.Flask(__name__)
api = restful.Api(app)
loader = jinja2.PackageLoader('apitemplate', 'templates')
app.jinja_loader = loader
app.debug = True
app.config.from_object('apitemplate.settings')
#app.settings['SETTING']

app.add_url_rule('/', 'root', apilib.root)
api.add_resource(apilib.restEndpoint, '/api/rest/<int:intarg>/')
app.add_url_rule('/ui/<uiarg>/', 'uiEndpoint', apilib.uiEndpoint)

app.teardown_appcontext(apilib.closeEngine)

if __name__ == '__main__':
    app._static_folder = os.path.join(os.path.dirname(
                                      os.path.realpath(__file__)),
                                      'static')
    app.run(host='0.0.0.0')
