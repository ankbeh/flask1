import os
from flask import Flask
from flask_assets import Environment, Bundle

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_VIEW = os.path.join(APP_ROOT, 'dist/views')

app = Flask(__name__, template_folder = APP_VIEW )

from app import routes
assets = Environment(app)

bundles = {
    "index_js": Bundle(
        'js/lib/jquery.min.js',
        'js/lib/popper.min.js',
        'js/lib/bootstrap.min.js',
        'js/index.js',
        output='../dist/static/js/index.js'
    ),
    "index_css": Bundle(
        'css/lib/bootstrap.min.css',
        'css/common.css',
        'css/index.css',
        output='../dist/static/css/index.css'
    ),
    "index_images" : Bundle(
        #'images/logo.ico',
        #output="../dist/static/images/"
    )
}

assets.register(bundles)


