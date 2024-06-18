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
from astropy.visualization import MinMaxInterval, ZScaleInterval, PercentileInterval


dash.register_page(__name__, path='/measurements', supress_callback_exceptions=True)

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
            html.H1("Measurement", style={'text-align': 'left', 'margin-left': '6.75vw'}),
            dbc.Select(
                id='command-dropdown_m',
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
    html.Button('Properties', id='button-3', n_clicks=0, style={'background-color': '#1C2634', 'color': 'white', 'text-align': 'center'},),
    html.Button('Statistics', id='button-4', n_clicks=0, style={'background-color': '#1C2634', 'color': 'white', 'text-align': 'center'},),
    dcc.Store(id='store3'),
    html.Div(id='output3')

], style={'position': 'absolute', 'left': '90px','display': 'flex', 'justify-content': 'space-between', 'top': '50px', 'width': '20px', 'height': '25px'}),
  

     #1 quadrante
    dcc.Store(id='1-quadrante-content2', data=[
        html.Div([
            
            html.Div([
                html.Label("Name: ", style={'color': 'white'}),
                html.Div(id='name', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),
    
            html.Div([
                html.Label("Dimensions: ", style={'color': 'white'}),
                html.Div(id='dimensions', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

            html.Div([
                html.Label("Type: ", style={'color': 'white'}),
                html.Div(id='detect_type', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),
   
            html.Div([
                html.Label("Wavelength: ", style={'color': 'white'}),
                html.Div(id='wv', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),
             html.Div(id='divs_type')

], style={'background-color': '#1C2634', 'color': 'white', 'position': 'absolute', 'left': '0vw', 'top': '30px', 'width': '400px', 'height': '370px'}),
    
   #1 quadrante 
        html.Div([
            html.P("Objects", style={'text-align': 'left','margin-left': '1vw'}),
  
    #1 bloco
            html.Div([
                html.P("Source", style={'text-align': 'left', 'margin-left': '1vw'}),
                html.Div([
                    html.Label("Name: ", style={'color': 'white'}),
                    html.Div(id='source2_name', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
            ], style={'display': 'flex', 'align-items': 'center', 'margin-left': '1vw'}),
                html.Div([
                html.Label("Type:", style={ 'color': 'white'}),
                html.Div(id='source2_type', style={'background-color': '#243343', 'margin-left': '10px'}),
                ], style={'display': 'flex', 'align-items': 'center', 'margin-left': '1vw'}),
    ], style={'background-color': '#243343', 'color': 'white', 'display': 'flex', 'flex-direction': 'column', 'width':'250px', 'height': '90px','margin-left': '1vw'}),

        #2 bloco
            html.Div([
                html.P("Wavefront Sensor", style={'text-align': 'left', 'margin-left': '1vw'}),
                html.Div([
                    html.Label("Name: ", style={'color': 'white'}),
                    html.Div(id='wfs2_name', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
            ], style={'display': 'flex', 'align-items': 'center', 'margin-left': '1vw'}),
                html.Div([
                html.Label("Type:", style={ 'color': 'white'}),
                html.Div(id='wfs2_type', style={'background-color': '#243343', 'margin-left': '10px'}),
                ], style={'display': 'flex', 'align-items': 'center', 'margin-left': '1vw'}),
    ], style={'background-color': '#243343', 'color': 'white', 'display': 'flex', 'flex-direction': 'column', 'width':'250px', 'height': '90px','margin-left': '1vw', 'margin-top': '15px'}),


    #3 bloco
            html.Div([
                html.P("Wavefront Sensor", style={'text-align': 'left', 'margin-left': '1vw'}),
                html.Div([
                    html.Label("Name: ", style={'color': 'white'}),
                    dcc.Link(
                    html.Button(id='detector_name', style={'border-radius': '10%', 'border': '1.5px solid blue', 'background-color': '#1C2634', 'color':'white','font-size':'15px', 'width': '150px', 'height': '20px', 'margin-left': '10px'})
                    , href='/pixels')
            ], style={'display': 'flex', 'align-items': 'center', 'margin-left': '1vw'}),
                html.Div([
                html.Label("Type:", style={ 'color': 'white'}),
                html.Div("Detector", style={'background-color': '#243343', 'margin-left': '10px'}),
                ], style={'display': 'flex', 'align-items': 'center', 'margin-left': '1vw'}),
    ], style={'background-color': '#243343', 'color': 'white', 'display': 'flex', 'flex-direction': 'column', 'width':'250px', 'height': '90px','margin-left': '1vw', 'margin-top': '15px'}),

    


    ], style={'background-color': '#1C2634', 'color': 'white', 'position': 'absolute', 'left': '310px', 'top': '30px', 'width': '280px', 'height': '370px'}),
]),

#5quadrante
    dcc.Store(id='5-quadrante-content2', data=[
    
        html.Div([
        html.P("Statistics", style={'text-align': 'left','margin-left': '1vw'}),
        html.P("For the Image: ", style={'color': 'white', 'text-decoration': 'underline', 'text-decoration-color': '#C17FEF'}),
            html.Div([
                html.Label("Maximum value: ", style={'color': 'white'}),
                html.Div(id='stat_max_m', style={'background-color': '#243343', 'width': '180px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

            html.Div([
                html.Label("Minimum value: ", style={'color': 'white'}),
                html.Div(id='stat_min_m', style={'background-color': '#243343', 'width': '180px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

            html.Div([
                html.Label("Average values: ", style={'color': 'white'}),
                html.Div(id='stat_aver_m', style={'background-color': '#243343', 'width': '180px', 'height': '20px', 'margin-left': '10px'}),
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

            html.Div([
                html.Div([
                    html.P("For the X dimension Measurement: ", style={'color': 'white', 'text-decoration': 'underline', 'text-decoration-color': '#C17FEF'}),
                    html.Div([
                        html.Label("Maximum value: ", style={'color': 'white'}),
                        html.Div(id='stat_max_m_x', style={'background-color': '#243343', 'width': '60px', 'height': '20px', 'margin-left': '10px'})
                    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),
                    html.Div([
                        html.Label("Minimum value: ", style={'color': 'white'}),
                        html.Div(id='stat_min_m_x', style={'background-color': '#243343', 'width': '60px', 'height': '20px', 'margin-left': '10px'})
                    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),
                    html.Div([
                        html.Label("Average values: ", style={'color': 'white'}),
                        html.Div(id='stat_aver_m_x', style={'background-color': '#243343', 'width': '60px', 'height': '20px', 'margin-left': '10px'}),
                    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),
                ], style={'display': 'inline-block', 'vertical-align': 'top', 'margin-right': '20px'}),

                html.Div([
                    html.P("For the Y dimension Measurement: ", style={'color': 'white', 'text-decoration': 'underline', 'text-decoration-color': '#C17FEF'}),
                    html.Div([
                        html.Label("Maximum value: ", style={'color': 'white'}),
                        html.Div(id='stat_max_m_y', style={'background-color': '#243343', 'width': '180px', 'height': '20px', 'margin-left': '10px'})
                    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),
                    html.Div([
                        html.Label("Minimum value: ", style={'color': 'white'}),
                        html.Div(id='stat_min_m_y', style={'background-color': '#243343', 'width': '180px', 'height': '20px', 'margin-left': '10px'})
                    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),
                    html.Div([
                        html.Label("Average values: ", style={'color': 'white'}),
                        html.Div(id='stat_aver_m_y', style={'background-color': '#243343', 'width': '180px', 'height': '20px', 'margin-left': '10px'}),
                    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),
                ], style={'display': 'inline-block', 'vertical-align': 'top'}),
            ], style={'display': 'flex', 'justify-content': 'space-between'})

], style={
    'background-color': '#1C2634', 
    'position': 'absolute',
    'left': '0px',
    'top': '30px',
    'width': '42vw',  
    'height': '27vw',  
}),
]),




    #2 quadrante 
    #imagem
        html.Div([
            dbc.Select(
        id="aotpy_scale_m",
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
        id="aotpy_color_m",
            options=[
                {'label': 'Standard', 'value': 'Standard'},
                {'label': 'Grey', 'value': 'Grey'},
                {'label': 'Red', 'value': 'Red'},
                {'label': 'Green', 'value': 'Green'},
                {'label': 'Blue', 'value': 'Blue'},
                {'label': 'Heat', 'value': 'Heat'},
                {'label': 'Tropics', 'value': 'Tropics'},
                {'label': 'Rainbow', 'value': 'Rainbow'},
        ],
        value='Standard',
        className='custom-select',
        style={'width': "10vw",'color': 'white', 'height':'35px' }
    ),
        dbc.Select(
        id="aotpy_interval_m",
            options=[
                {'label': 'MinMax', 'value': 'MinMax'},
                {'label': 'ZScale', 'value': 'ZScale'},
                {'label': 'Percentile_30', 'value': 'Percentile_30'}
                
        ],
        value='MinMax',
        className='custom-select',
        style={'width': "10vw",'color': 'white', 'height':'35px' }
    ),
       # html.Div(id='image', style={'position': 'absolute', 'left': '160px', 'top': '50px', 'width': '600px', 'height': '420px'}),
        #dcc.Graph(id='teste_meas', style={'position': 'absolute', 'left': '20px', 'top': '50px'}),
        #dcc.Graph(id='measnovo', style={'position': 'absolute', 'left': '10px', 'top': '50px'}),
        
        
        html.Div([  
            
            html.Div(id='testes_imagem1'),
            #dcc.Graph(id='testes_imagem2', style={
            #    'position': 'absolute',
            #    'left': '200px',
            #    'top': '50px',
            #    'height': '30px',
            #    'width': '400px'
            #}),
            html.Div(id='testes_imagem2'),

            html.Div(dcc.Slider(
                id='frame_slider',
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
                        'top': '360px', 
                    }),
      
            dcc.Store(id='image_data_store'),  
                
    ]),

], style={
    'display': 'flex',  
    'justify-content': 'space-between',  
    'background-color': '#1C2634', 
    'position': 'absolute', 
    'left': '700px', 
    'top': '50px', 
    'width': '600px', 
    'height': '400px'
}),
  

  
#3 quadrante ->1 cube
    html.Div([
        html.Div([
            html.Div([  
                dcc.Graph(id='x_dimension_image', style={'position': 'absolute', 'left': '0vw', 'top': '0vw'}),
                dcc.Graph(id='y_dimension_image', style={'position': 'absolute', 'left': '28.5vw', 'top': '0vw'}),
              #  slider,
    ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'center'}),

]),

], style={
    'background-color': '#1C2634',  # Cor ectangulo
    'position': 'absolute',
    'left': '1vw',
    'top': '34vw',
    'width': '58vw',  
    'height': '21vw'  
}),
 #'left': '160px', 'top': '80px', 'width': '400px', 'height': '390px'
    #4 quadrante

html.Div([
    
    html.Div([  
            dcc.Graph(id='scatterplot_2dim', style={'position': 'absolute'}),
    ], style={
        'background-color': '#1C2634',  # Cor rectangulo
        'position': 'absolute',
        'left': '0vw',
        'top': '0vw',
        'width': '15vw',  
        'height': '17vw'  
    }),

    ], style={
    'background-color': '#1C2634',  # Cor ectangulo
    'position': 'absolute',
    'left': '60vw',
    'top': '34vw',
    'width': '43vw',  
    'height': '25vw'  
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
        return 'greys_r'
    elif colormap == 'Red':
        return 'reds_r'
    elif colormap == 'Green':
        return 'greens_r'
    elif colormap == 'Blue':
        return 'blues_r'
    elif colormap == 'Heat':
        return 'hot'
    elif colormap == 'Tropic':
        return 'tropic'
    elif colormap == 'Rainbow':
        return 'rainbow'
    else:
        raise ValueError(f'Invalid colormap {colormap}')
    
    
def apply_interval(image, interval_type):
    if interval_type == 'MinMax':
        interval = MinMaxInterval()
        normalized_image = interval(image)

        return normalized_image
    elif interval_type == 'ZScale':
        zscale_interval = ZScaleInterval(n_samples=1000, contrast=0.25, max_reject=0.5, min_npixels=5, krej=2.5, max_iterations=5)
        normalized_image = zscale_interval(image)
        
        return normalized_image
   
    elif interval_type == 'Percentile_30':
        percentileinterval = PercentileInterval(30.)
        normalized_image = percentileinterval(image)

        return normalized_image
    else:
        raise ValueError(f'Invalid interval: {interval_type}')

    
def extract_coordinates(clickData):
    x = clickData['points'][0]['x']
    y = clickData['points'][0]['y']
    z = clickData['points'][0]['z']
    return x, y, z

def none_to_string(*args):
    return ['None' if arg is None or (isinstance(arg, list) and not arg) else arg for arg in args]

#Callbacks
@callback(
    Output('command-dropdown_m', 'options'),
    Output('command-dropdown_m', 'value'),
    [Input('url', 'pathname')],
    [State('pickle_store', 'data')]
)
def see_meas_wfs(pathname, pickle_file):
    if pathname == '/measurements' and pickle_file is not None:
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        sensors = sys.wavefront_sensors

        measurements = [sensor.measurements for sensor in sensors if sensor.measurements is not None]
        if measurements:
            options = [{'label': measurement.name, 'value': measurement.name} for measurement in measurements]
            initial_value = measurements[0].name
            return options, initial_value
        else:
            return [], None
    else:
        return [], None
    

@callback(
    [Output('name', 'children'),
    Output('dimensions', 'children'),
    Output('wv', 'children'),
    Output('detect_type', 'children')],
    [Input('pickle_store', 'data'),
     Input('url', 'pathname'),
     Input('command-dropdown_m', 'value')]
)
def key_properties_meas(pickle_file, pathname, selected_command):
    if pathname == '/measurements' and pickle_file is not None:
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        if not selected_command:
            selected_command = sys.wavefront_sensors[0].measurements.name if sys.wavefront_sensors else None
        
        sensor = next((sensor for sensor in sys.wavefront_sensors if sensor.measurements.name == selected_command), None)
        
        if sensor is None or sensor.measurements is None:
            return ["None"] * 10  
        
        name = sensor.measurements.name
        dimensions = sensor.dimensions
        wv = sensor.wavelength
        detect_type = type(sensor).__name__
        
        #Assim mostra o None
        name, dimensions, wv, detect_type = none_to_string(name, dimensions, wv, detect_type) 
        print(f'Name: {name}, Dimensions: {dimensions}, Wavelength: {wv}, type: {detect_type}')
        return name, dimensions, wv, detect_type
    else: 
        return ["None"] * 4
    
#para a secção dos objetos

@callback(
    [Output('source2_name', 'children'),
     Output('source2_type', 'children'),
    Output('detector_name', 'children'),
    Output('wfs2_name', 'children'),
    Output('wfs2_type', 'children')],
    [Input('pickle_store', 'data'),
     Input('url', 'pathname'),
     Input('command-dropdown_m', 'value')]
)
def key_properties_objects1(pickle_file, pathname, selected_command):
    if pathname == '/measurements' and pickle_file is not None:
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        if not selected_command:
            selected_command = sys.wavefront_sensors[0].measurements.name if sys.wavefront_sensors else None
        
        sensor = next((sensor for sensor in sys.wavefront_sensors if sensor.measurements.name == selected_command), None)
        
        if sensor is None or sensor.measurements is None:
            return ["None"] * 5 
        
        #print(vars(sensor.detector))  # attributos do detetor muito util
        #print(dir(sensor.detector)) #basicamente quais sao os topicos que existem

        source_name= sensor.source.uid
        source_type= type(sensor.source).__name__
        detector_name= sensor.detector.uid
        wfs_name= sensor.uid
        wfs_type= type(sensor).__name__
        source_name, source_type,detector_name, wfs_name, wfs_type = none_to_string(source_name, source_type,detector_name, wfs_name, wfs_type)  

        return source_name, source_type,detector_name, wfs_name, wfs_type 
    else: 
        return ["None"] * 5



@callback(
    Output('divs_type', 'children'),
    [Input('pickle_store', 'data'),
     Input('url', 'pathname'),
     Input('command-dropdown_m', 'value')]
)
def specific_properties_meas(pickle_file, pathname, selected_command):
    if pathname == '/measurements' and pickle_file is not None:
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        if not selected_command:
            selected_command = sys.wavefront_sensors[0].measurements.name if sys.wavefront_sensors else None
        
        sensor = next((sensor for sensor in sys.wavefront_sensors if sensor.measurements.name == selected_command), None)
        
        if sensor is None or sensor.measurements is None:
            return ["None"] * 1 
        
        if (type(sensor).__name__) == 'Pyramid':
            n_sides = sensor.n_sides
            modulation = sensor.modulation

            return html.Div([     
        html.Div([
                html.Label("Number Sides", style={'color': 'white'}),
                html.Div(n_sides, style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),
                 html.Div([
                html.Label("Modulation: ", style={'color': 'white'}),
                html.Div(modulation, style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),
        ])   
        else: #se for shack-hartman 
            centroiding = sensor.centroiding_algorithm
            print(f'Centroiding: {centroiding}')
            centroiding= none_to_string(centroiding)
            return  html.Div([
                html.Label("Centroiding Algorithm", style={'color': 'white'}),
                html.Div(centroiding, style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),



        
        #Assim mostra o None
        name, dimensions, wv, detect_type = none_to_string(name, dimensions, wv, detect_type) 
        print(f'Name: {name}, Dimensions: {dimensions}, Wavelength: {wv}, type: {detect_type}')
        return name, dimensions, wv, detect_type
    else: 
        return ["None"] * 4

#Imagem com slider

@callback(
    Output('image_data_store', 'data'),
    Output('frame_slider', 'max'),
    Output('frame_slider', 'marks'), 
    Output('frame_slider', 'value'),
    [Input('pickle_store', 'data'),
    Input('url', 'pathname'),
    Input('command-dropdown_m', 'value')]
)
def load_image_data(pickle_file, pathname, selected_command):
    if pathname == '/measurements' and pickle_file is not None:
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        if not selected_command:
            selected_command = sys.wavefront_sensors[0].measurements.name if sys.wavefront_sensors else None
        
        sensor = next((sensor for sensor in sys.wavefront_sensors if sensor.measurements.name == selected_command), None)
        
        if sensor is None or sensor.measurements is None:
            return None, 0, dash.no_update, dash.no_update
        
        img_data = sensor.measurements.data 
        
        max_frame = img_data.shape[0] - 1
        step_value = max(1, max_frame // 10)
        marks = {i: str(i) for i in range(0, max_frame + 1, step_value)}  
        print(f"max_frame: {max_frame}, marks: {marks}")
        return img_data.tolist(), max_frame, marks, 0
    else:
        return None, 0, dash.no_update, dash.no_update

@callback(
    Output('testes_imagem1', 'children'),
    [Input('image_data_store', 'data'),
    Input('pickle_store', 'data'),
    Input('frame_slider', 'value'),
    Input('aotpy_scale_m', 'value'),
    Input('aotpy_color_m', 'value'),
    Input('aotpy_interval_m', 'value'),
    Input('x_dimension_image', 'clickData'),
    Input('command-dropdown_m','value')]
)
def update_image_x(data, pickle_file, frame_index, scale_type,color_type,interval_type, clickData, selected_command):
        with open(pickle_file, 'rb') as f:
            ctx = dash.callback_context
            sys = pickle.load(f)

        if not selected_command:
            selected_command = sys.wavefront_sensors[0].measurements.name if sys.wavefront_sensors else None

        sensor = next((sensor for sensor in sys.wavefront_sensors if sensor.measurements.name == selected_command), None)

        if sensor is None or sensor.measurements is None:
            return {}

        subaperture_mask = sensor.subaperture_mask 
        if subaperture_mask is None or subaperture_mask.data is None:
            return html.Div("The image cannot be rasterized without the subaperture_mask", style={
                    'position': 'absolute',
                    'left': '300px',
                    'top': '50px',
                    'width': '140px'
                    
                })
        
        measurements = sensor.measurements.data
        measurements_x = measurements[:, 0, :]
        mask = sensor.subaperture_mask.data

        #meter nos espaços none
        output = np.full(mask.shape, np.nan)
        #onde não tem -1
        row_indices, col_indices = np.where(mask != -1)
        measurement_indices = mask[row_indices, col_indices]

        a = []
        for i in range(measurements_x.shape[0]):
            output[row_indices, col_indices] = measurements_x[i, measurement_indices]
            a.append(output.copy())
        #plt.imshow(output)

        if ctx.triggered and ctx.triggered[0]['prop_id'].split('.')[0] == 'x_dimension_image':
            # cordenadas do click data 
                x, y, z = extract_coordinates(clickData)
            
            # o x do slider é o frame index (tempo)
                frame_index = int(x)

        frame_processed = a[frame_index]
        frame_processed = apply_interval(frame_processed, interval_type)
        frame_processed = apply_scale(frame_processed, scale_type)
        colormap = apply_colormap(color_type)

        #frame_processed = frame_processed.reshape(-1, 1)


        #fig = go.Figure(data=go.Heatmap(z=frame_processed, colorscale='Viridis'))
        fig = px.imshow(frame_processed, color_continuous_scale=colormap)
        fig.update_layout(
            title=f'Frame {frame_index} Dimension X',
            #xaxis_title='X',
            #yaxis_title='Y',
            autosize=False,
            width=250,
            height=300,
            paper_bgcolor='rgba(0,0,0,0)', 
            title_font=dict(color='white'),  
            xaxis_title_font=dict(color='white'),  
            yaxis_title_font=dict(color='white'),
            xaxis_tickfont=dict(color='white'),  
            yaxis_tickfont=dict(color='white'),
            coloraxis_showscale=False, 
            margin=dict(l=65, r=50, b=65, t=90),
            coloraxis_colorbar=dict(tickfont=dict(color='white')),
        )
        return dcc.Graph(figure=fig, style={
                    'position': 'absolute',
                    'left': '3vw',
                    'top': '2vw',
                    'height': '7vw',
                    'width': '15vw'
                })


#at 2 cima
@callback(
    Output('testes_imagem2', 'children'),
    [Input('image_data_store', 'data'),
    Input('pickle_store', 'data'),
    Input('frame_slider', 'value'),
    Input('aotpy_scale_m', 'value'),
    Input('aotpy_color_m', 'value'),
    Input('aotpy_interval_m', 'value'),
    Input('y_dimension_image', 'clickData'),
    Input('command-dropdown_m','value')]
)
def update_image_y(data,pickle_file, frame_index, scale_type, color_type, interval_type, clickData, selected_command):
    with open(pickle_file, 'rb') as f:
        ctx = dash.callback_context
        sys = pickle.load(f)

        if not selected_command:
            selected_command = sys.wavefront_sensors[0].measurements.name if sys.wavefront_sensors else None
        
        sensor = next((sensor for sensor in sys.wavefront_sensors if sensor.measurements.name == selected_command), None)
        
        if sensor is None or sensor.measurements is None:
            return {}

        subaperture_mask = sensor.subaperture_mask 
        if subaperture_mask is None or subaperture_mask.data is None:
            return html.Div("The image cannot be rasterized without the subaperture_mask", style={
                    'position': 'absolute',
                    'left': '300px',
                    'top': '50px',
                    'width': '140px'
                    
                })
        

        measurements = sensor.measurements.data
        measurements_y = measurements[:, 1, :]
        mask = sensor.subaperture_mask.data

        #meter nos espaços none
        output = np.full(mask.shape, np.nan)
        #onde não tem -1
        row_indices, col_indices = np.where(mask != -1)
        measurement_indices = mask[row_indices, col_indices]

        a = []
        for i in range(measurements_y.shape[0]):
            output[row_indices, col_indices] = measurements_y[i, measurement_indices]
            a.append(output.copy())
        #plt.imshow(output)
        if ctx.triggered and ctx.triggered[0]['prop_id'].split('.')[0] == 'y_dimension_image':
            # cordenadas do click data 
                x, y, z = extract_coordinates(clickData)
            
            # o x do slider é o frame index (tempo)
                frame_index = int(x)

        frame_processed = a[frame_index]
        frame_processed = apply_interval(frame_processed, interval_type)
        frame_processed = apply_scale(frame_processed, scale_type)
        colormap = apply_colormap(color_type)

        #fig = go.Figure(data=go.Heatmap(z=frame_processed, colorscale='Viridis'))
        fig = px.imshow(frame_processed, color_continuous_scale=colormap)
        fig.update_layout(
            title=f'Frame {frame_index} Dimension Y',
            #xaxis_title='X',
            #yaxis_title='Y',
            autosize=False,
            width=250,
            height=300,
            paper_bgcolor='rgba(0,0,0,0)', 
            title_font=dict(color='white'),  
            xaxis_title_font=dict(color='white'),  
            yaxis_title_font=dict(color='white'),
            xaxis_tickfont=dict(color='white'),  
            yaxis_tickfont=dict(color='white'),
            coloraxis_showscale=False, 
            margin=dict(l=65, r=50, b=65, t=90),
            coloraxis_colorbar=dict(tickfont=dict(color='white')),
        )
        return dcc.Graph(figure=fig, style={
                    'position': 'absolute',
                    'left': '21vw',
                    'top': '2vw',
                    'height': '5vw',
                    'width': '10vw'
                })
#Imagem estática

#Measurements from the sensor over time. Each of its Sv subapertures is able to measure in d dimensions. (Dimensions t×d×Sv, in user defined units, using data type flt)

@callback(
    Output('x_dimension_image', 'figure'),
    Output('y_dimension_image', 'figure'),
    [Input('pickle_store', 'data'),
    Input('url', 'pathname'),
    Input('command-dropdown_m', 'value')]
)
def display_measurements(pickle_file, pathname, selected_command):
    if pathname == '/measurements' and pickle_file is not None:
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)
      
        if not selected_command:
            selected_command = sys.wavefront_sensors[0].measurements.name if sys.wavefront_sensors else None
        
        sensor = next((sensor for sensor in sys.wavefront_sensors if sensor.measurements.name == selected_command), None)
        
        if sensor is None or sensor.measurements is None:
            return {},{}
        
        measurements = sensor.measurements.data  

# Separar
        x_measurements = measurements[:, 0, :]
        y_measurements = measurements[:, 1, :]

# 
        fig_x = go.Figure(data=go.Heatmap(z=x_measurements.T, colorscale='Viridis',colorbar=dict(tickfont=dict(color='white'))))
        fig_y = go.Figure(data=go.Heatmap(z=y_measurements.T, colorscale='Viridis',colorbar=dict(tickfont=dict(color='white'))))

        fig_x.update_layout(
            title='X measurement per subaperture per frame',
            xaxis_title='Frame',
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
            title='Y measurement per subaperture per frame',
            xaxis_title='Frame',
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
#gráfico 

@callback(
    Output('scatterplot_2dim', 'figure'),
    [Input('pickle_store', 'data'),
     Input('url', 'pathname'),
     Input('x_dimension_image', 'clickData'),
     Input('y_dimension_image', 'clickData'),
     Input('testes_imagem1', 'clickData'),
     Input('testes_imagem2', 'clickData'),
     Input('command-dropdown_m', 'value')]
)
def display_detector_frame(pickle_file, pathname, x_clickData, y_clickData,first_clickData,second_clickData, selected_command):
    if pathname == '/measurements' and pickle_file is not None:
        ctx = dash.callback_context
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        if not selected_command:
            selected_command = sys.wavefront_sensors[0].measurements.name if sys.wavefront_sensors else None
        
        sensor = next((sensor for sensor in sys.wavefront_sensors if sensor.measurements.name == selected_command), None)
        
        if sensor is None or sensor.measurements is None:
            return {}

        measurements = sensor.measurements.data
        meas_data_x = measurements[:, 0, :]
        meas_data_y = measurements[:, 1, :]
     
        meas_data_mean_x = np.mean(meas_data_x, axis=0)
        meas_data_mean_y = np.mean(meas_data_y, axis=0)

        time_values_x = list(range(len(meas_data_mean_x)))
        time_values_y = list(range(len(meas_data_mean_y)))

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=time_values_x, y=meas_data_mean_x, mode='lines', name='Mean X Intensity'))
        fig.add_trace(go.Scatter(x=time_values_y, y=meas_data_mean_y, mode='lines', name='Mean Y Intensity'))

        time_values_x, time_values_y, time_values_1, time_values_2, meas_over_time_x, meas_over_time_y, meas_over_time_1,meas_over_time_2,x_x, x_y, y_x,y_y = [None] * 12

        trigger_id = ctx.triggered[0]['prop_id'].split('.')[0] if ctx.triggered else None

        if trigger_id == 'x_dimension_image':
           
            x_x, y_x, z_x = extract_coordinates(x_clickData)
            meas_over_time_x = meas_data_x[:, int(y_x)]
            time_values_x = list(range(len(meas_over_time_x)))


        if trigger_id == 'y_dimension_image':
            x_y, y_y, z_y = extract_coordinates(y_clickData)
            meas_over_time_y = meas_data_y[:, int(y_y)]  
            time_values_y = list(range(len(meas_over_time_y)))

#estes nao dao

        if trigger_id == 'testes_imagem1':
            x_1, y_1, z_1 = extract_coordinates(first_clickData)
            meas_over_time_1 = meas_data_y[:, int(y_1)]  
            time_values_1 = list(range(len(meas_over_time_1)))
        
        if trigger_id == 'testes_imagem2':
            x_2, y_2, z_2 = extract_coordinates(second_clickData)
            meas_over_time_2 = meas_data_y[:, int(y_2)]  
            time_values_2 = list(range(len(meas_over_time_2)))
        

        print(f" o trigger é {trigger_id}")
        
        fig.add_trace(go.Scatter(x=time_values_x, y=meas_over_time_x, mode='lines', name=f'X Intensity x={x_x},y={y_x}'))    
        fig.add_trace(go.Scatter(x=time_values_y, y=meas_over_time_y, mode='lines', name=f'Y Intensity x={x_y},y={y_y}'))
        fig.add_trace(go.Scatter(x=time_values_1, y=meas_over_time_1, mode='lines', name='X Intensity 2D'))
        fig.add_trace(go.Scatter(x=time_values_2, y=meas_over_time_2, mode='lines', name='Y Intensity 2D'))

        fig.update_layout(
            title='Intensities per measurement per frame',
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
    Output('stat_max_m', 'children'),
    Output('stat_min_m', 'children'),
    Output('stat_aver_m', 'children'),
    [Input('pickle_store', 'data'),
     Input('url', 'pathname'),
     Input('command-dropdown_m', 'value')]
)
def display_stats_m(pickle_file, pathname, selected_command):
    if pathname == '/measurements' and pickle_file is not None:
       
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        if not selected_command:
            selected_command = sys.wavefront_sensors[0].measurements.name if sys.wavefront_sensors else None
        
        sensor = next((sensor for sensor in sys.wavefront_sensors if sensor.measurements.name == selected_command), None)
        
        if sensor is None or sensor.measurements is None:
            return ["None"] *3

        meas_data = sensor.measurements.data
    
        max_value = np.max(meas_data)
        min_value = np.min(meas_data)
        average = np.mean(meas_data)

        return f'{max_value:.5f}', f'{min_value:.5f}', f'{average:.5f}'
    else:
        return ["None"] *3

@callback(
    Output('stat_max_m_x', 'children'),
    Output('stat_min_m_x', 'children'),
    Output('stat_aver_m_x', 'children'),
    [Input('pickle_store', 'data'),
     Input('url', 'pathname'),
     Input('x_dimension_image', 'clickData'),
     Input('command-dropdown_m', 'value')]
)
def display_stats_m_spe_x(pickle_file, pathname, clickData, selected_command):
    if pathname == '/measurements' and pickle_file is not None:
        ctx = dash.callback_context
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)
        
        if not selected_command:
            selected_command = sys.wavefront_sensors[0].measurements.name if sys.wavefront_sensors else None
        
        sensor = next((sensor for sensor in sys.wavefront_sensors if sensor.measurements.name == selected_command), None)
     
        measurements = sensor.measurements.data
        meas_data_x = measurements[:, 0, :]
        meas_over_time = 0

        trigger_id = ctx.triggered[0]['prop_id'].split('.')[0] if ctx.triggered else None

        if trigger_id == 'x_dimension_image':
           
            x, y, z = extract_coordinates(clickData)
            meas_over_time = meas_data_x[:, int(y)]
    
        max_value = np.max(meas_over_time)
        min_value = np.min(meas_over_time)
        average = np.mean(meas_over_time)
        return f'{max_value:.5f}', f'{min_value:.5f}', f'{average:.5f}'
    else:
        return ["None"] *3

@callback(
    Output('stat_max_m_y', 'children'),
    Output('stat_min_m_y', 'children'),
    Output('stat_aver_m_y', 'children'),
    [Input('pickle_store', 'data'),
     Input('url', 'pathname'),
     Input('y_dimension_image', 'clickData'),
     Input('command-dropdown_m', 'value')]
)
def display_stats_m_spe_y(pickle_file, pathname, clickData, selected_command):
    if pathname == '/measurements' and pickle_file is not None:
        ctx = dash.callback_context
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)
        
        if not selected_command:
            selected_command = sys.wavefront_sensors[0].measurements.name if sys.wavefront_sensors else None
        
        sensor = next((sensor for sensor in sys.wavefront_sensors if sensor.measurements.name == selected_command), None)
     
        measurements = sensor.measurements.data
        meas_data_y = measurements[:, 1, :]
        meas_over_time = 0

        trigger_id = ctx.triggered[0]['prop_id'].split('.')[0] if ctx.triggered else None

        if trigger_id == 'y_dimension_image':
           
            x, y, z = extract_coordinates(clickData)
            meas_over_time = meas_data_y[:, int(y)]
    
        max_value = np.max(meas_over_time)
        min_value = np.min(meas_over_time)
        average = np.mean(meas_over_time)
        return f'{max_value:.5f}', f'{min_value:.5f}', f'{average:.5f}'
    else:
        return ["None"] *3



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
