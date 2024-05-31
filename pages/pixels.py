import dash
from dash import Dash, dcc, html, dash_table, Input, Output, State, callback
import plotly.io as pio
import base64
import datetime
import io
import aotpy
import gzip
import cv2
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

import json
from dash.dependencies import Input, Output, State, ALL



dash.register_page(__name__, path='/pixels')

option_STYLE = {
    'width': '100%',
    'background-color': '#1C2634',
    'color': 'white',
    'cursor': 'pointer',
    'border': '1px solid #243343',
}

layout = html.Div([


    html.H1("Pixels", style={'text-align': 'left', 'margin-left': '8vw', 'marginBottom' : '0px'}),

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
                html.Label("Unique Identifier: ", style={'color': 'white'}),
                html.Div(id='detect_ui', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),
     
            html.Div([
                html.Label("Subaperture Mask: ", style={'color': 'white'}),
                html.Div(id='sm', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px', 'margin-top': '13px'}),

            html.Div([
                html.Label("Mask Ofset: ", style={'color': 'white'}),
                html.Div(id='mo', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

            html.Div([
                html.Label("Other: ", style={'color': 'white'}),
                html.Div([], style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

            html.Div([
                html.Label("Subapertures Size: ", style={'color': 'white'}),
                html.Div(id='ss', style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

            html.Div([
                html.Label("Altitudes: ", style={'color': 'white'}),
                html.Div([], style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),
   
            html.Div([
                html.Label("Float: ", style={'color': 'white'}),
                html.Div([], style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
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



    ], style={'background-color': '#1C2634', 'color': 'white', 'position': 'absolute', 'left': '310px', 'top': '30px', 'width': '280px', 'height': '390px'}),
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
    dcc.Graph(id='teste_imagem', style={'position': 'absolute', 'left': '20px', 'top': '50px', 'height': '330px', 'width': '500px'}),

        html.Div([  
            html.Label([
            "flat_field",
            dbc.Checkbox(id='checkbox-1', className='custom-checkbox')
    ], style={'display': 'flex', 'align-items': 'center'}),
    
            html.Label([
            "dark",
            dbc.Checkbox(id='checkbox-2', className='custom-checkbox')
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
    'left': '50px',
    'top': '480px',
    'width': '630px',  
    'height': '400px'  
}),
 #'left': '160px', 'top': '80px', 'width': '400px', 'height': '390px'
 
    #4 quadrante
        html.Div([
            html.P("Graphics", style={'text-align': 'left','margin-left': '1vw'}),
            html.Div([  
                html.Div(  # graph
                    style={
                    'background-color': '#243343',
                    'width': '400px',  
                    'height': '160px'  
            }
        ),
        html.Div('Time', style={'color': 'white'}),  
    ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'center'}),
        html.Div('Density', style={'color': 'white', 'position': 'absolute', 'top': '50%', 'left': '0'}) 

], style={
    'background-color': '#1C2634',  # Cor rectangulo
    'position': 'absolute',
    'left': '700px',
    'top': '580px',
    'width': '600px',  
    'height': '250px'  
}),

#5quadrante
    dcc.Store(id='5-quadrante-content', data=[
    
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
    'width': '650px',  
    'height': '390px',  
}),
]),

    #html.Div(id='img_data'),
    dcc.Store(id='pickle_store', storage_type='local'),
    html.Div(id='output-atmosphere-params'),
    
    
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
    Output('imag2D', 'figure'),
    [Input('pickle_store', 'data'),
     Input('url', 'pathname')]
)
def display_detector_frame(pickle_file, pathname):
    if pathname == '/pixels' and pickle_file is not None:
        
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        pixel_data = sys.wavefront_sensors[0].detector.pixel_intensities.data

        # poder ter uma imagem 2D por tempo
        reshaped = pixel_data.reshape(pixel_data.shape[0], -1)
        swapped = np.swapaxes(reshaped, 0, 1)

        # Criar com o timeslider
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

@callback(
    Output('teste_imagem', 'figure'),
    [Input('pickle_store', 'data'),
     Input('url', 'pathname')]
)
def display_imgs_data(pickle_file, pathname):
    if pathname == '/pixels' and pickle_file is not None:
    
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        img_data = sys.wavefront_sensors[0].detector.pixel_intensities.data
        print(f"Data PIXEL shape: {img_data.shape}, Data type: {type(img_data)}")
 
        fig = px.imshow(img_data, animation_frame=0, binary_string=True, labels=dict(animation_frame="slice"))
        fig.update_layout(
            title='Different 2D images over frames',
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



"""@callback(
    Output('selected_slice', 'figure'),
    [Input('pickle_store', 'data'),
     Input('url', 'pathname'),
     Input('slice-selector', 'value')]
)
def update_2d_graph(pickle_file, pathname, selected_slice):
    if pathname == '/pixels' and pickle_file and selected_slice is not None:
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)
 
        img_data = sys.wavefront_sensors[0].detector.pixel_intensities.data
        
        num_frames, rows, cols = img_data.shape
        img_data_1d = img_data.reshape(num_frames, rows * cols)
        
        selected_slice_data = img_data_1d[:, selected_slice]
        
        selected_slice_2d = selected_slice_data.reshape(num_frames, 1)
        
        fig = px.imshow(selected_slice_2d.T, aspect='auto', color_continuous_scale='gray')
        fig.update_layout(
            xaxis_title="Time (Frames)",
            yaxis_title="Pixel Intensity",
            coloraxis_showscale=False
        )
        return fig
    return {}"""



@callback(
    [Output('sm', 'children'),
    Output('mo', 'children'),
    Output('ss', 'children')],
    [Input('pickle_store', 'data'),
     Input('url', 'pathname')]
)
def key_properties(pickle_file, pathname):
    if pathname == '/pixels' and pickle_file is not None:
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)
        
        sm = sys.wavefront_sensors[0].subaperture_mask
        mo = sys.wavefront_sensors[0].mask_offsets
        ss = sys.wavefront_sensors[0].subaperture_size

        return sm, mo, ss
    else: 
        return "None", "None", "None"

@callback(
    [Output('name_ns', 'children'),
    Output('detect_ui', 'children'),
    Output('shuttert', 'children')],
    [Input('pickle_store', 'data'),
     Input('url', 'pathname')]
)
def key_properties_2(pickle_file, pathname):
    if pathname == '/pixels' and pickle_file is not None:
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)
        
        detect_ui = sys.wavefront_sensors[0].uid
        name_ns = sys.wavefront_sensors[0].detector.uid
        shuttert = sys.wavefront_sensors[0].detector.shutter_type 

        return name_ns, detect_ui, shuttert
    else: 
        return "None", "None", "None"

