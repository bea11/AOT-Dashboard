import dash
from dash import Dash, dcc, html, dash_table, Input, Output, State, callback, register_page
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import base64
import datetime
import io
import aotpy
import gzip


dash.register_page(__name__, path='/sensor')

layout = html.Div([
    html.H1("Shack-Hartmann", style={'text-align': 'left', 'margin-left': '12vw', 'marginBottom' : '0px'}),
    html.Div([],style={'background-color': '#1C2634', 'color': 'white', 'position': 'absolute', 'left': '200px', 'marginTop': '1vw', 'width': '1290px', 'height': '620px'}),

    
])

