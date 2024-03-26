import dash
from dash import Dash, dcc, html, dash_table, Input, Output, State, callback, register_page
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import base64
import datetime
import io
import aotpy
import gzip


dash.register_page(__name__, path='/pixels')

layout = html.Div([


    html.H1("Pixels", style={'text-align': 'left', 'margin-left': '12vw', 'marginBottom' : '0px'}),


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
        
    #Strings    
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
            html.Div([], style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

    #Floats
        html.Div([
            html.Label("Subapertures Size: ", style={'color': 'white'}),
            html.Div([], style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),

        html.Div([
            html.Label("Altitudes: ", style={'color': 'white'}),
            html.Div([], style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),
   
        html.Div([
            html.Label("Float: ", style={'color': 'white'}),
            html.Div([], style={'background-color': '#243343', 'width': '160px', 'height': '20px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '6px'}),


    ], style={'background-color': '#1C2634', 'color': 'white', 'position': 'absolute', 'left': '160px', 'top': '80px', 'width': '400px', 'height': '390px'}),
    
   #1 quadrante 
    html.Div([
        html.P("Objects", style={'text-align': 'left','margin-left': '1vw'}),
  
    #1 bloco
        html.Div([
            html.P("Source", style={'text-align': 'left', 'margin-left': '1vw'}),
            html.Div([
                html.Label("Name: ", style={'color': 'white'}),
                html.Button("Example_Name", style={'border-radius': '10%', 'border': '1.5px solid blue', 'background-color': '#1C2634', 'color':'white','font-size':'15px', 'width': '150px', 'height': '20px', 'margin-left': '10px'})
            ], style={'display': 'flex', 'align-items': 'center', 'margin-left': '1vw'}),
            html.P("Type: Natural Guide Star", style={'text-align': 'left', 'margin-left': '1vw', 'color': 'white'}),
    ], style={'background-color': '#243343', 'color': 'white', 'display': 'flex', 'flex-direction': 'column', 'width':'200px', 'height': '90px','margin-left': '1vw'}),

    #2 bloco
        html.Div([
            html.P("Detector", style={'text-align': 'left', 'margin-left': '1vw'}),
            html.Div([
                html.Label("Name: ", style={'color': 'white'}),
                html.Button("Other_Name", style={'border-radius': '10%', 'border': '1.5px solid blue', 'background-color': '#1C2634', 'color':'white','font-size':'15px', 'width': '150px', 'height': '20px', 'margin-left': '10px'})
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



    ], style={'background-color': '#1C2634', 'color': 'white', 'position': 'absolute', 'left': '580px', 'top': '80px', 'width': '230px', 'height': '390px'}),
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
   html.Div([  # Container for the checkboxes
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
    'justify-content': 'space-between',  # Space automatic
    'background-color': '#1C2634', 
    'position': 'absolute', 
    'left': '830px', 
    'top': '50px', 
    'width': '430px', 
    'height': '420px'
}),
  
  #3 quadrante
  html.Div([
    html.P("Data", style={'text-align': 'left','margin-left': '1vw'}),
    html.Div([  
        html.Div(  # Placeholder for the graph
            style={
                'background-color': 'grey',
                'width': '200px',  
                'height': '200px'  
            }
        ),
        html.Div('x-axis', style={'color': 'white'}),  # x-axis label
    ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'center'}),
    html.Div('y-axis', style={'color': 'white', 'position': 'absolute', 'top': '50%', 'left': '0'})  # y-axis label
], style={
    'background-color': '#1C2634',  # Corectangulo
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
        html.Div(  # Placeholder for the graph
            style={
                'background-color': 'grey',
                'width': '200px',  
                'height': '200px'  
            }
        ),
        html.Div('x-axis', style={'color': 'white'}),  # x-axis label
    ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'center'}),
    html.Div('y-axis', style={'color': 'white', 'position': 'absolute', 'top': '50%', 'left': '0'})  # y-axis label
], style={
    'background-color': '#1C2634',  # Cor rectangulo
    'position': 'absolute',
    'left': '780px',
    'top': '480px',
    'width': '600px',  
    'height': '300px'  
}),

dcc.Store(id='5-quadrante-content', data=[
    #5quadrante
     html.Div([
    html.P("oi", style={'text-align': 'left','margin-left': '1vw'}),
    html.Div([  
        html.Div( 
            style={
                'background-color': 'grey',
                'width': '200px',  
                'height': '200px'  
            }
        ),
        
    ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'center'}),
    
], style={
    'background-color': '#1C2634',  # Cor rectangulo
    'position': 'absolute',
    'left': '160px',
    'top': '80px',
    'width': '400px',  
    'height': '390px',  
}),
])


], style={'position': 'relative'})
    
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