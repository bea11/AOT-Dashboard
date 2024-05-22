import dash
from dash import Dash, dcc, html, dash_table, Input, Output, State, callback, register_page
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import base64
import datetime
import io
import aotpy
import gzip
from dash.html import Img
import pickle
from flask import session
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd
import numpy as np


dash.register_page(__name__, path='/measurements')

option_STYLE = {
    'width': '100%',
    'background-color': '#1C2634',
    'color': 'white',
    'cursor': 'pointer',
    'border': '1px solid #243343',
}


layout = html.Div([
    html.H1("Measurements", style={'text-align': 'left', 'margin-left': '12vw', 'marginBottom' : '0px'}),

#Buttons
    html.Div([
    html.Button('Properties', id='button-3', n_clicks=0, style={'background-color': '#1C2634', 'color': 'white', 'text-align': 'center'},),
    html.Button('Statistics', id='button-4', n_clicks=0, style={'background-color': '#1C2634', 'color': 'white', 'text-align': 'center'},),
    dcc.Store(id='store3'),
    html.Div(id='output3')

], style={'position': 'absolute', 'left': '90px','display': 'flex', 'justify-content': 'space-between', 'top': '50px', 'width': '20px', 'height': '25px'}),
  

     #1 quadrante
    dcc.Store(id='1-quadrante-content2', data=[
        html.Div([
            
            html.Div([
                html.Label("Name of sensor: ", style={'color': 'white'}),
                html.Div([], style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),
    
            html.Div([
                html.Label("Shutter Type: ", style={'color': 'white'}),
                html.Div([], style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

            html.Div([
                html.Label("String: ", style={'color': 'white'}),
                html.Div([], style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),
     
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
                html.Div(id='valid-subapertures-container', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

            html.Div([
                html.Label("Subapertures Size: ", style={'color': 'white'}),
               # html.Div(id='s_s'),
                #style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

            html.Div([
                html.Label("Altitudes: ", style={'color': 'white'}),
                html.Div([], style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),
   
            html.Div([
                html.Label("Wavelength: ", style={'color': 'white'}),
                html.Div(id='[]', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),


], style={'background-color': '#1C2634', 'color': 'white', 'position': 'absolute', 'left': '0px', 'top': '30px', 'width': '400px', 'height': '370px'}),
    
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



    ], style={'background-color': '#1C2634', 'color': 'white', 'position': 'absolute', 'left': '310px', 'top': '30px', 'width': '250px', 'height': '370px'}),
]),

#5quadrante
    dcc.Store(id='5-quadrante-content2', data=[
    
        html.Div([
        html.P("Statistics", style={'text-align': 'left','margin-left': '1vw'}),
        html.P("For the Image: ", style={'color': 'white', 'text-decoration': 'underline', 'text-decoration-color': '#C17FEF'}),
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
    'width': '620px', 
    'height': '370px',
}),
]),




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
       # html.Div(id='image', style={'position': 'absolute', 'left': '160px', 'top': '50px', 'width': '600px', 'height': '420px'}),
        dcc.Graph(id='teste_meas', style={'position': 'absolute', 'left': '20px', 'top': '50px'}),
            #dcc.Graph(id='measnovo', style={'position': 'absolute', 'left': '10px', 'top': '50px'}),
], style={
    'display': 'flex',  
    'justify-content': 'space-between',  
    'background-color': '#1C2634', 
    'position': 'absolute', 
    'left': '610px', 
    'top': '50px', 
    'width': '750px', 
    'height': '420px'
}),
  

  
#3 quadrante ->1 cube
    html.Div([
        html.Div([
            html.Div([  
                dcc.Graph(id='x_dimension_image', style={'position': 'absolute', 'left': '0px', 'top': '5px'}),
                dcc.Graph(id='y_dimension_image', style={'position': 'absolute', 'left': '300px', 'top': '10px'}),
                
    ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'center'}),

]),

], style={
    'background-color': '#1C2634',  # Cor ectangulo
    'position': 'absolute',
    'left': '90px',
    'top': '480px',
    'width': '700px',  
    'height': '350px'  
}),
 #'left': '160px', 'top': '80px', 'width': '400px', 'height': '390px'
    #4 quadrante
    html.Div([
        html.P("Graphics", style={'text-align': 'left','margin-left': '1vw'}),
        #html.Div([
         #   dcc.Graph(id='fig_x', style={'position': 'absolute', 'left': '0px', 'top': '5px'}),
         #   dcc.Graph(id='fig_y', style={'position': 'absolute', 'left': '300px', 'top': '10px'}),
        #], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'center'}),
], style={
    'background-color': '#1C2634',  # Cor rectangulo
    'position': 'absolute',
    'left': '700px',
    'top': '480px',
    'width': '600px',  
    'height': '250px'  
}),
    dcc.Store(id='pickle_store', storage_type='local'),
    html.Div(id='output-atmosphere-params'),
    #html.Div(id='s_s'),
], style={'position': 'relative'})

 #Funções
#WAVEFRONT SENSORS
def wavefront_sensors_to_dict(wavefront_sensor):
    return {
        'uid': wavefront_sensor.uid,
        'n_valid_subapertures': wavefront_sensor.n_valid_subapertures,
        'subaperture_size': wavefront_sensor.subaperture_size,
        'wavelength': wavefront_sensor.wavelength,
        #'subaperture_mask': wavefront_sensor.subaperture_mask.data,
    }


#Callbacks
"""
#Name of wavefront sensor
@callback(
    Output('meas_sensor_name', 'children'),
    [Input('pickle_store', 'data'),
     Input('url', 'pathname')]
)
def display_sensor1(pickle_file, pathname):
    if pathname == '/measurements' and pickle_file is not None:
       
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        sensors = [wavefront_sensors_to_dict(wavefront_sensor)['uid'] for wavefront_sensor in sys.wavefront_sensors]
        sensor_divs = [html.Div(sensor, id=(sensor if sensor is not None else 'default-id'), className='option', n_clicks=0, style=option_STYLE) for sensor in sensors]
        return sensor_divs
    else:
        return []
    
#Valid subapertures of wavefront sensor  
@callback(
    Output('meas_n_sub', 'children'),
    [Input('pickle_store', 'data'),
    Input('url', 'pathname')]
)
def display_subap(pickle_file, pathname):  
    if pathname == '/measurements' and pickle_file is not None:
       
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        n_subapertures = [wavefront_sensors_to_dict(wavefront_sensor)['n_valid_subapertures'] for wavefront_sensor in sys.wavefront_sensors]
        return f'{n_subapertures}'
    else:
        return "None"
    
#Size subapertures of wavefront sensor
@callback(
    Output('meas_s_s', 'children'),
    [Input('pickle_store', 'data'),
     Input('url', 'pathname')]
)
def display_subapertures(pickle_file, pathname):
    if pathname == '/measurements' and pickle_file is not None:
       
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        size_subapertures = [wavefront_sensors_to_dict(wavefront_sensor)['subaperture_size'] for wavefront_sensor in sys.wavefront_sensors]
        return f'{size_subapertures}'
    else:
        return "None"
    
#Wavelength of wavefront sensor --> posso só usar extrair a variavel a partir do objeto não tenho que passar pelo dicionário
@callback(
    Output('meas_wavelength_container', 'children'),
    [Input('pickle_store', 'data'),
     Input('url', 'pathname')]
)
def display_wavelength(pickle_file, pathname):
    if pathname == '/measurements' and pickle_file is not None:
       
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        wave = [wavefront_sensors_to_dict(wavefront_sensor)['wavelength'] for wavefront_sensor in sys.wavefront_sensors]
        return f'{wave}'
    else:
        return "None" 

"""
#Downsampling.
#Preprocessing: Perform any necessary preprocessing steps normalization, filtering)
"""@callback(
    Output('measnovo', 'figure'),
    [Input('pickle_store', 'data'),
     Input('url', 'pathname')]
)
def display_measurements_data(pickle_file, pathname):
    if pathname == '/measurements' and pickle_file is not None:
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        measurements_data = sys.wavefront_sensors[0].measurements.data
        print(f"Data shape: {measurements_data.shape}, Data type: {type(measurements_data)}")

        # Create a list of figures for each frame
        frames = [px.imshow(frame, binary_string=True).data[0] for frame in measurements_data]

        fig = go.Figure(
            data=frames[0],
            layout=go.Layout(
                title='Different 2D images over frames',
                xaxis_title='Local X',
                yaxis_title='Local Y',
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
                updatemenus=[dict(type='buttons',
                                  showactive=False,
                                  buttons=[dict(label='Play',
                                                method='animate',
                                                args=[None])])]),
            frames=[go.Frame(data=frame) for frame in frames]
        )

        return fig
    else:
        print("Pathname not '/measurements' or pickle_file is None")
        return {}
"""

#Measurements from the sensor over time. Each of its Sv subapertures is able to measure in d dimensions. (Dimensions t×d×Sv, in user defined units, using data type flt)

@callback(
    Output('x_dimension_image', 'figure'),
    Output('y_dimension_image', 'figure'),
    Input('pickle_store', 'data'),
    Input('url', 'pathname')
)
def display_measurements(pickle_file, pathname):
    if pathname == '/measurements' and pickle_file is not None:
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)
      
        measurements = sys.wavefront_sensors[0].measurements.data  

        subaperture_mask = sys.wavefront_sensors[0].subaperture_mask
        #subaperture_mask = [wavefront_sensors_to_dict(wavefront_sensor)['subaperture_mask'] for wavefront_sensor in sys.wavefront_sensors]


        if subaperture_mask is None or subaperture_mask.data is None:
            mask_flattened = None
        else:
            subaperture_mask_data = subaperture_mask.data
            mask_flattened = subaperture_mask_data.flatten()

# Separar
        x_measurements = measurements[:, 0, :]
        y_measurements = measurements[:, 1, :]

#  t x sv
        t, sv = x_measurements.shape

# subaperture mask filter
        if mask_flattened is not None:
            valid_indices = mask_flattened >= 0
            x_processed = x_measurements[:, valid_indices]
            y_processed = y_measurements[:, valid_indices]
        else:
            x_processed = x_measurements
            y_processed = y_measurements

# 
        fig_x = go.Figure(data=go.Heatmap(z=x_processed.T, colorscale='Viridis'))
        fig_y = go.Figure(data=go.Heatmap(z=y_processed.T, colorscale='Viridis'))

        fig_x.update_layout(
            title='X_D Measurements Over Time',
            xaxis_title='Time',
            yaxis_title='Subaperture',
            autosize=False,
            width=400,
            height=300,
            margin=dict(l=65, r=50, b=65, t=90),
            paper_bgcolor='rgba(0,0,0,0)', 
            plot_bgcolor='rgba(0,0,0,0)' , 
            title_font=dict(color='white'),  # texto cor
            xaxis_title_font=dict(color='white'), 
            yaxis_title_font=dict(color='white'),
            xaxis_tickfont=dict(color='white'),  # label
            yaxis_tickfont=dict(color='white'),
        )

        fig_y.update_layout(
            title='Y_D Measurements Over Time',
            xaxis_title='Time',
            yaxis_title='Subaperture',
            autosize=False,
            width=400,
            height=300,
            margin=dict(l=65, r=50, b=65, t=90),
            paper_bgcolor='rgba(0,0,0,0)',  
            plot_bgcolor='rgba(0,0,0,0)',  
            title_font=dict(color='white'),  # texto cor
            xaxis_title_font=dict(color='white'), 
            yaxis_title_font=dict(color='white'),
            xaxis_tickfont=dict(color='white'),  # label
            yaxis_tickfont=dict(color='white'),
        )

        return fig_x, fig_y
    else:
        return {}, {}
"""   
@callback(
    Output('teste_meas', 'figure'),
    [Input('pickle_store', 'data'),
     Input('url', 'pathname')]
)
def display_imgs_data(pickle_file, pathname):
    if pathname == '/measurements' and pickle_file is not None:
    
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        img_data = sys.wavefront_sensors[0].measurements.data 
        half_frames = img_data.shape[0] // 2
        img_data = img_data[:half_frames]
        print(f"Data MEASUREMENT shape: {img_data.shape}, Data type: {type(img_data)}")

        fig = go.Figure(
            data=[go.Heatmap(z=img_data[0], colorscale='Viridis')],
            layout=go.Layout(
                title='Different 2D images over frames',
                xaxis_title='Local X',
                yaxis_title='Local Y',
                autosize=False,
                width=700,
                height=650,
                paper_bgcolor='rgba(0,0,0,0)', 
                title_font=dict(color='white'),  
                xaxis_title_font=dict(color='white'),  
                yaxis_title_font=dict(color='white'),
                xaxis_tickfont=dict(color='white'),  
                yaxis_tickfont=dict(color='white'),
                coloraxis_showscale=False, 
                margin=dict(l=65, r=50, b=65, t=90),
                updatemenus=[dict(
                    type="buttons",
                    showactive=False,
                    buttons=[dict(label="Play",
                                  method="animate",
                                  args=[None, {"frame": {"duration": 500, "redraw": False},
                                               "fromcurrent": True,
                                               "transition": {"duration": 300, "easing": "quadratic-in-out"}}])]
                )]
            ),
            frames=[go.Frame(data=[go.Heatmap(z=img_data[i])]) for i in range(half_frames)]
        )

        return fig
    else:
        return {}    """

"""@callback(
    Output('fig_x', 'figure'),
    Output('fig_y', 'figure'),
    Input('pickle_store', 'data'),
    Input('url', 'pathname')
)
def display_measurements(pickle_file, pathname):
    if pathname == '/measurements' and pickle_file is not None:
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)
      
        measurements = sys.wavefront_sensors[0].measurements.data  

        subaperture_mask = sys.wavefront_sensors[0].subaperture_mask

        if subaperture_mask is None or subaperture_mask.data is None:
            mask_flattened = None
        else:
            subaperture_mask_data = subaperture_mask.data
            mask_flattened = subaperture_mask_data.flatten()

        x_measurements = measurements[:, 0, :]
        y_measurements = measurements[:, 1, :]

        t, sv = x_measurements.shape

        if mask_flattened is not None:
            valid_indices = mask_flattened >= 0
            x_processed = x_measurements[:, valid_indices]
            y_processed = y_measurements[:, valid_indices]
        else:
            x_processed = x_measurements
            y_processed = y_measurements

        fig_x = go.Figure()
        fig_y = go.Figure()

        for i in range(t):
            fig_x.add_trace(go.Heatmap(z=x_processed[i, :].T, colorscale='Viridis', visible=(i==0)))
            fig_y.add_trace(go.Heatmap(z=y_processed[i, :].T, colorscale='Viridis', visible=(i==0)))

        steps_x = []
        steps_y = []
        for i in range(t):
            step_x = dict(
                method="update",
                args=[{"visible": [(el==i) for el in range(t)]}],
            )
            step_y = dict(
                method="update",
                args=[{"visible": [(el==i) for el in range(t)]}],
            )
            steps_x.append(step_x)
            steps_y.append(step_y)

        sliders_x = [dict(
            active=0,
            currentvalue={"prefix": "Time: "},
            pad={"t": t},
            steps=steps_x
        )]

        sliders_y = [dict(
            active=0,
            currentvalue={"prefix": "Time: "},
            pad={"t": t},
            steps=steps_y
        )]

        fig_x.update_layout(sliders=sliders_x)
        fig_y.update_layout(sliders=sliders_y)

        return fig_x, fig_y
    else:
        return {}, {}"""



@callback(
    Output('teste_meas', 'figure'),
    [Input('pickle_store', 'data'),
     Input('url', 'pathname')]
)
def display_imgs_data(pickle_file, pathname):
    if pathname == '/measurements' and pickle_file is not None:
    
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        img_data = sys.wavefront_sensors[0].measurements.data
        half_frames = img_data.shape[0] // 2
        img_data = img_data[:half_frames]

        print(f"Data MEASUREMENT shape: {img_data.shape}, Data type: {type(img_data)}")
 
        fig = px.imshow(img_data, animation_frame=0, binary_string=True, labels=dict(animation_frame="slice"))
        fig.update_layout(
            title='Different 2D images over frames',
            xaxis_title='Local X',
            yaxis_title='Local Y',
            autosize=False,
            width=500,
            height=200,
            paper_bgcolor='rgba(0,0,0,0)', 
            title_font=dict(color='white'),  
            xaxis_title_font=dict(color='white'),  
            yaxis_title_font=dict(color='white'),
            xaxis_tickfont=dict(color='white'),  
            yaxis_tickfont=dict(color='white'),
            coloraxis_showscale=False, 
            margin=dict(l=65, r=50, b=65, t=90),
        )
        return fig
    else:
        return {}

"""

@callback(
    Output('stat_max', 'children'),
    Output('stat_min', 'children'),
    Output('stat_aver', 'children'),
    [Input('pickle_store', 'data'),
     Input('url', 'pathname')]
)
def display_wavelength(pickle_file, pathname):
    if pathname == '/measurements' and pickle_file is not None:
       
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        meas_data = sys.wavefront_sensors[0].measurements.data
    
        max_value = np.max(meas_data)
        min_value = np.min(meas_data)
        average = np.mean(meas_data)

        return f'{max_value}', f'{min_value}', f'{average}'
    else:
        return "None"
"""
"""@callback(
    Output('meas1D', 'figure'),
    [Input('pickle_store', 'data'),
     Input('url', 'pathname')]
)
def display_meas_frame(pickle_file, pathname):
    if pathname == '/measurements' and pickle_file is not None:

        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        meas_data = sys.wavefront_sensors[0].measurements

        if hasattr(meas_data, 'data'):
            meas_data = meas_data.data

        
            reshaped = meas_data.reshape(meas_data.shape[0], -1)

        fig = go.Figure(data=go.Heatmap(z=reshaped, colorscale='Viridis'))

        fig.update_layout(
            title='Measurements over time',
            xaxis_title='Subaperture',
            yaxis_title='Y',
            autosize=False,
            width=600,
            height=320,
            margin=dict(l=65, r=50, b=65, t=90),
            paper_bgcolor='rgba(0,0,0,0)', 
            title_font=dict(color='white'),  # text color
            xaxis_title_font=dict(color='white'), 
            yaxis_title_font=dict(color='white'),
            xaxis_tickfont=dict(color='white'),  # label
            yaxis_tickfont=dict(color='white'),
            )

        return fig
    else:
        return {}





"""

@callback(
    Output('store3', 'data'),
    [Input('button-3', 'n_clicks'), Input('button-4', 'n_clicks')],
    [dash.dependencies.State('store3', 'data')]
)
def update_store3(n3, n4, data):
    ctx = dash.callback_context
    if not ctx.triggered:
        button_id = 'No clicks yet'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    return button_id

@callback(
    Output('output3', 'children'),
    [Input('button-3', 'n_clicks_timestamp'), Input('button-4', 'n_clicks_timestamp')],
    [State('1-quadrante-content2', 'data'), State('5-quadrante-content2', 'data')]
)
def update_output3(n_clicks_timestamp3, n_clicks_timestamp4, content3, content4):
    if n_clicks_timestamp3 is None and n_clicks_timestamp4 is None:
        return content3
    if n_clicks_timestamp3 is None:
        n_clicks_timestamp3 = 0
    if n_clicks_timestamp4 is None:
        n_clicks_timestamp4 = 0

    if n_clicks_timestamp3 > n_clicks_timestamp4:
        return content3
    else:
        return content4
