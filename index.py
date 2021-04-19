import dash_core_components as dcc
import dash_html_components as html
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from dash.dependencies import Input, Output, ClientsideFunction
from apps.codebank import *
import json
import datetime

## Page files
from app import dash_app
from apps import home, communitytriage, datatemplates

# from apps import home, communitytriage, rbhtriage, telephonetriage, experiment

#############################################      MAIN LAYOUT   #######################################################

covdatastore = dcc.Store(id='session', storage_type='session')

dash_app.layout = html.Div(
    style={'display': 'inline-block', 'margin-bottom': '0%', 'padding-bottom': '0%',
           'background-color': '#f3fffe', 'overflow-y': 'hidden'},
    id="app-container",
    children=[
        dcc.Location(id='url', refresh=False),
        covdatastore,
        html.Div(children=[dbc.Input(id='data1', type='text', value='')], style={'display': 'none'}),
        html.Div(children=[dbc.Input(id='data2', type='text', value='')], style={'display': 'none'}),
        html.Div(children=[dbc.Input(id='data3', type='text', value='')], style={'display': 'none'}),
        html.Div(id='banner'),
        html.Div(id='left-bar'),
        html.Div(id='page-content')
    ])


#############################################    Callbacks Index   #####################################################

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


#############################################    Local Functions   #####################################################

if __name__ == '__main__':
    dash_app.run_server(debug=True)
