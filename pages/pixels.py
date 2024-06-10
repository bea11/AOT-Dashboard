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



dash.register_page(__name__, path='/pixels', suppress_callback_exceptions=True)

option_STYLE = {
    'width': '100%',
    'background-color': '#1C2634',
    'color': 'white',
    'cursor': 'pointer',
    'border': '1px solid #243343',
}

layout = html.Div([


    html.H1("Pixels", style={'text-align': 'left', 'margin-left': '8vw', 'marginBottom' : '0px'}),
    html.Div([
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
            'margin-left': '25vw',
            'display': 'flex',  
            'position': 'absolute', 
            #'left': '830px', 
            #'top': '50px',
        }
    ),
]),
#Buttons
    html.Div([
    html.Button('Properties', id='button-1', n_clicks=0, style={'background-color': '#1C2634', 'color': 'white', 'text-align': 'center'},),
    html.Button('Statistics', id='button-2', n_clicks=0, style={'background-color': '#1C2634', 'color': 'white', 'text-align': 'center'},),
    dcc.Store(id='store_data'),
    html.Div(id='output_data')

], style={'position': 'absolute', 'left': '90px','display': 'flex', 'justify-content': 'space-between', 'top': '50px', 'width': '20px', 'height': '25px'}),
  
  
   #1 quadrante
    dcc.Store(id='1-quadrante-content', data=[
        html.Div([
            html.P("Properties", style={'text-align': 'left', 'margin-left': '1vw'}),
           
            html.Div([
                html.Label("Name of Detector: ", style={'color': 'white'}),
                html.Div(id='name_ns', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),
    
            html.Div([
                html.Label("Shutter Type: ", style={'color': 'white'}),
                html.Div(id='shuttert', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

            html.Div([
                html.Label("Subeapertures Size: ", style={'color': 'white'}),
                html.Div(id='ss', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),
     
            html.Div([
                html.Label("Mask Ofset: ", style={'color': 'white'}),
                html.Div(id='mo', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

            html.Div([
                html.Label("Frame Rate: ", style={'color': 'white'}),
                html.Div(id='frame_rate', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

            html.Div([
                html.Label("Gain: ", style={'color': 'white'}),
                html.Div(id='gain', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

            html.Div([
                html.Label("Integration Time: ", style={'color': 'white'}),
                html.Div(id='integration_time', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

            html.Div([
                html.Label("Pixel Scale: ", style={'color': 'white'}),
                html.Div(id='pixel_scale', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),
   
            html.Div([
                html.Label("Quantum Efficiency: ", style={'color': 'white'}),
                html.Div(id='quantum_efficiency', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

            html.Div([
                html.Label("Readout Noise: ", style={'color': 'white'}),
                html.Div(id='readout_noise', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

            html.Div([
                html.Label("Readout Rate: ", style={'color': 'white'}),
                html.Div(id='readout_rate', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

            html.Div([
                html.Label("Sampling Technique: ", style={'color': 'white'}),
                html.Div(id='sampling_technique', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),


], style={'background-color': '#1C2634', 'color': 'white', 'position': 'absolute', 'left': '0px', 'top': '30px', 'width': '400px', 'height': '390px'}),
    
   #1 quadrante 
        html.Div([
            html.P("Objects", style={'text-align': 'left','margin-left': '1vw'}),
  
    #1 bloco
            html.Div([
                html.P("Source", style={'text-align': 'left', 'margin-left': '1vw'}),
                html.Div([
                    html.Label("Name: ", style={'color': 'white'}),
                    html.Button("NGS", style={'border-radius': '10%', 'border': '1.5px solid blue', 'background-color': '#1C2634', 'color':'white','font-size':'15px', 'width': '150px', 'height': '20px', 'margin-left': '10px'})
            ], style={'display': 'flex', 'align-items': 'center', 'margin-left': '1vw'}),
                html.P("Type: Natural Guide Star", style={'text-align': 'left', 'margin-left': '1vw', 'color': 'white'}),
    ], style={'background-color': '#243343', 'color': 'white', 'display': 'flex', 'flex-direction': 'column', 'width':'200px', 'height': '90px','margin-left': '1vw'}),

    #2 bloco
            html.Div([
                html.P("Detector", style={'text-align': 'left', 'margin-left': '1vw'}),
                html.Div([
                    html.Label("Name: ", style={'color': 'white'}),
                    html.Button("SAPHIRA", style={'border-radius': '10%', 'border': '1.5px solid blue', 'background-color': '#1C2634', 'color':'white','font-size':'15px', 'width': '150px', 'height': '20px', 'margin-left': '10px'})
            ], style={'display': 'flex', 'align-items': 'center', 'margin-left': '1vw'}),
                html.P("Type: CMOS", style={'text-align': 'left', 'margin-left': '1vw', 'color': 'white'}),
    ], style={'background-color': '#243343', 'color': 'white', 'display': 'flex', 'flex-direction': 'column', 'width':'200px', 'height': '90px','margin-left': '1vw', 'margin-top': '15px'}),

    #3 bloco
            html.Div([
                html.P("Aberration 1", style={'text-align': 'left', 'margin-left': '1vw'}),
                html.Div([
                    html.Label("Name: ", style={'color': 'white'}),
                    html.Button("Example", style={'border-radius': '10%', 'border': '1.5px solid blue', 'background-color': '#1C2634', 'color':'white','font-size':'15px', 'width': '150px', 'height': '20px', 'margin-left': '10px'})
            ], style={'display': 'flex', 'align-items': 'center', 'margin-left': '1vw'}),
                html.P("Type: Other", style={'text-align': 'left', 'margin-left': '1vw', 'color': 'white'}),
    ], style={'background-color': '#243343', 'color': 'white', 'display': 'flex', 'flex-direction': 'column', 'width':'200px', 'height': '90px','margin-left': '1vw', 'margin-top': '15px'}),



    ], style={'background-color': '#1C2634', 'color': 'white', 'position': 'absolute', 'left': '310px', 'top': '30px', 'width': '280px', 'height': '470px'}),
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
    style={'width': "10vw",'color': 'white', 'height':'35px' }
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
        style={'width': "10vw",'color': 'white', 'height':'35px' }
    ),
        dbc.Select(
        id="aotpy_interval",
            options=[
                {'label': 'Interval', 'value': 'loops'},
                {'label': 'D0', 'value': 'C0'},
                {'label': 'D1', 'value': 'C1'},
                {'label': 'D2', 'value': 'C2'}
        ],
        value='loops',
        className='custom-select',
        style={'width': "10vw",'color': 'white', 'height':'35px' }
    ),
    dcc.Graph(id='teste_imagem_diferente', style={'position': 'absolute', 'left': '20px', 'top': '50px', 'height': '330px', 'width': '500px'}),
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
                        'top': '370px',  
                    }),

        html.Div([  
            html.Label([
            "flat_field",
            dbc.Checkbox(id='checkbox-1', className='custom-checkbox')
    ], style={'display': 'flex', 'align-items': 'center'}),
    
            html.Label([
            "dark",
            dbc.Checkbox(id='dark_feature', className='custom-checkbox')
    ], style={'display': 'flex', 'align-items': 'center'}),
    
            html.Label([
            "sky_background",
            dbc.Checkbox(id='checkbox-3', className='custom-checkbox')
    ], style={'display': 'flex', 'align-items': 'center'})

], style={'display': 'flex', 'justify-content': 'space-between', 'position': 'absolute', 'bottom': '0', 'width': '100%'}),

], style={
    'display': 'flex',  
    'justify-content': 'space-between',  
    'background-color': '#1C2634', 
    'position': 'absolute', 
    'left': '700px', 
    'top': '50px', 
    'width': '600px', 
    'height': '520px'
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
    'left': '90px',
    'top': '580px',
    'width': '590px',  
    'height': '350px'  
}),
 #'left': '160px', 'top': '80px', 'width': '400px', 'height': '390px'
 
    #4 quadrante
        html.Div([
            html.Div([  
                dcc.Graph(id='lineplot',style={'position': 'absolute', 'left': '20px', 'top': '0px', 'height': '330px', 'width': '500px'}),
       
    ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'center'}),
       

], style={
    'background-color': '#1C2634',  # Cor rectangulo
    'position': 'absolute',
    'left': '700px',
    'top': '580px',
    'width': '590px',  
    'height': '350px'  
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
                html.Div(id='stat_aver_p', style={'background-color': '#243343', 'width': '180px', 'height': '20px', 'margin-left': '10px'}),
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

        html.P("For the Queue: ", style={'color': 'white', 'text-decoration': 'underline', 'text-decoration-color': '#C17FEF'}),
            html.Div([
                html.Label("Maximum value: ", style={'color': 'white'}),
                html.Div([], style={'background-color': '#243343', 'width': '60px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

            html.Div([
                html.Label("Minimum value: ", style={'color': 'white'}),
                html.Div([], style={'background-color': '#243343', 'width': '60px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

            html.Div([
                html.Label("Average values: ", style={'color': 'white'}),
                html.Div([], style={'background-color': '#243343', 'width': '60px', 'height': '20px', 'margin-left': '10px'}),
                html.Div([], style={'background-color': '#243343', 'width': '60px', 'height': '20px', 'margin-left': '10px'}),
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

], style={
    'background-color': '#1C2634', 
    'position': 'absolute',
    'left': '0px',
    'top': '30px',
    'width': '650px',  
    'height': '390px',  
}),
]),

    #html.Div(id='img_data'),
    dcc.Store(id='pickle_store', storage_type='local'),
    html.Div(id='output-atmosphere-params'),
    dcc.Store(id='teste_imagem'),
    
    #dcc.Graph(id='img_imagem', style={'width': '33%', 'display': 'inline-block'}),


    #dcc.Dropdown(id='slice-selector', options=[], placeholder="Select Pixel Slice"),
    #dcc.Graph(id='selected_slice', style={'width': '33%', 'display': 'inline-block'}),
   
    
    #dcc.Graph(id='imag2D', style={'width': '33%', 'display': 'inline-block'}),
    #dcc.Slider(id='frameindex', min=0, max=100, step=1, value=0, marks={0: '0', 100: '100'}),


   # html.Div(id='mo', style={'color': 'red'}),
    #html.Div(id='sm', style={'color': 'blue'}),
    #html.Div(id='ss', style={'color': 'black'}),

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
        return np.log1p(image)  # log(1 + imagem)
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
        #conta histograma
        img_array = np.array(image)

        histogram, bins = np.histogram(img_array.flatten(), bins=256, density=True)
        cdf = histogram.cumsum()  # função distribuição cumulativa
        cdf = 255 * cdf / cdf[-1]  # normalizar

    # interpolação linear
        image_equalized = np.interp(img_array.flatten(), bins[:-1], cdf)
        return image_equalized.reshape(img_array.shape)
    elif scale_type == 'Log Exponent':
        return np.exp(image)
    else:
        raise ValueError(f'Invalid scale: {scale_type}')

def apply_colormap(colormap):
    if colormap == 'Standard':
        return None #normal
    elif colormap == 'Grey':
        return 'greys'
    elif colormap == 'Red':
        return 'reds'
    elif colormap == 'Green':
        return 'greens'
    elif colormap == 'Blue':
        return 'blues'
    elif colormap == 'Heat':
        return 'hot'
    elif colormap == 'Rainbow':
        return 'rainbow'
    else:
        raise ValueError(f'Invalid colormap {colormap}')
    
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
    [Input('url', 'pathname')],
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
    Output('sampling_technique', 'children'),],
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
        
        # Corrected: Iterating through sys.wavefront_sensors to find the matching sensor
        sensor = next((sensor for sensor in sys.wavefront_sensors if sensor.detector.uid == selected_command), None)
        
        if sensor is None or sensor.detector is None:
            return ["None"] * 2 
        
        #sm = sys.wavefront_sensors[0].subaperture_mask.name if sys.wavefront_sensors[0].subaperture_mask else None
        mo = sensor.mask_offsets
        ss = sensor.subaperture_size

         #Assim mostra o None
        mo, ss = none_to_string( mo, ss)  
        print(f" Mask offsets: {mo}, Subaperture size: {ss}")

        return mo, ss
    else: 
        return ["None"] * 2 


#Imagem estática

@callback(
    Output('imag2D', 'figure'),
    [Input('pickle_store', 'data'),
     Input('url', 'pathname'),
     Input('command-dropdown_p', 'value'),]
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

    
        fig = go.Figure(data=go.Heatmap(z=swapped, colorscale='Viridis'))

        fig.update_layout(
            title='Pixel with frame index',
            xaxis_title='Frame Index',
            yaxis_title='Pixel',
            autosize=False,
            width=600,
            height=350,
            margin=dict(l=65, r=50, b=65, t=90),
            #plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)', 
            title_font=dict(color='white'),  # texto cor
            xaxis_title_font=dict(color='white'), 
            yaxis_title_font=dict(color='white'),
            xaxis_tickfont=dict(color='white'),  # label
            yaxis_tickfont=dict(color='white')
        )

        return fig
    else:
        return {}
"""
@callback(
    Output('img_data', 'children'),
    [Input('second-atmosphere-params', 'data'),
     Input('url', 'pathname')]
)
def display_img_data(data, pathname):
    if pathname == '/pixels' and data is not None:
        img_data = data['np_image_data']
        print(f"received {img_data}")

        # Flatten a lista duas vezes se for uma lista 3D e converter para inteiros
        if isinstance(img_data[0][0], list):
            img_data = [item for sublist1 in img_data for sublist2 in sublist1 for item in sublist2]
        elif isinstance(img_data[0], list):
            img_data = [item for sublist in img_data for item in sublist]
        else:
            img_data = [item for item in img_data]

        # Normalizar entre 0-255
        max_val = max(img_data)
        min_val = min(img_data)
        img_data = [int(255 * (item - min_val) / (max_val - min_val)) for item in img_data]

        # lista inteiros -> bytes
        img_data_bytes = bytes(img_data)

        # encode bytes para base64 -> para passar para cá tive que decode
        encoded_image = base64.b64encode(img_data_bytes).decode('utf-8')

        # html.Img 
        return html.Img(src=f"data:image/jpeg;base64,{encoded_image}", style={'width': '100%'})
    else: []"""

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
        step = max(1, max_frame // 10)  # Example: divide by 10 for more granularity

        marks = {i: str(i) for i in range(0, max_frame + 1, step)}  
        
        return max_frame, marks, 0
    else:
        return 0, {}, 0

#com slide
@callback(
    Output('teste_imagem_diferente', 'figure'),
    [Input('frame3_slider', 'value'),
    Input('pickle_store', 'data'),
     Input('url', 'pathname'),
     Input('aotpy_scale', 'value'),
     Input('aotpy_color', 'value'),
     Input('imag2D', 'clickData'),
     Input('command-dropdown_p', 'value'),
     Input('dark_feature', 'value'),]  
)
def display_detector_frame(slider_value, pickle_file, pathname, scale_type, color_type, clickData, selected_command, dark):
  
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
        
        print(f"Data PIXEL shape: {img_data.shape}, Data type: {type(img_data)}")

        frame_index = slider_value
        
        if ctx.triggered and ctx.triggered[0]['prop_id'].split('.')[0] == 'imag2D':
            # cordenadas do click data 
                x, y, z = extract_coordinates(clickData)
            
            # o x do slider é o frame index (tempo)
                frame_index = int(x)
    
        frame_processed = img_data[frame_index]
        frame_processed = apply_scale(frame_processed, scale_type)

    
        
        colormap = apply_colormap(color_type)
        print(f"Colormap: {colormap}")
        #para mudar a cor uso o continuous_scale mas ainda não está a funcionar
        new_figure = px.imshow(frame_processed, color_continuous_scale=colormap)
        print(f"{colormap}")
        new_figure.update_layout(
            title=f'Different 2D images over frames, {frame_index} ',
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
            coloraxis_showscale=False, 
            margin=dict(l=65, r=50, b=65, t=90),
        )
        return new_figure
    else:
        return {}

#Gráfico com intensidade

@callback(
    Output('lineplot', 'figure'),
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
            return  {}

        pixel_data = sensor.detector.pixel_intensities.data
        

       # media
        pixel_data_mean = np.mean(pixel_data, axis=(1, 2))

        time_values = list(range(len(pixel_data_mean)))

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=time_values, y=pixel_data_mean, mode='lines', name='Mean intensity over time'))
        fig.update_layout(
            title='Intensity over time',
            xaxis_title='Time',
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
            yaxis_tickfont=dict(color='white')
        )

        return fig
    else:
        return {}


"""@callback(
    Output('slice-selector', 'options'),
    Input('pickle_store', 'data'),
    Input('url', 'pathname')
)
def update_slice_selector(pickle_file, pathname):
    if pathname == '/pixels' and pickle_file:
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)
        
     
        num_pixels = sys.wavefront_sensors[0].detector.pixel_intensities.data.shape[1] * sys.wavefront_sensors[0].detector.pixel_intensities.data.shape[2]
        
        options = [{'label': f'Pixel {i}', 'value': i} for i in range(num_pixels)]
        return options
    return []    """





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

        return f'{max_value}', f'{min_value}', f'{average}'
    else:
        return ["None"] *3
