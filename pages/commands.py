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
    html.H1("Commands", style={'text-align': 'left', 'margin-left': '12vw', 'marginBottom' : '0px'}),

    html.Div([
    dbc.Select(
        id='command-dropdown',
        options=[],
        value=None,
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
            html.Label("Deformable Mirror Coordinates: ", style={'color': 'white'}),
            html.Div([], style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

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
    dcc.Graph(id='teste2_imagem', style={'position': 'absolute', 'left': '20px', 'top': '50px', 'height': '330px', 'width': '500px'}),

    html.Div(dcc.Slider(
                id='frame2_slider',
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
        dcc.Graph(id='differentplot', style={'position': 'absolute', 'left': '20px', 'top': '50px', 'height': '330px', 'width': '500px'}),
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

def none_to_string(*args):
    return ['None' if arg is None or (isinstance(arg, list) and not arg) else arg for arg in args]
    
@callback(
    Output('command-dropdown', 'options'),
    [Input('url', 'pathname')],
    [State('pickle_store', 'data')]
)
def see_commands_loop(pathname, pickle_file):
    if pathname == '/commands' and pickle_file is not None:
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        loops = sys.loops
        commands = [loop.commands for loop in loops if loop.commands is not None]
        options = [{'label': command.name, 'value': command.name} for command in commands]

        return options
    else:
        return []
    

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
     Input('command-dropdown', 'value')]
)
def key_properties_comma(pickle_file, pathname, selected_command):
    if pathname == '/commands' and pickle_file is not None:
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)
        #loop correspondente
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


#Imagem com slide
@callback(
    Output('teste2_imagem', 'figure'),
    [Input('frame2_slider', 'value'),
     Input('pickle_store', 'data'),
     Input('url', 'pathname'),
     Input('command-dropdown', 'value')]
)
def update_image(frame_index, pickle_file, pathname, selected_command):
    if pathname == '/commands' and pickle_file is not None:
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        loop = next((loop for loop in sys.loops if loop.commands.name == selected_command), None)
        if loop is None:
            return {}  
        
        img_data = loop.commands.data
        frame_processed = img_data[frame_index]

      
        fig = go.Figure(data=go.Heatmap(z=frame_processed.reshape(-1, 1), colorscale='Viridis'))

        fig.update_layout(
            title=f'Frame {frame_index} Dimension X',
            xaxis_title='Index',
            yaxis_title='Value',
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
        )

        return fig
    else:
        return {}

@callback(
    [Output('frame2_slider', 'max'),
     Output('frame2_slider', 'marks'), 
     Output('frame2_slider', 'value')],
    [Input('pickle_store', 'data'),
     Input('url', 'pathname'),
     Input('command-dropdown', 'value')]
)
def update_slider(pickle_file, pathname, selected_command):
    if pathname == '/commands' and pickle_file is not None:
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

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
import numpy as np
import plotly.graph_objects as go

@callback(
    Output('differentplot', 'figure'),
    [Input('pickle_store', 'data'),
     Input('url', 'pathname'),
     Input('command-dropdown', 'value')]
)
def display_commands_frame(pickle_file, pathname, selected_command):
    if pathname == '/commands' and pickle_file is not None:
        
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        loop = next((loop for loop in sys.loops if loop.commands.name == selected_command), None)
        if loop is None:
            return {}  
        
        cmd_data = loop.commands.data

        # média
        cmd_data_mean = np.mean(cmd_data, axis=1)

        time_values = list(range(len(cmd_data_mean)))

        fig = go.Figure()

        fig.add_trace(go.Scatter(x=time_values, y=cmd_data_mean, mode='lines', name='Mean command value'))

        fig.update_layout(
            title='Mean command value over time',
            xaxis_title='Time',
            yaxis_title='Mean command value',
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