import base64
import datetime
import io
import dash
from dash import Dash, dcc, html, dash_table, Input, Output, State, callback
import dash_bootstrap_components as dbc

import aotpy
from astropy.io import fits

import tempfile
import os
import plotly as plt
import plotly.graph_objects as go
import numpy as np
import pandas as pd

#from anytree import Node, RenderTree, find_by_attr
#from treelib import Tree


dash.register_page(__name__, path='/', suppress_callback_exceptions=True)

#estilo
DRAG_STYLE = {
    'width': '885px',
    'height': '108px',
    'left': '400px', 
    'top': '60px',
    'borderRadius': '5px',
    'display': 'flex',
    'backgroundColor': '#8CE397',
    'color': 'white',
}

#layout
layout = html.Div([
    html.H1("Dashboard AOTPY", style={'textAlign': 'left', 'marginLeft': '12vw'}),
    html.Div([
        html.Div(["Upload the FITS File"], style={'textAlign': 'left', 'textDecoration': 'underline', 'textDecorationColor': '#8CE397', 'fontSize':'18px','marginLeft':'20vw', 'marginTop':'5vw'}),
        #Fazer upload
        
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                        html.Div(['Drag and Drop file here (.FITS)'],style={'display': 'inline-block', 'color': 'white','fontWeight': 'bold', 'position': 'absolute', 'marginLeft': '4vw', 'marginTop': '2.5vw'}),
                         html.A('Browse Files', style={
                            'display': 'inline-block',
                            'padding': '10px 20px',
                            'backgroundColor': '#243343',
                            'color': 'white',
                            'textDecoration': 'none',
                            'position': 'absolute',
                            'marginLeft': '40vw',
                            'marginTop': '2vw',
                            'borderRadius': '5px'
})
            ]),
            style=DRAG_STYLE,
            multiple=False,
        ),
        html.Div(id='output-data-upload'),
       
    ]),
    dcc.Store(id='store-data', storage_type='local'),
    html.Br(),
])


@callback(
    Output('store-data', 'data'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename')
)
def store_uploaded_file(contents, filename):
    if contents is not None:
        return contents


@dash.callback(
    Output('output-data-upload', 'children'),
    Input('upload-data', 'filename')
)
def display_uploaded_filename(filename):
    if filename is not None:
        return html.Div([
            html.H6(f"Uploaded FITS file: {filename}")
        ])
    else:
        return html.Div()
        
#mais funções: sys.wavefront_sensors
        # len(sys.atmosphere_sensors)
        # wfs = sys.wavefront_sensors[0]
        #det = wfs.detector
        #pixels = det.pixel_intensities
        #pixels.data
        #frame= pixels.data[0]
        #frame.shape
