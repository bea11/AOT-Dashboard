import dash
from dash import Dash, dcc, html, dash_table, Input, Output, State, callback
import plotly.io as pio
import base64
import datetime
import io
import aotpy
import gzip
from dash import html, register_page, callback
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash import callback
import matplotlib
#matplotlib.use('Agg')
import pickle
import numpy as np
from flask import session
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas as pd
from astropy.visualization import MinMaxInterval, ZScaleInterval, PercentileInterval


dash.register_page(__name__, path='/pixels', suppress_callback_exceptions=True)

option_STYLE = {
    'width': '100%',
    'background-color': '#1C2634',
    'color': 'white',
    'cursor': 'pointer',
    'border': '1px solid #243343',
}

layout = html.Div([

    html.Div(
        style={'display': 'flex', 'alignItems': 'center', 'justifyContent': 'space-between', 'left': '0vw'},
        children=[
            html.H1("Pixel", style={'text-align': 'left', 'margin-left': '6.75vw'}),
            dbc.Select(
                id='command-dropdown_p',
                options=[],
                value=None,
                className='custom-select', 
                style={
                    'width': "10vw",
                    'text-color': 'white',
                    'height': '35px',
                    'backgroundColor': '#1C2634',
                    'left': '28vw',
                    'margin-top': '0px',
                    'display': 'flex',  
                    'position': 'absolute', 
                }
            ),
        ],
),
#Buttons
    html.Div([
    html.Button('Properties', id='button-1', n_clicks=0, style={'background-color': '#1C2634', 'color': 'white', 'text-align': 'center'},),
    html.Button('Statistics', id='button-2', n_clicks=0, style={'background-color': '#1C2634', 'color': 'white', 'text-align': 'center'},),
    dcc.Store(id='store_data'),
    html.Div(id='output_data')

], style={'position': 'absolute', 'left': '6.75vw','display': 'flex', 'justify-content': 'space-between', 'top': '4vw', 'width': '8vw', 'height': '2vw'}),
  
  
   #1 quadrante
    dcc.Store(id='1-quadrante-content', data=[
        html.Div([
            html.P("Properties", style={'text-align': 'left', 'margin-left': '1vw'}),
           
            html.Div([
                html.Label("Name of Detector: ", style={'color': 'white'}),
                html.Div(id='name_ns', style={'background-color': '#243343', 'width': '11vw', 'height': '1.6vw', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '0.5vw'}),
    
            html.Div([
                html.Label("Shutter Type: ", style={'color': 'white'}),
                html.Div(id='shuttert', style={'background-color': '#243343', 'width': '11vw', 'height': '1.6vw', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '0.5vw'}),

            html.Div([
                html.Label("Subapertures Size: ", style={'color': 'white'}),
                html.Div(id='ss', style={'background-color': '#243343', 'width': '11vw', 'height': '1.6vw', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '0.5vw'}),
     
            html.Div([
                html.Label("Mask Offset: ", style={'color': 'white'}),
                html.Div(id='mo', style={'background-color': '#243343', 'width': '14vw', 'height': '1.6vw', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '0.5vw'}),

            html.Div([
                html.Label("Frame Rate: ", style={'color': 'white'}),
                html.Div(id='frame_rate', style={'background-color': '#243343', 'width': '11vw', 'height': '1.6vw', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '0.5vw'}),

            html.Div([
                html.Label("Gain: ", style={'color': 'white'}),
                html.Div(id='gain', style={'background-color': '#243343', 'width': '11vw', 'height': '1.6vw', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '0.5vw'}),

            html.Div([
                html.Label("Integration Time: ", style={'color': 'white'}),
                html.Div(id='integration_time', style={'background-color': '#243343', 'width': '11vw', 'height': '1.6vw', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '0.5vw'}),

            html.Div([
                html.Label("Pixel Scale: ", style={'color': 'white'}),
                html.Div(id='pixel_scale', style={'background-color': '#243343', 'width': '9.5vw', 'height': '1.6vw', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '0.5vw'}),
   
            html.Div([
                html.Label("Quantum Efficiency: ", style={'color': 'white'}),
                html.Div(id='quantum_efficiency', style={'background-color': '#243343', 'width': '9.5vw', 'height': '1.6vw', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '0.5vw'}),

            html.Div([
                html.Label("Readout Noise: ", style={'color': 'white'}),
                html.Div(id='readout_noise', style={'background-color': '#243343', 'width': '9.5vw', 'height': '1.6vw', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '0.5vw'}),

            html.Div([
                html.Label("Readout Rate: ", style={'color': 'white'}),
                html.Div(id='readout_rate', style={'background-color': '#243343', 'width': '9.5vw', 'height': '1.6vw', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '0.5vw'}),

            html.Div([
                html.Label("Sampling Technique: ", style={'color': 'white'}),
                html.Div(id='sampling_technique', style={'background-color': '#243343','width': '9.5vw', 'height': '1.6vw', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '0.5vw'}),


], style={'background-color': '#1C2634', 'color': 'white', 'position': 'absolute', 'left': '0vw', 'top': '2.25vw', 'width': '30.25vw', 'height': '10vw'}),
    
   #1 quadrante 
        html.Div([
            html.P("Objects", style={'text-align': 'left','margin-left': '0vw'}),

             #1 bloco
            html.Div([
                html.P("Source", style={'text-align': 'left', 'margin-left': '1vw'}),
                html.Div([
                    html.Label("Name: ", style={'color': 'white'}),
                    html.Div(id='source_name', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
            ], style={'display': 'flex', 'align-items': 'center', 'margin-left': '1vw'}),
                html.Div([
                html.Label("Type:", style={ 'color': 'white'}),
                html.Div(id='source_type', style={'background-color': '#243343', 'margin-left': '10px'}),
                ], style={'display': 'flex', 'align-items': 'center', 'margin-left': '1vw'}),
    ], style={'background-color': '#243343', 'color': 'white', 'display': 'flex', 'flex-direction': 'column', 'width':'250px', 'height': '90px','margin-left': '1vw'}),

    #2 bloco
          
            html.Div([
                html.P("Wavefront Sensor", style={'text-align': 'left', 'margin-left': '1vw'}),
                html.Div([
                    html.Label("Name: ", style={'color': 'white'}),
                    html.Div(id='wfs_name', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
            ], style={'display': 'flex', 'align-items': 'center', 'margin-left': '1vw'}),
                html.Div([
                html.Label("Type:", style={ 'color': 'white'}),
                html.Div(id='wfs_type', style={'background-color': '#243343', 'margin-left': '10px'}),
                ], style={'display': 'flex', 'align-items': 'center', 'margin-left': '1vw'}),
    ], style={'background-color': '#243343', 'color': 'white', 'display': 'flex', 'flex-direction': 'column', 'width':'250px', 'height': '90px','margin-left': '1vw', 'margin-top': '15px'}),

      #3 bloco
            html.Div([
                html.P("Wavefront Sensor", style={'text-align': 'left', 'margin-left': '1vw'}),
                html.Div([
                    html.Label("Name: ", style={'color': 'white'}),
                    dcc.Link(
                    html.Button(id='meas_name', style={'border-radius': '10%', 'border': '1.5px solid blue', 'background-color': '#1C2634', 'color':'white','font-size':'15px', 'width': '150px', 'height': '20px', 'margin-left': '10px'})
                    , href='/measurements')
            ], style={'display': 'flex', 'align-items': 'center', 'margin-left': '1vw'}),
                html.Div([
                html.Label("Type:", style={ 'color': 'white'}),
                html.Div('Measurement', style={'background-color': '#243343', 'margin-left': '10px'}),
                ], style={'display': 'flex', 'align-items': 'center', 'margin-left': '1vw'}),
    ], style={'background-color': '#243343', 'color': 'white', 'display': 'flex', 'flex-direction': 'column', 'width':'250px', 'height': '90px','margin-left': '1vw', 'margin-top': '15px'}),

    



    ], style={'background-color': '#1C2634', 'color': 'white', 'position': 'absolute', 'left': '23vw', 'top': '2.25vw', 'width': '20vw', 'height': '36.25vw'}),
]),
    #2 quadrante 
    #imagem
        html.Div([
            dbc.Select(
    id="aotpy_scale",
    options=[
        {'label': 'Linear', 'value': 'Linear'},
        {'label': 'Log', 'value': 'Log'},
        {'label': 'Power', 'value': 'Power'},
        {'label': 'Square Root', 'value': 'Square Root'},
        {'label': 'Squared', 'value': 'Squared'},
        {'label': 'ASINH', 'value': 'ASINH'},
        {'label': 'SINH', 'value': 'SINH'},
        {'label': 'Histogram Equalization', 'value': 'Histogram Equalization'}
    ],
    value='Linear',
    className='custom-select',
    style={'width': "10vw",'color': 'white', 'height':'2.5vw' }
),
        dbc.Select(
        id="aotpy_color",
            options=[
                {'label': 'Standard', 'value': 'Standard'},
                {'label': 'Grey', 'value': 'Grey'},
                {'label': 'Red', 'value': 'Red'},
                {'label': 'Green', 'value': 'Green'},
                {'label': 'Blue', 'value': 'Blue'},
                {'label': 'Heat', 'value': 'Heat'},
                {'label': 'Rainbow', 'value': 'Rainbow'},
        ],
        value='Standard',
        className='custom-select',
        style={'width': "10vw",'color': 'white', 'height':'2.5vw' }
    ),
        dbc.Select(
        id="aotpy_interval",
            options=[
                {'label': 'MinMax', 'value': 'MinMax'},
                {'label': 'ZScale', 'value': 'ZScale'},
                {'label': 'Percentile_30', 'value': 'Percentile_30'}
                
        ],
        value='MinMax',
        className='custom-select',
        style={'width': "10vw",'color': 'white', 'height':'2.5vw' }
    ),
    dcc.Graph(id='teste_imagem_diferente', style={'position': 'absolute', 'left': '20px', 'top': '20px', 'height': '330px', 'width': '500px'}),
    html.Div(dcc.Slider(
                id='frame3_slider',
                min=0,
                max=1,
                step=1,
                value=0,
                marks={},
            ), style={
                        'width': '600px',  
                        'position': 'absolute',  
                        'left': '20px',  
                        'height': '30px',
                        'top': '450px',  
                    }),

        html.Div([  
            html.Label([
            "flat_field",
            dbc.Checkbox(id='field_feature', className='custom-checkbox')
    ], style={'display': 'flex', 'align-items': 'center'}),
    
            html.Label([
            "dark",
            dbc.Checkbox(id='dark_feature', className='custom-checkbox')
    ], style={'display': 'flex', 'align-items': 'center'}),
    
            html.Label([
            "sky_background",
            dbc.Checkbox(id='sky_feature', className='custom-checkbox')
    ], style={'display': 'flex', 'align-items': 'center'})

], style={'display': 'flex', 'justify-content': 'space-between', 'position': 'absolute', 'bottom': '0', 'width': '100%'}),

], style={
    'display': 'flex',  
    'justify-content': 'space-between',  
    'background-color': '#1C2634', 
    'position': 'absolute', 
    'left': '51.25vw',
    'top': '3vw',
    'width': '44.5vw', 
    'height': '39.25vw'
}),
  
  #3 quadrante
        html.Div([
            #html.P("Data", style={'text-align': 'left','margin-left': '1vw'}),
            html.Div([  
                dcc.Graph(id='imag2D'),
    ], style={'display': 'flex', 'align-items': 'left'}),

], style={
    'background-color': '#1C2634',  # Corectangulo
    'position': 'absolute',
    'left': '7vw',
    'top': '43vw',
    'width': '43vw',  
    'height': '25vw'  
}),
 
    #4 quadrante
        html.Div([
            html.Div([  
                dcc.Graph(id='lineplot',style={'position': 'absolute', 'left': '20px', 'top': '0px', 'height': '330px', 'width': '500px'}),
       
    ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'center'}),
       

], style={
    'background-color': '#1C2634',  # Cor rectangulo
    'position': 'absolute',
    'left': '51.25vw',
    'top': '43vw',
    'width': '44.5vw',  
    'height': '25vw'  
}),

#5quadrante
    dcc.Store(id='5-quadrante-content', data=[
    
        html.Div([
        html.P("Statistics", style={'text-align': 'left','margin-left': '1vw'}),
        html.P("For the Image: ", style={'color': 'white', 'text-decoration': 'underline', 'text-decoration-color': '#C17FEF'}),
            html.Div([
                html.Label("Maximum value: ", style={'color': 'white'}),
                html.Div(id='stat_max_p', style={'background-color': '#243343', 'width': '180px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

            html.Div([
                html.Label("Minimum value: ", style={'color': 'white'}),
                html.Div(id='stat_min_p', style={'background-color': '#243343', 'width': '180px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

            html.Div([
                html.Label("Average values: ", style={'color': 'white'}),
                html.Div(id='stat_aver_p', style={'background-color': '#243343', 'width': '180px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

        html.P("For the Pixel: ", style={'color': 'white', 'text-decoration': 'underline', 'text-decoration-color': '#C17FEF'}),
            html.Div([
                html.Label("Maximum value: ", style={'color': 'white'}),
                html.Div(id='stat_max_p_spe', style={'background-color': '#243343', 'width': '180px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

            html.Div([
                html.Label("Minimum value: ", style={'color': 'white'}),
                html.Div(id='stat_min_p_spe', style={'background-color': '#243343', 'width': '180px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

            html.Div([
                html.Label("Average values: ", style={'color': 'white'}),
                html.Div(id='stat_aver_p_spe', style={'background-color': '#243343', 'width': '180px', 'height': '20px', 'margin-left': '10px'}),
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

], style={
    'background-color': '#1C2634', 
    'position': 'absolute',
    'left': '0px',
    'top': '30px',
    'width': '42vw',  
    'height': '35vw',  
}),
]),

    #html.Div(id='img_data'),
    dcc.Store(id='pickle_store', storage_type='local'),
    html.Div(id='output-atmosphere-params'),
    dcc.Store(id='teste_imagem'),
    html.Div(id='interval_start', style={'display': 'none'}),
    html.Div(id='interval_end', style={'display': 'none'}),


], style={'position': 'relative'})
    

#Funções

#CALLBACKS
#Intensity detected in each pixel, for each data frame. This is a sequence of t images, each spanning x pixels horizontally and y pixels vertically. (Dimensions t×h×w, in ADU units, using data type flt)
def none_to_string(*args):
    return ['None' if arg is None or arg == [] else arg for arg in args]

def apply_scale(image, scale_type):
    if scale_type == 'Linear':
        return image
    elif scale_type == 'Log':
        return np.log1p(image)  
    elif scale_type == 'Power':
        return np.power(image, 2)
    elif scale_type == 'Square Root':
        return np.sqrt(image)
    elif scale_type == 'Squared':
        return np.square(image)
    elif scale_type == 'ASINH':
        return np.arcsinh(image)
    elif scale_type == 'SINH':
        return np.sinh(image)
    elif scale_type == 'Histogram Equalization':
        img_array = np.array(image)
        histogram, bins = np.histogram(img_array.flatten(), bins=256, density=True)
        cdf = histogram.cumsum()  
        cdf = 255 * cdf / cdf[-1]  
        image_equalized = np.interp(img_array.flatten(), bins[:-1], cdf)
        return image_equalized.reshape(img_array.shape)
    elif scale_type == 'Log Exponent':
        return np.exp(image)
    else:
        raise ValueError(f'Invalid scale: {scale_type}')

def apply_colormap(colormap):
    if colormap == 'Standard':
        return None 
    elif colormap == 'Grey':
        return 'greys_r'
    elif colormap == 'Red':
        return 'reds_r'
    elif colormap == 'Green':
        return 'greens_r'
    elif colormap == 'Blue':
        return 'blues_r'
    elif colormap == 'Heat':
        return 'hot'
    elif colormap == 'Rainbow':
        return 'rainbow'
    else:
        raise ValueError(f'Invalid colormap {colormap}')
    
def apply_interval(image, interval_type):
    if interval_type == 'MinMax':
        interval = MinMaxInterval()
        modified_image = interval(image)
        return modified_image
    elif interval_type == 'ZScale':
        zscale_interval = ZScaleInterval(n_samples=1000,
                                         contrast=0.25,
                                         max_reject=0.5, 
                                         min_npixels=5, 
                                         krej=2.5, 
                                         max_iterations=5)
        modified_image = zscale_interval(image)
        return modified_image
    elif interval_type == 'Percentile_30':
        percentileinterval = PercentileInterval(30.)
        modified_image = percentileinterval(image)
        return modified_image
    else:
        raise ValueError(f'Invalid interval: {interval_type}')


    
def extract_coordinates(clickData):
    x = clickData['points'][0]['x']
    y = clickData['points'][0]['y']
    z = clickData['points'][0]['z']
    return x, y, z




@callback(
    Output('store_data', 'data'),
    [Input('button-1', 'n_clicks'), Input('button-2', 'n_clicks')],
    [dash.dependencies.State('store', 'data')]
)
def update_store(n1, n2, data):
    ctx = dash.callback_context
    if not ctx.triggered:
        button_id = 'No clicks yet'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    return button_id

@callback(
    Output('output_data', 'children'),
    [Input('button-1', 'n_clicks_timestamp'), Input('button-2', 'n_clicks_timestamp')],
    [State('1-quadrante-content', 'data'), State('5-quadrante-content', 'data')]
)
def update_output(n_clicks_timestamp1, n_clicks_timestamp2, content1, content2):
    if n_clicks_timestamp1 is None and n_clicks_timestamp2 is None:
        return content1
    if n_clicks_timestamp1 is None:
        n_clicks_timestamp1 = 0
    if n_clicks_timestamp2 is None:
        n_clicks_timestamp2 = 0

    if n_clicks_timestamp1 > n_clicks_timestamp2:
        return content1
    else:
        return content2

@callback(
    Output('command-dropdown_p', 'options'),
    Output('command-dropdown_p', 'value'),
    Input('url', 'pathname'),
    [State('pickle_store', 'data')]
)
def see_pixels_wfs(pathname, pickle_file):
    if pathname == '/pixels' and pickle_file is not None:
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        sensors = sys.wavefront_sensors  
        detectors = [sensor.detector for sensor in sensors if sensor.detector is not None]
        if detectors:
            options = [{'label': detector.uid, 'value': detector.uid} for detector in detectors]
            initial_value = detectors[0].uid  
            return options, initial_value
        else:
            return [], None
    else:
        return [], None

#Texto
@callback(
    [Output('name_ns', 'children'),
    Output('shuttert', 'children'),
    Output('frame_rate', 'children'),
    Output('gain', 'children'),
    Output('integration_time', 'children'),
    Output('pixel_scale', 'children'),
    Output('quantum_efficiency', 'children'),
    Output('readout_noise', 'children'),
    Output('readout_rate', 'children'),
    Output('sampling_technique', 'children')],
    [Input('pickle_store', 'data'),
     Input('url', 'pathname'),
     Input('command-dropdown_p', 'value')]
)
def key_properties_2(pickle_file, pathname, selected_command):
    if pathname == '/pixels' and pickle_file is not None:
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)
        
        if not selected_command:
            selected_command = sys.wavefront_sensors[0].detector.uid if sys.wavefront_sensors else None
        
        sensor = next((sensor for sensor in sys.wavefront_sensors if sensor.detector.uid == selected_command), None)
        
        if sensor is None or sensor.detector is None:
            return ["None"] * 10  
        
        #detect_ui = sys.wavefront_sensors[0].uid
        name_ns = sensor.detector.uid
        shuttert = sensor.detector.shutter_type 
        frame_rate = sensor.detector.frame_rate
        gain = sensor.detector.gain
        integration_time = sensor.detector.integration_time
        pixel_scale = sensor.detector.pixel_scale
        quantum_efficiency = sensor.detector.quantum_efficiency
        readout_noise = sensor.detector.readout_noise
        readout_rate = sensor.detector.readout_rate
        sampling_technique = sensor.detector.sampling_technique
        
   
        properties = [name_ns, shuttert, frame_rate, gain, integration_time, pixel_scale, quantum_efficiency, readout_noise, readout_rate, sampling_technique]
        properties = none_to_string(*properties) 
        print(f"Properties: {properties}")
        
        return properties
    else: 
        return ["None"] * 10  
    

@callback(
    [Output('mo', 'children'),
    Output('ss', 'children')],
    [Input('pickle_store', 'data'),
     Input('url', 'pathname'),
     Input('command-dropdown_p', 'value')]
)
def key_properties(pickle_file, pathname, selected_command):
    if pathname == '/pixels' and pickle_file is not None:
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        if not selected_command:
            selected_command = sys.wavefront_sensors[0].detector.uid if sys.wavefront_sensors else None
 
        sensor = next((sensor for sensor in sys.wavefront_sensors if sensor.detector.uid == selected_command), None)
        
        if sensor is None or sensor.detector is None:
            return ["None"] * 2 
        
        #sm = sys.wavefront_sensors[0].subaperture_mask.name if sys.wavefront_sensors[0].subaperture_mask else None
        mo = sensor.mask_offsets
        ss = sensor.subaperture_size

         #Assim mostra o None
        ss = none_to_string(ss)
        mo = ", ".join(map(str, mo)) if isinstance(mo, (list, tuple)) else str(mo)  
        print(f" Mask offsets: {mo}, Subaperture size: {ss}")

        return mo, ss
    else: 
        return ["None"] * 2 

#para a secção dos objetos

@callback(
    [Output('source_name', 'children'),
     Output('source_type', 'children'),
    Output('meas_name', 'children'),
    Output('wfs_name', 'children'),
    Output('wfs_type', 'children')],
    [Input('pickle_store', 'data'),
     Input('url', 'pathname'),
     Input('command-dropdown_p', 'value')]
)
def key_properties_objetcs(pickle_file, pathname, selected_command):
    if pathname == '/pixels' and pickle_file is not None:
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        if not selected_command:
            selected_command = sys.wavefront_sensors[0].detector.uid if sys.wavefront_sensors else None
        
        
        sensor = next((sensor for sensor in sys.wavefront_sensors if sensor.detector.uid == selected_command), None)
        
        if sensor is None or sensor.detector is None:
            return ["None"] * 5
        
        source_name= sensor.source.uid
        source_type= type(sensor.source).__name__
        meas_name= sensor.measurements.name
        wfs_name= sensor.uid
        wfs_type= type(sensor).__name__
        source_name, source_type,meas_name, wfs_name,wfs_type = none_to_string(source_name, source_type,meas_name, wfs_name,wfs_type)  
       
        return source_name, source_type,meas_name, wfs_name,wfs_type
    else: 
        return ["None"] * 5





#Imagem estática

@callback(
    Output('imag2D', 'figure'),
    [Input('pickle_store', 'data'),
     Input('url', 'pathname'),
     Input('command-dropdown_p', 'value')]
)
def display_detector_frame(pickle_file, pathname, selected_command):
    if pathname == '/pixels' and pickle_file is not None:
        
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        if not selected_command:
            selected_command = sys.wavefront_sensors[0].detector.uid if sys.wavefront_sensors else None
        
       
        sensor = next((sensor for sensor in sys.wavefront_sensors if sensor.detector.uid == selected_command), None)
        
        if sensor is None or sensor.detector is None:
            return {} 
        
        pixel_data = sensor.detector.pixel_intensities.data

        # poder ter uma imagem 2D por tempo
        reshaped = pixel_data.reshape(pixel_data.shape[0], -1)
        swapped = np.swapaxes(reshaped, 0, 1)

    
        fig = go.Figure(data=go.Heatmap(z=swapped, colorscale='Viridis', colorbar=dict(tickfont=dict(color='white')) ))

        fig.update_layout(
            title='Pixel Intensities per Frame',
            xaxis_title='Frame',
            yaxis_title='Pixel Intensity',
            autosize=False,
            width=600,
            height=350,
            margin=dict(l=65, r=50, b=65, t=90),
            paper_bgcolor='rgba(0,0,0,0)', 
            title_font=dict(color='white'),  # texto cor
            xaxis_title_font=dict(color='white'), 
            yaxis_title_font=dict(color='white'),
            xaxis_tickfont=dict(color='white'),  # label
            yaxis_tickfont=dict(color='white'),
        )

        return fig
    else:
        return {}


#Imagem com slider

@callback(
    [Output('frame3_slider', 'max'),
     Output('frame3_slider', 'marks'), 
     Output('frame3_slider', 'value')],
    [Input('pickle_store', 'data'),
     Input('url', 'pathname'),
     Input('command-dropdown_p', 'value')]
)
def update_slider_pixel(pickle_file, pathname, selected_command):
    if pathname == '/pixels' and pickle_file is not None:
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)
        
        if not selected_command:
            selected_command = sys.wavefront_sensors[0].detector.uid if sys.wavefront_sensors else None
        
       
        sensor = next((sensor for sensor in sys.wavefront_sensors if sensor.detector.uid == selected_command), None)
        
        if sensor is None or sensor.detector is None:
            return  0, {}, 0 
        
        img_data = sensor.detector.pixel_intensities.data
        max_frame = img_data.shape[0] - 1
        step = max(1, max_frame // 10)  

        marks = {i: str(i) for i in range(0, max_frame + 1, step)}  
        return max_frame, marks, 0
    else:
        return 0, {}, 0,

"""
estava a tentar bloquear o disabled
@callback(
        Output('dark_feature', 'disabled'),
        Input('pickle_store', 'data'),
        Input('url', 'pathname'),
        Input('command-dropdown_p', 'value')
)
def block_dark(pickle_file, pathname, selected_command):
    disable_checkbox = False
    if pathname == '/pixels' and pickle_file is not None:
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)
        
        if not selected_command:
            selected_command = sys.wavefront_sensors[0].detector.uid if sys.wavefront_sensors else None
        
        sensor = next((sensor for sensor in sys.wavefront_sensors if sensor.detector.uid == selected_command), None)
        
        if sensor is None or sensor.detector is None:
           disable_checkbox = False

        return disable_checkbox"""


#com slide
@callback(
    Output('teste_imagem_diferente', 'figure'),
    [Input('frame3_slider', 'value'),
     Input('pickle_store', 'data'),
     Input('url', 'pathname'),
     Input('aotpy_scale', 'value'),
     Input('aotpy_color', 'value'),
     Input('aotpy_interval', 'value'),
     Input('imag2D', 'clickData'),
     Input('command-dropdown_p', 'value'),
     Input('dark_feature', 'value'),
     Input('sky_feature', 'value'),
     Input('field_feature', 'value')]  
)
def display_detector_frame(slider_value, pickle_file, pathname, scale_type, color_type,interval_type, clickData, selected_command, dark, sky, field):
  
    if pathname == '/pixels' and pickle_file is not None:
        ctx = dash.callback_context
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        if not selected_command:
            selected_command = sys.wavefront_sensors[0].detector.uid if sys.wavefront_sensors else None
        
        sensor = next((sensor for sensor in sys.wavefront_sensors if sensor.detector.uid == selected_command), None)
        
        if sensor is None or sensor.detector is None:
            return  {}

        img_data = sensor.detector.pixel_intensities.data

        if dark and sensor.detector.dark is not None:
            img_data = img_data - sensor.detector.dark.data
        
        if sky and sensor.detector.sky_background is not None:
            img_data = img_data - sensor.detector.sky_background.data  

        if field and sensor.detector.flat_field is not None:
            img_data = img_data - sensor.detector.flat_field.data  
        
        frame_index = slider_value
        
        if ctx.triggered and ctx.triggered[0]['prop_id'].split('.')[0] == 'imag2D':
                x, y, z = extract_coordinates(clickData)
                frame_index = int(x)
       
        frame_processed = img_data[frame_index]
        frame_processed = apply_interval(frame_processed, interval_type)
        frame_processed = apply_scale(frame_processed, scale_type)
        
        colormap = apply_colormap(color_type)

        new_figure = px.imshow(frame_processed, color_continuous_scale=colormap)
        print(f"{colormap}")
        new_figure.update_layout(
                title=f'Frame: {frame_index} of detector {selected_command} ',
                xaxis_title='X',
                yaxis_title='Y',
                autosize=False,
                width=600,
                height=450,
                paper_bgcolor='rgba(0,0,0,0)', 
                title_font=dict(color='white'),  
                xaxis_title_font=dict(color='white'),  
                yaxis_title_font=dict(color='white'),
                xaxis_tickfont=dict(color='white'),  
                yaxis_tickfont=dict(color='white'),
                margin=dict(l=65, r=50, b=65, t=90),
                coloraxis_colorbar=dict(tickfont=dict(color='white')), 
            )
        return new_figure
    else:
        return {}

#Gráfico com intensidade

@callback(
    Output('lineplot', 'figure'),
    [Input('pickle_store', 'data'),
     Input('url', 'pathname'),
     Input('teste_imagem_diferente', 'clickData'),
     Input('imag2D', 'clickData'),
     Input('command-dropdown_p', 'value')]
)
def display_detector_frame(pickle_file, pathname, clickData, second_clickData, selected_command):
    if pathname == '/pixels' and pickle_file is not None:
        ctx = dash.callback_context
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        if not selected_command:
            selected_command = sys.wavefront_sensors[0].detector.uid if sys.wavefront_sensors else None
        
        sensor = next((sensor for sensor in sys.wavefront_sensors if sensor.detector.uid == selected_command), None)
        
        if sensor is None or sensor.detector is None:
            return {}

        pixel_data = sensor.detector.pixel_intensities.data

        pixel_data_mean = np.mean(pixel_data, axis=(1, 2))

        time_values = list(range(len(pixel_data_mean)))
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=time_values, y=pixel_data_mean, mode='lines', name='Mean Intensity of detector', line=dict(dash='dash')))

        trigger_id = ctx.triggered[0]['prop_id'].split('.')[0] if ctx.triggered else None
        time_values_1, time_values_2, pixel_intensity_over_time_1, pixel_intensity_over_time_2, x_1, y_1, x_2,y_2 = [None] *8

        if trigger_id == 'teste_imagem_diferente':
           
            x_1, y_1, z_1 = extract_coordinates(clickData)
            
            pixel_intensity_over_time_1 = pixel_data[:, int(y_1), int(x_1)]

            time_values_1 = list(range(len(pixel_intensity_over_time_1)))

        """if trigger_id == 'imag2D':
           
            x_2, y_2, z_2 = extract_coordinates(second_clickData)
            print(f"X2: {x_2}, Y2: {y_2}")
            pixel_intensity_over_time_2 = pixel_data[:, int(y_2), int(x_2)]
            print(f"pixel_intensity_over_time_2: {pixel_intensity_over_time_2}")
            time_values_2 = list(range(len(pixel_intensity_over_time_2)))
            print(f"Time values 2: {time_values_2}")"""
       
        print(f"it triggers {trigger_id}")
        fig.add_trace(go.Scatter(x=time_values_1, y=pixel_intensity_over_time_1, mode='lines', name = f'Pixel Intensity of x={x_1}, y={y_1}'))
        fig.add_trace(go.Scatter(x=time_values_2, y=pixel_intensity_over_time_2, mode='lines', name= f'Pixel Intensity of x={x_2}, y={y_2}'))
            
        fig.update_layout(
            title='Intensity per pixel per frame',
            xaxis_title='Frame',
            yaxis_title='Intensity',
            autosize=False,
            width=600,
            height=350,
            margin=dict(l=65, r=50, b=65, t=90),
            plot_bgcolor='rgba(36,51,67,1)',
            paper_bgcolor='rgba(0,0,0,0)', 
            title_font=dict(color='white'),
            xaxis_title_font=dict(color='white'), 
            yaxis_title_font=dict(color='white'),
            xaxis_tickfont=dict(color='white'),
            yaxis_tickfont=dict(color='white'),
            showlegend=True,
            legend=dict(
            font=dict(
                color="white"
            )
        )
        
        )
        return fig
    else:
        return {}
            
            

@callback(
    Output('stat_max_p', 'children'),
    Output('stat_min_p', 'children'),
    Output('stat_aver_p', 'children'),
    [Input('pickle_store', 'data'),
     Input('url', 'pathname'),
     Input('command-dropdown_p', 'value')]
)
def display_stats_p(pickle_file, pathname, selected_command):
    if pathname == '/pixels' and pickle_file is not None:
       
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)
        
        if not selected_command:
            selected_command = sys.wavefront_sensors[0].detector.uid if sys.wavefront_sensors else None
        
        sensor = next((sensor for sensor in sys.wavefront_sensors if sensor.detector.uid == selected_command), None)
        
        if sensor is None or sensor.detector is None:
            return  ["None"] *3 
        
        pixel_data = sensor.detector.pixel_intensities.data
    
        max_value = np.max(pixel_data)
        min_value = np.min(pixel_data)
        average = np.mean(pixel_data)

        return f'{max_value:.5f}', f'{min_value:.5f}', f'{average:.5f}'
    else:
        return ["None"] *3
    
    
@callback(
    Output('stat_max_p_spe', 'children'),
    Output('stat_min_p_spe', 'children'),
    Output('stat_aver_p_spe', 'children'),
    [Input('pickle_store', 'data'),
     Input('url', 'pathname'),
     Input('teste_imagem_diferente', 'clickData'),
     Input('command-dropdown_p', 'value')]
)
def display_stats_p_spe(pickle_file, pathname, clickData, selected_command):
    if pathname == '/pixels' and pickle_file is not None:
        ctx = dash.callback_context
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)
        
        if not selected_command:
            selected_command = sys.wavefront_sensors[0].detector.uid if sys.wavefront_sensors else None
        
        sensor = next((sensor for sensor in sys.wavefront_sensors if sensor.detector.uid == selected_command), None)
        
        if sensor is None or sensor.detector is None:
            return  ["None"] *3 
        
        pixel_data = sensor.detector.pixel_intensities.data
        pixel_intensity_over_time =0

        trigger_id = ctx.triggered[0]['prop_id'].split('.')[0] if ctx.triggered else None

        if trigger_id == 'teste_imagem_diferente':
            x, y, z = extract_coordinates(clickData)

            pixel_intensity_over_time= pixel_data[:, int(y), int(x)]
    
        max_value = np.max(pixel_intensity_over_time)
        min_value = np.min(pixel_intensity_over_time)
        average = np.mean(pixel_intensity_over_time)

        return f'{max_value:.5f}', f'{min_value:.5f}', f'{average:.5f}'
    else:
        return ["None"] *3
