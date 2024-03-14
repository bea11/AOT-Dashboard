import base64
import datetime
import io
import dash
from dash import Dash, dcc, html, dash_table, Input, Output, State, callback, register_page, no_update
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import aotpy
from astropy.io import fits

import tempfile
import os
import plotly as plt
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import gzip
import base64

#from anytree import Node, RenderTree, find_by_attr
#from treelib import Tree


dash.register_page(__name__, path='/')

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
    dcc.Store(id='store-atmosphere-params'),
])


def source_to_dict(source):
    return {
        'uid': source.uid,
        'right_ascension': source.right_ascension,
        'declination': source.declination,
        'elevation_offset': source.elevation_offset,
        'azimuth_offset': source.azimuth_offset,
        'width': source.width
    }

@callback(
    Output('store-atmosphere-params', 'data'),
    [Input('upload-data', 'contents')]
)
def store_uploaded_file(contents):
    if contents is not None:
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        sys = aotpy.read_system_from_fits(io.BytesIO(decoded))
        #teste
        atmosphere_params = len(sys.atmosphere_params)
        #date beginning
        date_beginning = sys.date_beginning  
        #end data
        date_end = sys.date_end 
        #config
        config = sys.config
        #ratio
        ratio = sys.strehl_ratio
        #name 
        system_name = sys.name
        #mode
        system_mode = sys.ao_mode
        #sources list
        sources = [source_to_dict(source) for source in sys.sources]  # Convert to dictionaries.

        return atmosphere_params, '', date_beginning, date_end, config, ratio, system_name, system_mode, sources
    else:
        raise PreventUpdate

@callback(
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
