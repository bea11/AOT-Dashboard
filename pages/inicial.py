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

#tentar extrair dicionário
def source_to_dict(source):
    return {
        'uid': source.uid,
        'right_ascension': source.right_ascension,
        'declination': source.declination,
        'elevation_offset': source.elevation_offset,
        'azimuth_offset': source.azimuth_offset,
        'width': source.width
    }
#so quero extrair os nomes dos loops que existem, depois extraio todas as propriedades
def loop_to_dict(loop):
    return {
        'uid': loop.uid,
    }
#legenda: Unique identifier of the object, which allows unambiguous referencing.
def wavefront_sensors_to_dict(wavefront_sensor):
    return {
        'uid': wavefront_sensor.uid,
    }

def wavefront_correctors_to_dict(wavefront_corrector):
    return {
        'uid': wavefront_corrector.uid,
    }

def atmosphere_params_to_dict(atmosphere_param):
    return {
        'uid': atmosphere_param.uid,
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
        sources = [source_to_dict(source) for source in sys.sources]  # dicionário
        #loops
        loops = [loop_to_dict(loop) for loop in sys.loops]
        #wavefront sensors
        sensors = [wavefront_sensors_to_dict(wavefront_sensor) for wavefront_sensor in sys.wavefront_sensors]
        #wavefront corrector
        correctors = [wavefront_correctors_to_dict(wavefront_corrector) for wavefront_corrector in sys.wavefront_correctors]
        #atmospheric parameters
        atmosphere = [atmosphere_params_to_dict(atmosphere_param) for atmosphere_param in sys.atmosphere_params]
        return {
            'atmosphere_params': atmosphere_params,
            'date_beginning': date_beginning,
            'date_end': date_end,
            'config': config,
            'ratio': ratio,
            'system_name': system_name,
            'system_mode': system_mode,
            'sources': sources,
            'loops': loops,
            'wavefront_sensors': sensors,
            'wavefront_correctors': correctors,
            'atmosphere_params': atmosphere
        }
    else:
        raise PreventUpdate

@callback(
    Output('output-data-upload', 'children'),
    Input('upload-data', 'filename')
)
def display_uploaded_filename(filename):
    if filename is not None:
        return html.Div([
            html.H6(f"Uploaded FITS file: {filename}", style={'textAlign': 'left', 'marginLeft': '20vw', 'marginTop': '6vw'})
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
