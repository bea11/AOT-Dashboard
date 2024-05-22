import dash
from dash import Dash, dcc, html, dash_table, Input, Output, State, callback, register_page
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import base64
import datetime
import io
import aotpy
import gzip
import pickle
from flask import session

dash.register_page(__name__, path='/commands')

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
option_STYLE = {
    'width': '100%',
    'background-color': '#1C2634',
    'color': 'white',
    'cursor': 'pointer',
    'border': '1px solid #243343',
}


layout = html.Div([
    html.H1("Commands", style={'text-align': 'left', 'margin-left': '12vw', 'marginBottom' : '0px'}),

    html.Div([
    dbc.Select(
        id='command-dropdown',
        options=[
            {'label': 'HODM', 'value': 'CMD1'},
            {'label': 'ITTM', 'value': 'CMD2'},
        ],
        value='CMD1',
        className='custom-select', 
        style={
            'width': "10vw",
            'text-color': 'white',
            'height': '28px',
            'backgroundColor': '#1C2634',
            'margin-left': '12vw',
            'display': 'flex',  
            'position': 'absolute', 
            #'left': '830px', 
            #'top': '50px',
        }
    ),
]),
    

   #1 quadrante
    html.Div([

        html.P("Properties", style={'text-align': 'left', 'margin-left': '1vw'}),
        
    #Strings    
        html.Div([
            html.Label("Name of sensor: ", style={'color': 'white'}),
            html.Div(id='sensor_name', style={'background-color': '#243343', 'width': '160px', 'height': '18px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),
    
        html.Div([
            html.Label("Shutter Type: ", style={'color': 'white'}),
            html.Div([], style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

        html.Div([
            html.Label("String: ", style={'color': 'white'}),
            html.Div([], style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),
     
    #Integers
        html.Div([
            html.Label("Unique Identifier: ", style={'color': 'white'}),
            html.Div([], style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px', 'margin-top': '13px'}),

        html.Div([
            html.Label("Integer: ", style={'color': 'white'}),
            html.Div([], style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

        html.Div([
            html.Label("Number of valid subapertures: ", style={'color': 'white'}),
            html.Div(id='n_sub', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

    #Floats
        html.Div([
            html.Label("Subapertures Size: ", style={'color': 'white'}),
            html.Div(id='s_s', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

        html.Div([
            html.Label("Altitudes: ", style={'color': 'white'}),
            html.Div([], style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),
   
        html.Div([
            html.Label("Wavelength: ", style={'color': 'white'}),
            html.Div(id='wavelength_d', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),


    ], style={'background-color': '#1C2634', 'color': 'white', 'position': 'absolute', 'left': '160px', 'top': '85px', 'width': '400px', 'height': '390px'}),
    
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



    ], style={'background-color': '#1C2634', 'color': 'white', 'position': 'absolute', 'left': '580px', 'top': '85px', 'width': '230px', 'height': '390px'}),

    #2 quadrante 
    #imagem
    html.Div([
    dbc.Select(
        id="aotpy_scale",
        options=[
            {'label': 'Scale', 'value': 'loops'},
            {'label': 'C0', 'value': 'C0'},
            {'label': 'C1', 'value': 'C1'},
            {'label': 'C2', 'value': 'C2'}
        ],
        value='loops',
        className='custom-select',
        style={'width': "10vw",'color': 'white', 'height':'35px' }
    ),
    dbc.Select(
        id="aotpy_color",
        options=[
            {'label': 'Color', 'value': 'loops'},
            {'label': 'C0', 'value': 'C0'},
            {'label': 'C1', 'value': 'C1'},
            {'label': 'C2', 'value': 'C2'}
        ],
        value='loops',
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


], style={
    'display': 'flex',  
    'justify-content': 'space-between',  
    'background-color': '#1C2634', 
    'position': 'absolute', 
    'left': '830px', 
    'top': '50px', 
    'width': '480px', 
    'height': '420px'
}),
  
  #3 quadrante
  html.Div([
    html.P("Data", style={'text-align': 'left','margin-left': '1vw'}),
    html.Div([  
        html.Div(  
            style={
                'background-color': 'grey',
                'width': '300px',  
                'height': '200px'  
            }
        ),
        html.Div('Seconds', style={'color': 'white'}),  # x
    ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'center'}),
    html.Div('Actuator index', style={'color': 'white', 'position': 'absolute', 'top': '50%', 'left': '0'})  # y
], style={
    'background-color': '#1C2634',  
    'position': 'absolute',
    'left': '160px',
    'top': '480px',
    'width': '600px',  
    'height': '300px'  
}),
 #'left': '160px', 'top': '80px', 'width': '400px', 'height': '390px'
 
    #4 quadrante
    html.Div([
    html.P("Graphics", style={'text-align': 'left','margin-left': '1vw'}),
    html.Div([  
        html.Div(  
            style={
                'background-color': '#243343',
                'width': '500px',  
                'height': '200px'  
            }
        ),
        html.Div('Time', style={'color': 'white'}),  # x
    ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'center'}),
    html.Div('AAA', style={'color': 'white', 'position': 'absolute', 'top': '50%', 'left': '0'})  # y
], style={
    'background-color': '#1C2634',  # Cor rectangulo
    'position': 'absolute',
    'left': '780px',
    'top': '480px',
    'width': '600px',  
    'height': '300px'  
}),
        dcc.Store(id='pickle_store', storage_type='local'),

], style={'position': 'relative'})
    
 #Funções
#WAVEFRONT SENSORS
def wavefront_sensors_to_dict(wavefront_sensor):
    return {
        'uid': wavefront_sensor.uid,
        'n_valid_subapertures': wavefront_sensor.n_valid_subapertures,
        'subaperture_size': wavefront_sensor.subaperture_size,
        'wavelength': wavefront_sensor.wavelength,
    }

#Callbacks

#Name of wavefront sensor
@callback(
    Output('sensor_name', 'children'),
    [Input('pickle_store', 'data'),
     Input('url', 'pathname')]
)
def display_sensor1(pickle_file, pathname):
    if pathname == '/commands' and pickle_file is not None:
  
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        sensors = [wavefront_sensors_to_dict(wavefront_sensor)['uid'] for wavefront_sensor in sys.wavefront_sensors]
        sensor_divs = [html.Div(sensor, id=(sensor if sensor is not None else 'default-id'), className='option', n_clicks=0, style=option_STYLE) for sensor in sensors]
        return sensor_divs
    else:
        return []
    
#Valid subapertures  
@callback(
    Output('n_sub', 'children'),
    [Input('pickle_store', 'data'),
    Input('url', 'pathname')]
)
def display_subap(pickle_file, pathname):  
    if pathname == '/commands' and pickle_file is not None:
       
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        n_subapertures = [wavefront_sensors_to_dict(wavefront_sensor)['n_valid_subapertures'] for wavefront_sensor in sys.wavefront_sensors]
        return f'{n_subapertures}'
    else:
        return "None"
    
#Size subapertures 
@callback(
    Output('s_s', 'children'),
    [Input('pickle_store', 'data'),
     Input('url', 'pathname')]
)
def display_subapertures(pickle_file, pathname):
    if pathname == '/commands' and pickle_file is not None:
      
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        size_subapertures = [wavefront_sensors_to_dict(wavefront_sensor)['subaperture_size'] for wavefront_sensor in sys.wavefront_sensors]
        return f'{size_subapertures}'
    else:
        return "None"
    
#Wavelength
@callback(
    Output('wavelength_d', 'children'),
    [Input('pickle_store', 'data'),
     Input('url', 'pathname')]
)
def display_wavelength(pickle_file, pathname):
    if pathname == '/commands' and pickle_file is not None:
       
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        wave = [wavefront_sensors_to_dict(wavefront_sensor)['wavelength'] for wavefront_sensor in sys.wavefront_sensors]
        return f'{wave}'
    else:
        return "None"