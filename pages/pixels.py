import dash
from dash import Dash, dcc, html, dash_table, Input, Output, State, callback
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import base64
import datetime
import io
import aotpy
import gzip
import cv2
import dash
from dash import dcc
from dash import html, register_page, callback
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash import callback
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib
#matplotlib.use('Agg')

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


    html.H1("Pixels", style={'text-align': 'left', 'margin-left': '12vw', 'marginBottom' : '0px'}),

#Buttons
    html.Div([
    html.Button('Properties', id='button-1', n_clicks=0, style={'background-color': '#1C2634', 'color': 'white', 'text-align': 'center'},),
    html.Button('Statistics', id='button-2', n_clicks=0, style={'background-color': '#1C2634', 'color': 'white', 'text-align': 'center'},),
    dcc.Store(id='store'),
    html.Div(id='output')

], style={'position': 'absolute', 'left': '160px','display': 'flex', 'justify-content': 'space-between', 'top': '50px', 'width': '20px', 'height': '25px'}),
  
  
   #1 quadrante
    dcc.Store(id='1-quadrante-content', data=[
        html.Div([
            html.P("Properties", style={'text-align': 'left', 'margin-left': '1vw'}),
           
            html.Div([
                html.Label("Name of Detector: ", style={'color': 'white'}),
                html.Div("[[[SAPHIRA", style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),
    
            html.Div([
                html.Label("Shutter Type: ", style={'color': 'white'}),
                html.Div([], style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

            html.Div([
                html.Label("Unique Identifier: ", style={'color': 'white'}),
                html.Div([], style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
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
                html.Label("Number of valid subapertures: ", style={'color': 'white'}),
                html.Div("[]", style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

            html.Div([
                html.Label("Subapertures Size: ", style={'color': 'white'}),
                html.Div("[]", style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
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



    ], style={'background-color': '#1C2634', 'color': 'white', 'position': 'absolute', 'left': '400px', 'top': '30px', 'width': '250px', 'height': '390px'}),
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
    html.Div(id='teste_imagem', style={'position': 'absolute', 'left': '10px', 'top': '50px'}),

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
                    html.Div(id='teste'),
                    style={
                    'background-color': 'grey',
                    'width': '300px',  
                    'height': '150px'  
            }
        ),
        html.Div('Seconds', style={'color': 'white'}),  # x
    ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'center'}),
        html.Div('Pixel index', style={'color': 'white', 'position': 'absolute', 'top': '50%', 'left': '0'})  # y

], style={
    'background-color': '#1C2634',  # Corectangulo
    'position': 'absolute',
    'left': '160px',
    'top': '480px',
    'width': '600px',  
    'height': '250px'  
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
    'left': '780px',
    'top': '480px',
    'width': '550px',  
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
    html.Div(id='img_data'),
    dcc.Store(id='second-atmosphere-params', storage_type='local'),
    html.Div(id='output-atmosphere-params'),
    
   # html.Div(id='teste_imagem', style={'position': 'absolute', 'left': '160px', 'top': '80px', 'width': '400px', 'height': '390px'}),
    html.Div(id='mo', style={'color': 'red'}),
    html.Div(id='sm', style={'color': 'blue'}),
    html.Div(id='ss', style={'color': 'black'}),

], style={'position': 'relative'})
    
#CALLBACKS

@callback(
    Output('teste_imagem', 'children'),
    [Input('second-atmosphere-params', 'data'),
     Input('url', 'pathname')]
)
def display_imgs_data(data, pathname):
    if pathname == '/pixels' and data is not None:
        img_data = data['new']
        # BytesIO object
        buf = io.BytesIO()
        from .inicial import _sys

        # fig = plt.figure()
        # plt.imshow(img_data)
        # plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
        # fig.savefig(buf, format='png', dpi=70)  # dpi-> tamanho
        #img = img_data[25:40]
        fig = px.imshow(_sys.wavefront_sensors[0].detector.pixel_intensities.data, animation_frame=0, binary_string=True, labels=dict(animation_frame="slice"))
        fig.show()

        img_str = base64.b64encode(buf.getvalue()).decode('utf-8')
        return html.Img(src='data:image/png;base64,{}'.format(img_str))
  
    else: 
        return []	


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
    else: []

@callback(
    Output('sm', 'children'),
    [Input('second-atmosphere-params', 'data'),
     Input('url', 'pathname')]
)
def display_sm_data(data, pathname):
    if pathname == '/pixels' and data is not None:
        
        sm = data['subaperture_mask']
        print(f"recebi {sm}")
        return sm
    else: 
        return "None"

@callback(
    Output('mo', 'children'),
    [Input('second-atmosphere-params', 'data'),
     Input('url', 'pathname')]
)
def display_ss_data(data, pathname):
    if pathname == '/pixels' and data is not None:
        
        mo = data['mask_offsets']
        print(f"recebi {mo}")
        return mo
    else: 
        return "None"

@callback(
    Output('ss', 'children'),
    [Input('second-atmosphere-params', 'data'),
     Input('url', 'pathname')]
)
def display_ss_data(data, pathname):
    print(f"entrei aqui")
    if pathname == '/pixels' and data is not None:
        
        ss = data['subaperture_size']
        print(f"recebi {ss}")
        return ss
    else: 
        return "None"

"""
@callback(
    Output('teste', 'children'),
    [Input('mo', 'children'),
     Input('teste_imagem', 'children'),
     Input('ss', 'children'),
     Input('sm', 'children'),
     Input('url', 'pathname')],
    [State('second-atmosphere-params', 'data')])
def display_corrector1(mo, teste_imagem, ss, sm, pathname, data):
    if pathname == '/pixels' and data is not None:
        
        image_data=teste_imagem
        mask_offsets=mo
        subaperture_mask=sm
        subaperture_size = ss


        if subaperture_mask is not None:
            n_rows = subaperture_mask.shape[0]
            n_cols = subaperture_mask.shape[1]
            
        #Criar cópia dos dados da imagem para desenhar a grelha 
            image_with_grid = image_data.copy()

        # Colunas e linhas na grelha
        #n_rows = subaperture_mask.shape[0]
        #n_cols = subaperture_mask.shape[1]

        #grelha
            for i in range(n_rows):
                for j in range(n_cols):
                # canto superior esquerdo 
                    top_left = (mask_offsets[0] + i * subaperture_size, mask_offsets[1] + j * subaperture_size)

                #canto inferior direito
                    bottom_right = (top_left[0] + subaperture_size, top_left[1] + subaperture_size)

                # é uma subaperture válida?
                    if subaperture_mask[i, j] == 1:
                    # desenhar na imagem
                        cv2.rectangle(image_with_grid, top_left, bottom_right, color=(0, 255, 0), thickness=1)
        
            buf = io.BytesIO()

            fig = plt.figure()
            plt.imshow(image_with_grid)
            fig.savefig(buf, format='png')

            
            img_str = base64.b64encode(buf.getvalue()).decode('utf-8')

            return img_str
    
        else:
            return []
    else:
        return []
        """

@callback(
    Output('store', 'data'),
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
    Output('output', 'children'),
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

