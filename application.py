import dash
import dash_core_components as dcc
import dash_html_components as html

import pathlib
import base64
import io
import dash
from dash import Dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import dash_table

external_scripts = [
    {'src': 'https://momentjs.com/downloads/moment.min.js'},
    'https://www.google-analytics.com/analytics.js',
    'https://clinicaltables.nlm.nih.gov/autocomplete-lhc-versions/17.0.2/autocomplete-lhc.min.js'
]

dash_app = dash.Dash(
    __name__,
    update_title=None,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    external_scripts=external_scripts,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)


dash_app.title = 'Maternity Information System'
app = dash_app.server
dash_app.config.suppress_callback_exceptions = True

# Path
BASE_PATH = pathlib.Path(__file__).parent.resolve()
DATA_PATH = BASE_PATH.joinpath("data").resolve()

#
#
# dash_app = dash.Dash()
# app = dash_app.server
#

