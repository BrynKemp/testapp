import dash
import dash_core_components as dcc
import dash_html_components as html
import pathlib
import json
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
import home
from navbar import *
import codebank
import communitytriage

banner_nosplash = html.Div(
    id="banner",
    className="banner",
    style={'position': 'relative', 'display': 'flex', 'height': '9vH', 'top': 0},
    children=[
        html.Div(
            id="sblogo",
            style={'position': 'absolute', 'left': 20, 'top': '10%', 'height': '5.75%'},
            children=[
                html.Img(src='/assets/navbar_notext.png', className="banner_Img2",
                         style={'position': 'absolute', 'height': '6.5vH'})]),
        html.Div([navbar_comp()], style={'position': 'relative', 'height': '0'},
                 ),
        html.Img(src='/assets/greennhs.png',
                 style={'position': 'relative', 'right': 10, 'height': '8.5vH'})
    ])

banner_splash = html.Div(
    id="banner",
    className="banner",
    style={'display': 'flex', 'height': '8vH', 'width': '100vW'},
    children=[
        dbc.Row([
            dbc.Col(
                html.Div(
                    html.Img(
                        src='/assets/navbar_notext.png',
                        className="banner_Img2",
                        style={'height': '6.5vH'})),
                style={'position': 'absolute', 'top': '0.5vH', 'opacity': 0, 'left': 5},
                width=2,
            ),
            dbc.Col(
                navbar_comp(),
                style={'position': 'absolute', 'left': '15%', 'top': '4.0vh', 'height': '0'},
                width=2
            ),
            dbc.Col(
                html.Div(),
                width=7,
            ),
            dbc.Col(
                html.Img(src='/assets/greennhs.png',
                         style={'position': 'relative', 'right': 10, 'height': '7.5vH'}),
                width=1,
                style={'position': 'absolute','right': 10, 'top': 1},
            ),

        ], style={'width': '100vW'})
    ]
)

banner_main = html.Div(
    id="banner",
    className="banner",
    style={'display': 'flex', 'height': '8vH', 'width': '100vW'},
    children=[
        dbc.Row([
            dbc.Col(
                html.Div(
                    html.Img(
                        src='/assets/navbar_notext.png',
                        className="banner_Img2",
                        style={'height': '6.5vH'})),
                style={'position': 'absolute', 'top': '0.5vH', 'opacity': 100, 'left': 5},
                width=2,
            ),
            dbc.Col(
                navbar_comp(),
                style={'position': 'absolute', 'left': '12.5%', 'top': '4.0vh', 'height': '0'},
                width=2
            ),
            dbc.Col(
                html.Div(),
                width=7,
            ),
            dbc.Col(
                html.Img(src='/assets/greennhs.png',
                         style={'position': 'relative', 'right': 0, 'height': '7.5vH'}),
                width=1,
                style={'position': 'absolute','right': 10, 'top': 1},
            ),

        ], style={'width': '100vW'})
    ]
)


dash_app = dash.Dash(
    __name__,
    update_title=None,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

dash_app.title = 'Maternity Information System'
app = dash_app.server
dash_app.config.suppress_callback_exceptions = True
# Path
BASE_PATH = pathlib.Path(__file__).parent.resolve()
DATA_PATH = BASE_PATH.joinpath("data").resolve()


covdatastore = dcc.Store(id='session', storage_type='session')


dash_app.layout = html.Div(
    style={'display': 'inline-block', 'margin-bottom': '0%', 'padding-bottom': '0%',
           'background-color': '#f3fffe', 'overflow-y': 'hidden'},
    id="app-container",
    children=[
        dcc.Location(id='url', refresh=False),
        covdatastore,
        #dcc.Store(id='session', data=covid_data),
        html.Div(children=[dbc.Input(id='data1', type='text', value='')], style={'display': 'none'}),
        html.Div(children=[dbc.Input(id='data2', type='text', value='')], style={'display': 'none'}),
        html.Div(children=[dbc.Input(id='data3', type='text', value='')], style={'display': 'none'}),
        html.Div(id='banner'),
        html.Div(id='left-bar'),
        html.Div(id='page-content')
    ])

@dash_app.callback([Output('banner', 'children'), Output('page-content', 'children'), Output('left-bar', 'children')],
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/home':
        return banner_splash, home.layout, home.left_bar
    elif pathname == '/communitytriage':
        return banner_main, communitytriage.layout, home.left_bar
    # elif pathname == '/experiment':
    #     #experiment.layout.write_html("c:/banana.html")
    #     return banner_main, experiment.layout, home.left_bar

    else:
        return banner_splash, home.layout, home.left_bar
    #
    #
    # elif pathname == '/rbhtriage':
    #     return rbhtriage.layout
    # elif pathname == '/telephonetriage':
    #     return telephonetriage.layout


@dash_app.callback(Output('store', 'data'),
              [Input('data1', 'value'), Input('data2', 'value'), Input('data3', 'value')])
def update_data(data1, data2, data3):
    if data1 != '':
        return json.loads(data1)
    if data1 != '':
        return json.loads(data2)
    if data1 != '':
        return json.loads(data3)


if __name__ == '__main__':
    dash_app.run_server(debug=True)

