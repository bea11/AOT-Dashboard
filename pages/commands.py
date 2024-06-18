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
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from astropy.visualization import MinMaxInterval, ZScaleInterval, PercentileInterval

dash.register_page(__name__, path='/commands', suppress_callback_exceptions=True)

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
    html.Div(
        style={'display': 'flex', 'alignItems': 'center', 'justifyContent': 'space-between', 'left': '0vw'},
        children=[
            html.H1("Command", style={'text-align': 'left', 'margin-left': '6.75vw'}),
            dbc.Select(
                id='command-dropdown_c',
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
    

   #1 quadrante
    html.Div([

        html.P("Properties", style={'text-align': 'left', 'margin-left': '1vw'}),
        
    #Strings    
        html.Div([
            html.Label("Loop: ", style={'color': 'white'}),
            html.Div(id='loop', style={'background-color': '#243343', 'width': '160px', 'height': '18px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),
    
        html.Div([
            html.Label("Reference Commmands: ", style={'color': 'white'}),
            html.Div(id='refcom', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

        html.Div([
            html.Label("Residual Commmands: ", style={'color': 'white'}),
            html.Div(id='rescom', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),
     
    #Integers
        html.Div([
            html.Label("Modal Coefficients: ", style={'color': 'white'}),
            html.Div(id='mc', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px', 'margin-top': '13px'}),


        html.Div([
            html.Label("Wavefront Corrector: ", style={'color': 'white'}),
            html.Div(id='wave_corrector', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

    #Floats
        html.Div([
            html.Label("Valid Actuators: ", style={'color': 'white'}),
            html.Div(id='valid_act', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

        html.Div([
            html.Label("tfz_den: ", style={'color': 'white'}),
            html.Div(id='tfz_den', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),
   
        html.Div([
            html.Label("tfz_num: ", style={'color': 'white'}),
            html.Div(id='tfz_num', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),
        html.Div(id='deformmirror'),

    ], style={'background-color': '#1C2634', 'color': 'white', 'position': 'absolute', 'left': '6.75vw', 'top': '5vw', 'width': '37vw', 'height': '32vw'}),
    
   html.Div([
            html.P("Objects", style={'text-align': 'left','margin-left': '1vw'}),
  
    #1 bloco
            html.Div([
                html.P("Telescope", style={'text-align': 'left', 'margin-left': '1vw'}),
                html.Div([
                    html.Label("Name: ", style={'color': 'white'}),
                    html.Div(id='telescope_name', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
            ], style={'display': 'flex', 'align-items': 'center', 'margin-left': '1vw'}),
                html.Div([
                html.Label("Type:", style={ 'color': 'white'}),
                html.Div(id='telescope_type', style={'background-color': '#243343', 'margin-left': '10px'}),
                ], style={'display': 'flex', 'align-items': 'center', 'margin-left': '1vw'}),
    ], style={'background-color': '#243343', 'color': 'white', 'display': 'flex', 'flex-direction': 'column', 'width':'250px', 'height': '90px','margin-left': '1vw'}),

    #2 bloco
            html.Div([
                html.P("Aberration 1", style={'text-align': 'left', 'margin-left': '1vw'}),
                html.Div([
                    html.Label("Name: ", style={'color': 'white'}),
                    html.Button("Example", style={'border-radius': '10%', 'border': '1.5px solid blue', 'background-color': '#1C2634', 'color':'white','font-size':'15px', 'width': '150px', 'height': '20px', 'margin-left': '10px'})
                    
            ], style={'display': 'flex', 'align-items': 'center', 'margin-left': '1vw'}),
                html.Div([
                    html.Label("Type:", style={ 'color': 'white'}),
                    html.Div("Other", style={'background-color': '#243343', 'margin-left': '10px'}),
                ], style={'display': 'flex', 'align-items': 'center', 'margin-left': '1vw'}),
    ], style={'background-color': '#243343', 'color': 'white', 'display': 'flex', 'flex-direction': 'column', 'width':'250px', 'height': '90px','margin-left': '1vw', 'margin-top': '15px'}),
                
                html.Div([
                html.P("Aberration 2", style={'text-align': 'left', 'margin-left': '1vw'}),
                html.Div([
                    html.Label("Name: ", style={'color': 'white'}),
                    html.Div("Example", style={'border-radius': '10%', 'border': '1.5px solid blue', 'background-color': '#1C2634', 'color':'white','font-size':'15px', 'width': '150px', 'height': '20px', 'margin-left': '10px'})
            ], style={'display': 'flex', 'align-items': 'center', 'margin-left': '1vw'}),
                html.Div([
                    html.Label("Type:", style={ 'color': 'white'}),
                    html.Div("Other", style={'background-color': '#243343', 'margin-left': '10px'}),
                ], style={'display': 'flex', 'align-items': 'center', 'margin-left': '1vw'}),
    
    ], style={'background-color': '#243343', 'color': 'white', 'display': 'flex', 'flex-direction': 'column', 'width':'250px', 'height': '90px','margin-left': '1vw', 'margin-top': '15px'}),


     ], style={'background-color': '#1C2634', 'color': 'white', 'position': 'absolute', 'left': '37vw', 'top': '5vw', 'width': '20vw', 'height': '32vw'}),

    #2 quadrante 
    #imagem
    html.Div([
     dbc.Select(
        id="aotpy_scale_c",
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
        id="aotpy_color_c",
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
        id="aotpy_interval_c",
            options=[
                {'label': 'MinMax', 'value': 'MinMax'},
                {'label': 'ZScale', 'value': 'ZScale'},
                {'label': 'Percentile_30', 'value': 'Percentile_30'}
                
        ],
        value='MinMax',
        className='custom-select',
        style={'width': "10vw",'color': 'white', 'height':'35px' }
    ),
    html.Div(id='teste2_imagem'),

    html.Div(dcc.Slider(
                id='frame2_slider',
                min=0,
                max=1,
                step=1,
                value=0,
                marks={},
            ), style={
                        'width': '450px',  
                        'position': 'absolute',  
                        'left': '20px',  
                        'height': '30px',
                        'top': '400px',  
                    }),

], style={
    'display': 'flex',  
    'justify-content': 'space-between',  
    'background-color': '#1C2634', 
    'position': 'absolute', 
    'left': '58vw',
    'top': '3vw',
    'width': '39vw', 
    'height': '35.5vw'
}),
  
  #3 quadrante
  html.Div([
    dcc.Graph(id='imag2D_com', style={'position': 'absolute', 'left': '10px', 'height': '320px', 'width': '500px'}),
    
], style={
    'background-color': '#1C2634',  
    'position': 'absolute',
    'left': '8vw',
    'top': '39vw',
    'width': '44vw',  
    'height': '25vw' 
}),
 #'left': '160px', 'top': '80px', 'width': '400px', 'height': '390px'
 
    #4 quadrante
    html.Div([
        html.Div([  
        dcc.Graph(id='differentplot', style={'position': 'absolute', 'left': '20px', 'height': '330px', 'width': '500px'}),
    ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'center'}),

   
], style={
    'background-color': '#1C2634',  # Cor rectangulo
    'position': 'absolute',
    'left': '53vw',
    'top': '39vw',
    'width': '44.5vw',  
    'height': '25vw'  
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



#Callbacks

#Name of wavefront sensor

def none_to_string(*args):
    return ['None' if arg is None or (isinstance(arg, list) and not arg) else arg for arg in args]
    
@callback(
    Output('command-dropdown_c', 'options'),
    Output('command-dropdown_c', 'value'),
    [Input('url', 'pathname')],
    [State('pickle_store', 'data')]
)
def see_commands_loop(pathname, pickle_file):
    if pathname == '/commands' and pickle_file is not None:
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        loops = [loop for loop in sys.loops if not isinstance(loop, aotpy.OffloadLoop)]
        commands = [loop.commands for loop in loops if loop.commands is not None]
        if commands: 
            options = [{'label': command.name, 'value': command.name} for command in commands]
            initial_value = commands[0].name 
            return options, initial_value
        else:
            return [], None
    else:
        return [], None
    

@callback(
    [Output('loop', 'children'),
    Output('refcom', 'children'),
    Output('rescom', 'children'),
    Output('mc', 'children'),
    Output('wave_corrector', 'children'),
    Output('valid_act', 'children'),
    Output('tfz_den', 'children'),
    Output('tfz_num', 'children')],
    [Input('pickle_store', 'data'),
     Input('url', 'pathname'),
     Input('command-dropdown_c', 'value')]
)
def key_properties_comma(pickle_file, pathname, selected_command):
    if pathname == '/commands' and pickle_file is not None:
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)
        #loop correspondente
        if not selected_command:
            selected_command = sys.loops[0].commands.name if sys.loops else None
        loop = next((loop for loop in sys.loops if loop.commands.name == selected_command), None)
        if loop is None:
            return ["None"] * 8
        
        refcom = loop.ref_commands.name if loop.ref_commands else None
        rescom = loop.residual_commands.name if loop.residual_commands else None
        mc = loop.modal_coefficients.name if loop.modal_coefficients else None
        wave_corrector = loop.commanded_corrector.uid if loop.commanded_corrector else None
        #acttuators = loop.commanded_corrector.n_valid_actuators if loop.commanded_corrector else None
        valid_act = loop.commanded_corrector.n_valid_actuators if loop.commanded_corrector else None
        tfz_den = loop.commanded_corrector.tfz_den if loop.commanded_corrector else None
        tfz_num = loop.commanded_corrector.tfz_num if loop.commanded_corrector else None
        
        loop, refcom, rescom, mc, wave_corrector, valid_act, tfz_den, tfz_num = none_to_string(loop.uid, refcom, rescom, mc, wave_corrector, valid_act, tfz_den, tfz_num)
        
        print(loop, refcom, rescom, mc, wave_corrector, valid_act, tfz_den, tfz_num)
        return loop, refcom, rescom, mc, wave_corrector, valid_act, tfz_den, tfz_num
    else: 
        return ["None"] * 8
    

    #não sei se estou a extrair corretamente
@callback(
    Output('deformmirror', 'children'),
    [Input('pickle_store', 'data'),
     Input('url', 'pathname'),
     Input('command-dropdown_c', 'value')]
)
def key_extra_comma(pickle_file, pathname, selected_command):
    if pathname == '/commands' and pickle_file is not None:
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)
        #loop correspondente
        if not selected_command:
            selected_command = sys.loops[0].commands.name if sys.loops else None
        loop = next((loop for loop in sys.loops if loop.commands.name == selected_command), None)
        if loop is None:
            return None
        
        #não sei se está correto
        if isinstance(loop.commanded_corrector, aotpy.DeformableMirror):
            dmac = loop.commanded_corrector.actuator_coordinates 
            dms = loop.commanded_corrector.stroke 
            dmac, dms = none_to_string(dmac, dms)
            print(loop.commanded_corrector.uid, dmac, dms)
            return html.Div([
                html.Div([
                    html.Label("Deformable Mirror actuator Coordinates: ", style={'color': 'white'}),
                    html.Div(dmac, style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
            ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

                
                html.Div([
                    html.Label("Deformable Mirror stroke: ", style={'color': 'white'}),
                    html.Div(dms, style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
            ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),
        ])
        else:
            return None

#para a secção dos objetos
@callback(
    Output('telescope_name', 'children'),
     Output('telescope_type', 'children'),
     #Output('detector3_name', 'children'),
     #Output('detector3_type', 'children'),
    #Output('meas3_name', 'children'),
    #Output('meas3_type', 'children')],
    [Input('pickle_store', 'data'),
     Input('url', 'pathname'),
     Input('command-dropdown_c', 'value')]
)
def key_properties_objetcs3(pickle_file, pathname, selected_command):
    if pathname == '/commands' and pickle_file is not None:
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)
        #loop correspondente
        if not selected_command:
            selected_command = sys.loops[0].commands.name if sys.loops else None
        loop = next((loop for loop in sys.loops if loop.commands.name == selected_command), None)
        if loop is None:
            return ["None"] * 2
        
        #source3_name= sensor.source.uid
        #source3_type= type(sensor.source).__name__
        telescope_name= loop.commanded_corrector.telescope.uid
        telescope_type= type(loop.commanded_corrector.telescope).__name__
        #t_name= sensor.measurements.name
        #meas3_type= type(sensor.measurements).__name__
        #source3_name, source3_type, detector3_name, detector3_type, meas3_name, meas3_type = none_to_string(source3_name, source3_type, detector3_name, detector3_type, meas3_name, meas3_type)  
        #print(f" source name: {source3_name}, source type: {source3_type}, meas name: {meas3_name}, meas type: {meas3_type}")
        telescope_name, telescope_type = none_to_string(telescope_name, telescope_type)
        return telescope_name, telescope_type
        #return source3_name, source3_type, detector3_name, detector3_type, meas3_name, meas3_type
    else: 
        return ["None"] * 2


#Imagem com slide
@callback(
    Output('teste2_imagem', 'children'),
    [Input('frame2_slider', 'value'),
     Input('pickle_store', 'data'),
     Input('url', 'pathname'),
     Input('command-dropdown_c', 'value'),
     Input('aotpy_scale_c', 'value'),
     Input('aotpy_color_c', 'value'),
     Input('aotpy_interval_c', 'value'),
     Input('imag2D_com', 'clickData')]
     
)
def update_image(slider_value, pickle_file, pathname, selected_command, scale_type, color_type,interval_type, clickData):
    if pathname == '/commands' and pickle_file is not None:
        ctx = dash.callback_context
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        if not selected_command:
            selected_command = sys.loops[0].commands.name if sys.loops else None

        loop = next((loop for loop in sys.loops if loop.commands.name == selected_command), None)
        if loop is None:
            return {}  
        
        img_data = loop.commands.data

        if not hasattr(loop.commanded_corrector, 'actuator_coordinates') or not loop.commanded_corrector.actuator_coordinates or img_data is None:
            return html.Div("The image cannot be rasterized without the actuator coordinates", style={
                'position': 'absolute',
                'left': '200px',
                'top': '50px',
                'width': '140px'            
            })
        print(loop.commanded_corrector.actuator_coordinates) 
        frame_index = slider_value

        if ctx.triggered and ctx.triggered[0]['prop_id'].split('.')[0] == 'imag2D_com':
        
            x, y, z = extract_coordinates(clickData)
            frame_index = int(x)
        
     
        frame_processed = img_data[frame_index]
        frame_processed = apply_scale(frame_processed, scale_type)
        frame_processed = apply_interval(frame_processed, interval_type)
        
        colormap = apply_colormap(color_type)
        fig = go.Figure(data=go.Heatmap(z=frame_processed.reshape(-1, 1), colorscale=colormap))

        fig.update_layout(
            title=f'Frame {frame_index}',
            xaxis_title='Index',
            yaxis_title='Value',
            autosize=False,
            width=550,
            height=400,
            paper_bgcolor='rgba(0,0,0,0)', 
            title_font=dict(color='white'),  
            xaxis_title_font=dict(color='white'),  
            yaxis_title_font=dict(color='white'),
            xaxis_tickfont=dict(color='white'),  
            yaxis_tickfont=dict(color='white'),
            margin=dict(l=65, r=50, b=65, t=90),
            coloraxis_colorbar=dict(tickfont=dict(color='white')),
        )

        return dcc.Graph(figure=fig, style={
                    'position': 'absolute',
                    'left': '100px',
                    'top': '50px',
                    'height': '30px',
                    'width': '400px'
                })

@callback(
    [Output('frame2_slider', 'max'),
     Output('frame2_slider', 'marks'), 
     Output('frame2_slider', 'value')],
    [Input('pickle_store', 'data'),
     Input('url', 'pathname'),
     Input('command-dropdown_c', 'value')]
)
def update_slider(pickle_file, pathname, selected_command):
    if pathname == '/commands' and pickle_file is not None:
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        if not selected_command:
            selected_command = sys.loops[0].commands.name if sys.loops else None
        loop = next((loop for loop in sys.loops if loop.commands.name == selected_command), None)
        if loop is None:
            return 0, {}, 0  
        
        img_data = loop.commands.data
        max_frame = img_data.shape[0] - 1
        marks = {i: str(i) for i in range(0, max_frame + 1, 1000)}  
        return max_frame, marks, 0
    else:
        return 0, {}, 0
    
#Gráfico

@callback(
    Output('differentplot', 'figure'),
    [Input('pickle_store', 'data'),
     Input('url', 'pathname'),
     Input('imag2D_com','clickData'),
     Input('command-dropdown_c', 'value')]
)
def display_commands_frame(pickle_file, pathname, clickData,selected_command):
    if pathname == '/commands' and pickle_file is not None:
        ctx = dash.callback_context
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        if not selected_command:
            selected_command = sys.loops[0].commands.name if sys.loops else None
        loop = next((loop for loop in sys.loops if loop.commands.name == selected_command), None)
        if loop is None:
            return {}  
        
        cmd_data = loop.commands.data
        
        cmd_data_mean = np.mean(cmd_data, axis=1)
        time_values = list(range(len(cmd_data_mean)))

        time_values, commands_over_time, x,y =[None] *4

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=time_values, y=cmd_data_mean, mode='lines', name='Mean command value'))

        if ctx.triggered and ctx.triggered[0]['prop_id'].split('.')[0] == 'imag2D_com':
           
            x, y, z = extract_coordinates(clickData)
            print(f"im here {x}, {y}, {z}")
            commands_over_time = cmd_data[:,int(y)]

            time_values = list(range(len(commands_over_time)))
         
        fig.add_trace(go.Scatter(x=time_values, y=commands_over_time, mode='lines', name=f'Intensity x={x},y={y}'))
        
        fig.update_layout(
            title='Actuator motion per frame',
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
        
    
#imagem estatica
@callback(
    Output('imag2D_com', 'figure'),
    [Input('pickle_store', 'data'),
     Input('url', 'pathname'),
     Input('command-dropdown_c', 'value')]
)
def display_detector_frame(pickle_file, pathname, selected_command):
    if pathname == '/commands' and pickle_file is not None:
        
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        if not selected_command:
            selected_command = sys.loops[0].commands.name if sys.loops else None
        loop = next((loop for loop in sys.loops if loop.commands.name == selected_command), None)
        if loop is None:
            return {}  
        
        cmd_data = loop.commands.data

      
        swapped = np.swapaxes(cmd_data, 0, 1)

    
        fig = go.Figure(data=go.Heatmap(z=swapped, colorscale='Viridis',colorbar=dict(tickfont=dict(color='white'))))

        fig.update_layout(
            title='Motion per actuator per frame',
            xaxis_title='Frame',
            yaxis_title='Actuator Index',
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