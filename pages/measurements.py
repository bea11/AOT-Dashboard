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


dash.register_page(__name__, path='/measurements', supress_callback_exceptions=True)

option_STYLE = {
    'width': '100%',
    'background-color': '#1C2634',
    'color': 'white',
    'cursor': 'pointer',
    'border': '1px solid #243343',
}


layout = html.Div([
    html.H1("Measurements", style={'text-align': 'left', 'margin-left': '12vw', 'marginBottom' : '0px'}),

    html.Div([
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
                html.Label("Pyramid ", style={'color': 'white'}),
                html.Div([], style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px', 'margin-top': '13px'}),

            html.Div([
                html.Label("Shack Hartman", style={'color': 'white'}),
                html.Div([], style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

   
            html.Div([
                html.Label("Wavelength: ", style={'color': 'white'}),
                html.Div(id='wv', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
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
        #dcc.Graph(id='teste_meas', style={'position': 'absolute', 'left': '20px', 'top': '50px'}),
        #dcc.Graph(id='measnovo', style={'position': 'absolute', 'left': '10px', 'top': '50px'}),
        
        
        html.Div([  
            #    dcc.Graph(id='new_x_dimension_image', style={'position': 'absolute', 'left': '0px', 'top': '5px'}),
             #   dcc.Graph(id='new_y_dimension_image', style={'position': 'absolute', 'left': '300px', 'top': '10px'}),
             #   dcc.Interval(
             #       id='interval-component',
             #       interval=1*1000,  # 1000 milliseconds = 1 second
             #       n_intervals=0
             #   ),
            
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
                        'top': '350px', 
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
                dcc.Graph(id='x_dimension_image', style={'position': 'absolute', 'left': '0px', 'top': '5px'}),
                dcc.Graph(id='y_dimension_image', style={'position': 'absolute', 'left': '300px', 'top': '10px'}),
              #  slider,
    ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'center'}),

]),

], style={
    'background-color': '#1C2634',  # Cor ectangulo
    'position': 'absolute',
    'left': '40px',
    'top': '480px',
    'width': '690px',  
    'height': '320px'  
}),
 #'left': '160px', 'top': '80px', 'width': '400px', 'height': '390px'
    #4 quadrante
    html.Div([  
        dcc.Graph(id='scatterplot', style={'position': 'absolute'}),
], style={
    'background-color': '#1C2634',  # Cor rectangulo
    'position': 'absolute',
    'left': '760px',
    'top': '480px',
    'width': '580px',  
    'height': '340px'  
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
        return 'greys'
    elif colormap == 'Red':
        return 'reds'
    elif colormap == 'Green':
        return 'greens'
    elif colormap == 'Blue':
        return 'blues'
    elif colormap == 'Heat':
        return 'hot'
    elif colormap == 'Tropic':
        return 'tropic'
    elif colormap == 'Rainbow':
        return 'rainbow'
    else:
        raise ValueError(f'Invalid colormap {colormap}')
    
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
        #sm2 = sensor.subaperture_mask
        #refm = sensor.ref_measurements.name 
        #si = sensor.subaperture_intensities.name
        wv = sensor.wavelength
        detect_type = type(sensor).__name__


        
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
        
       # print(f'img_data shape: {img_data.shape}')
    
        max_frame = img_data.shape[0] - 1
        marks = {i: str(i) for i in range(0, max_frame + 1, 1000)}  
        return img_data.tolist(), max_frame, marks, 0
    else:
        return None, 0, dash.no_update, dash.no_update

@callback(
    Output('testes_imagem1', 'children'),
    [Input('image_data_store', 'data'),
    Input('pickle_store', 'data'),
    Input('frame_slider', 'value'),
    Input('aotpy_scale_m', 'value'),
    Input('x_dimension_image', 'clickData'),
    Input('command-dropdown_m','value')]
)
def update_image_x(data,pickle_file, frame_index, scale_type, x_clickData, selected_command):
   # print(f'data: {data}')
    #print(f'frame_index: {frame_index}')
    with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

    if not selected_command:
            selected_command = sys.wavefront_sensors[0].measurements.name if sys.wavefront_sensors else None
        
    sensor = next((sensor for sensor in sys.wavefront_sensors if sensor.measurements.name == selected_command), None)
        
    if sensor is None or sensor.measurements is None:
            return {}
    
    subaperture_mask = sensor.subaperture_mask  
    img_data = sensor.measurements.data   

    if data is None or frame_index is None:
        return {}

    if subaperture_mask is None or subaperture_mask.data is None:
        mask_flattened = None
    else:
        subaperture_mask_data = subaperture_mask.data
        mask_flattened = subaperture_mask_data.flatten()

    if x_clickData is not None:
        # cordenadas do click data 
            x, y, z = extract_coordinates(x_clickData)
        
        # o x do slider é o frame index (tempo)
            frame_index = int(x)
    
    frame = img_data[frame_index, 0, :]
    #frame = img_data[frame_index, 0, :].reshape(-1, 1)
    if mask_flattened is not None:
        valid_indices = mask_flattened >= 0
        frame_processed = frame[valid_indices]
    else:
        frame_processed = frame

    frame_processed = frame_processed.reshape(-1, 1)

    frame_processed = apply_scale(frame_processed, scale_type)

    fig = px.imshow(frame_processed, color_continuous_scale='Viridis')
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
    )
    
    if subaperture_mask is None or subaperture_mask.data is None:
        return html.Div("The image cannot be rasterized without the subaperture_mask", style={
                'position': 'absolute',
                'left': '30px',
                'top': '50px',
                'width': '140px'
                
            })
    else:
        return dcc.Graph(figure=fig, style={
                'position': 'absolute',
                'left': '0px',
                'top': '50px',
                'height': '30px',
                'width': '400px'
            })

#at 2 cima
@callback(
    Output('testes_imagem2', 'children'),
    [Input('image_data_store', 'data'),
    Input('pickle_store', 'data'),
    Input('frame_slider', 'value'),
    Input('aotpy_scale_m', 'value'),
    Input('y_dimension_image', 'clickData'),
    Input('command-dropdown_m','value')]
)
def update_image_y(data,pickle_file, frame_index, scale_type, y_clickData, selected_command):
   # print(f'data: {data}')
    #print(f'frame_index: {frame_index}')
    with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

    if not selected_command:
            selected_command = sys.wavefront_sensors[0].measurements.name if sys.wavefront_sensors else None
        
    sensor = next((sensor for sensor in sys.wavefront_sensors if sensor.measurements.name == selected_command), None)
        
    if sensor is None or sensor.measurements is None:
            return {}

    subaperture_mask = sensor.subaperture_mask  
    img_data = sensor.measurements.data   

    if data is None or frame_index is None:
        return {}

    if subaperture_mask is None or subaperture_mask.data is None:
        
        mask_flattened = None
       # mask_flattened = None
    else:
        subaperture_mask_data = subaperture_mask.data
        mask_flattened = subaperture_mask_data.flatten()

    if y_clickData is not None:
        # cordenadas do click data 
            x, y, z = extract_coordinates(y_clickData)
        
        # o x do slider é o frame index (tempo)
            frame_index = int(x)
    
    frame = img_data[frame_index, 1, :]
    #frame = img_data[frame_index, 0, :].reshape(-1, 1)
    if mask_flattened is not None:
        valid_indices = mask_flattened >= 0
        frame_processed = frame[valid_indices]
    else:
        frame_processed = frame

    frame_processed = frame_processed.reshape(-1, 1)

    frame_processed = apply_scale(frame_processed, scale_type)

    fig = px.imshow(frame_processed, color_continuous_scale='Viridis')
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
    )

    if subaperture_mask is None or subaperture_mask.data is None:
        return html.Div("The image cannot be rasterized without the subaperture_mask", style={
                'position': 'absolute',
                'left': '300px',
                'top': '50px',
                'width': '140px'
                
            })
    else:
        return dcc.Graph(figure=fig, style={
                'position': 'absolute',
                'left': '200px',
                'top': '50px',
                'height': '30px',
                'width': '400px'
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

        #subaperture_mask = sys.wavefront_sensors[0].subaperture_mask
        


        #if subaperture_mask is None or subaperture_mask.data is None:
        #    mask_flattened = None
        #else:
        #    subaperture_mask_data = subaperture_mask.data
        #    mask_flattened = subaperture_mask_data.flatten()

# Separar
        x_measurements = measurements[:, 0, :]
        y_measurements = measurements[:, 1, :]

#  t x sv
        #t, sv = x_measurements.shape

# subaperture mask filter
        #if mask_flattened is not None:
        #    valid_indices = mask_flattened >= 0
        #    x_processed = x_measurements[:, valid_indices]
        #    y_processed = y_measurements[:, valid_indices]
        #else:
        #    x_processed = x_measurements
        #    y_processed = y_measurements

# 
        fig_x = go.Figure(data=go.Heatmap(z=x_measurements.T, colorscale='Viridis'))
        fig_y = go.Figure(data=go.Heatmap(z=y_measurements.T, colorscale='Viridis'))

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

#Gráfico
@callback(
    Output('scatterplot', 'figure'),
    [Input('pickle_store', 'data'),
     Input('url', 'pathname'),
     Input('command-dropdown_m', 'value')]
)
def display_detector_frame(pickle_file, pathname, selected_command):
    if pathname == '/measurements' and pickle_file is not None:
        
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        if not selected_command:
            selected_command = sys.wavefront_sensors[0].measurements.name if sys.wavefront_sensors else None
        
        sensor = next((sensor for sensor in sys.wavefront_sensors if sensor.measurements.name == selected_command), None)
        
        if sensor is None or sensor.measurements is None:
            return {}

        meas_data = sensor.measurements.data  
     
        meas_data_mean = np.mean(meas_data, axis=(1, 2))

        time_values = list(range(len(meas_data_mean)))

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=time_values, y=meas_data_mean, mode='lines', name='Mean intensity over time'))
        fig.update_layout(
            title='Density over time',
            xaxis_title='Time',
            yaxis_title='Density',
            autosize=False,
            width=600,
            height=350,
            margin=dict(l=65, r=50, b=65, t=90),
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

        return f'{max_value}', f'{min_value}', f'{average}'
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
