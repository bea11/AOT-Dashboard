import dash
from dash import dcc
from dash import html, register_page, callback
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash import callback

#import plotly.graph_objects as go

dash.register_page(__name__, path='/analise')

#para editar cada quadro do AOT:
option_STYLE = {
    'width': '100%',
    'background-color': '#1C2634',
    'color': 'white',
    'cursor': 'pointer',
    'border': '1px solid #243343',
}


layout = html.Div([
    html.H1("Analysis", style={'text-align': 'left', 'margin-left': '12vw'}),
    
#nomes/blocos -Juntar os 2
    #primeiros2
    html.Div([
            html.Div([
                html.Div('System Name:', style={'margin-top': '2vw'}),
                html.A(id='system_name', style={
                    'display': 'inline-block',
                    'width': '150px',
                    'height': '50px',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),
                html.Div('Mode:', style={'margin-top': '1vw'}),
                html.A(id='system_mode', style={
                    'display': 'inline-block',
                    'width': '150px',
                    'height': '50px',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),

            ], style={'position': 'absolute', 'margin-left': '12vw'}),

]),
    #segundos2
    html.Div([
            html.Div([
                html.Div('Beginning date:', style={'margin-top': '2vw'}),
                html.A(id='beginning-date', style={
                    'display': 'inline-block',
                    'width': '150px',
                    'height': '50px',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),
                html.Div('End date:', style={'margin-top': '1vw'}),
                html.A(id='end-date', style={
                    'display': 'inline-block',
                    'width': '150px',
                    'height': '50px',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),

            ], style={'position': 'absolute', 'margin-left': '26vw'}),

]),
#terceiros2
    html.Div([
            html.Div([
                html.Div('Strehl Ratio:', style={'margin-top': '2vw'}),
                html.A(id='ratio', style={
                    'display': 'inline-block',
                    'width': '150px',
                    'height': '50px',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),
                html.Div('Strehl Wavelength:', style={'margin-top': '1vw'}),
                html.A(id = 'wavelength', style={
                    'display': 'inline-block',
                    'width': '150px',
                    'height': '50px',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),

            ], style={'position': 'absolute', 'margin-left': '40vw'}),

]),

#quartos2
    html.Div([
            html.Div([
                html.Div('Config:', style={'margin-top': '2vw'}),
                html.A(id='config', style={
                    'display': 'inline-block',
                    'width': '150px',
                    'height': '50px',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),
               

            ], style={'position': 'absolute', 'margin-left': '54vw'}),


    #importante quando quero variar entre estados
    html.Button('Source', id='source'),

]),



    #esquema AO
    html.Div([
        html.H3("AO System", style={'text-align': 'center', 'text-decoration': 'underline', 'text-decoration-color': '#C17FEF', 'margin-bottom': '1vw'}),

#SOURCES
        html.Div([
           html.Div([
                html.Div(id='output_container'),
                html.Div('Sources', style={'margin-left':'12vw'}),
                html.Div(id='source_divs', style={
                    'width': "15vw",
                    'height': '100px',
                    'overflowY': 'scroll',
                    'backgroundColor': '#1C2634',
                    'color': 'white',
                    'margin-left': '12vw'
            }),
        ]),
#WAVEFRONT SENSORS
        html.Div([
                html.Div(id='output_container'),
                html.Div('Wavefront Sensors', style={'margin-left':'2vw'}),
                html.Div(id='sensor_divs', style={
                'width': "15vw",
                'height': '100px',
                'overflowY': 'scroll',
                'backgroundColor': '#1C2634',
                'color': 'white',
                'margin-left': '2vw'
            }),
        ]),
#WAVEFRONT CORRECTORS        
        html.Div([
                html.Div(id='output_container'),
                html.Div('Wavefront Correctors', style={'margin-left':'2vw'}),
                html.Div(id='corrector_divs', style={
                'width': "15vw",
                'height': '100px',
                'overflowY': 'scroll',
                'backgroundColor': '#1C2634',
                'color': 'white',
                'margin-left': '2vw'
            }),
        ]),
#LOOPS
        html.Div([
                html.Div(id='output_container'),
                html.Div('Loops ', style={'margin-left':'2vw'}),
                html.Div(id='loop_divs', style={
                'width': "15vw",
                'height': '100px',
                'overflowY': 'scroll',
                'backgroundColor': '#1C2634',
                'color': 'white',
                'margin-left': '2vw'
            }),
        ]),
#ATMOSPHERE PARAMETERS
        html.Div([
                html.Div(id='output_container'),
                html.Div('Atmosphere Parameters ', style={'margin-left':'2vw'}),
                html.Div(id='atm_divs', style={
                'width': "15vw",
                'height': '100px',
                'overflowY': 'scroll',
                'backgroundColor': '#1C2634',
                'color': 'white',
                'margin-left': '2vw'
            }),
        ]),

        
        ], style={'display': 'flex', 'justifyContent': 'flex-start', 'flexWrap': 'wrap'}),
    ], style={'position': 'absolute', 'top': '270px', 'width': '100%'}),


#3parte
html.Div([
        html.P("Images", style={'text-align': 'left', 'margin-left': '1vw'}),
        html.Div([
    
        # Primeiro
        html.Div([
            html.Div([
                html.Label("Name: ", style={'color': 'white'}),
                html.Label("Dimensions: ", style={'color': 'white'}),
                html.Label("Type: ", style={'color': 'white'}),
                html.Label("Unit: ", style={'color': 'white'}),
                html.Label("Metadata ", style={'color': 'white'}),
    ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start'}),
                dcc.Link(
                    dbc.Button('Pixels', id='submit-button', style={'background-color':'#243343', 'color': 'white','margin-left':'2vw', 'width': '10vw'}),
                    href='/pixels'),
], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'margin-left': '1vw'}),
       # Segundo
        html.Div([
            html.Div([
                html.Label("Name:", style={'color': 'white'}),
                html.Label("Dimensions: ", style={'color': 'white'}),
                html.Label("Type: ", style={'color': 'white'}),
                html.Label("Unit: ", style={'color': 'white'}),
                html.Label("Metadata ", style={'color': 'white'}),
    ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start'}),
                dcc.Link(
                    dbc.Button('Measurements', id='submit-button', style={'background-color':'#243343', 'color': 'white','margin-left':'2vw', 'width': '10vw'}),
                    href='/measurements'),
], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'margin-left': '10vw'}),
       # Terceiro
        html.Div([
            html.Div([
                html.Label("Name: ", style={'color': 'white'}),
                html.Label("Dimensions: ", style={'color': 'white'}),
                html.Label("Type: ", style={'color': 'white'}),
                html.Label("Unit: ", style={'color': 'white'}),
                html.Label("Metadata ", style={'color': 'white'}),
    ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start'}),
            dcc.Link(
                dbc.Button('Commands', id='submit-button', style={'background-color':'#243343', 'color': 'white','margin-left':'2vw', 'width': '10vw'}),
                href='/commands'),
], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'margin-left': '10vw'}),
    
    ], style={'display': 'flex'}),
], style={'background-color': '#1C2634', 'color': 'white', 'position': 'absolute', 'left': '160px', 'top': '460px', 'width': '1100px', 'height': '160px'}),

    dcc.Store(id='store-atmosphere-params'),
    html.Div(id='output-atmosphere-params'),
])


#returnar dados todos
@callback(
    Output('beginning-date', 'children'),
    [Input('store-atmosphere-params', 'data')]
)
def display_beginning_date(data):
    if data is not None:
        
        beginning_date = data['date_beginning']
        return f'{beginning_date}'
    else:
        return ''
    
@callback(
    Output('end-date', 'children'),
    [Input('store-atmosphere-params', 'data')]
)
def display_end_date(data):
    if data is not None:
        
        end_date = data['date_end']
        return f'{end_date}'
    else:
        return ''
    
@callback(
    Output('config', 'children'),
    [Input('store-atmosphere-params', 'data')]
)
def display_end_date(data):
    if data is not None:
        
        config = data['config']
        return f'{config}'
    else:
        return ''
    
@callback(
    Output('ratio', 'children'),
    [Input('store-atmosphere-params', 'data')]
)
def display_end_date(data):
    if data is not None:
        
        ratio = data['ratio']
        return f'{ratio}'
    else:
        return ''

@callback(
    Output('system_name', 'children'),
    [Input('store-atmosphere-params', 'data')]
)
def display_end_date(data):
    if data is not None:
        
        system_name = data['system_name']
        return f'{system_name}'
    else:
        return ''

@callback(
    Output('system_mode', 'children'),
    [Input('store-atmosphere-params', 'data')]
)
def display_end_date(data):
    if data is not None:
        
        system_mode = data['system_mode']
        return f'{system_mode}'
    else:
        return ''


@callback(
    Output('source_divs', 'children'),
    [Input('store-atmosphere-params', 'data')]
)
def display_sources(data):
    if data is not None:       
        sources = data['sources']
        #lista
        source_divs = [html.Div(source['uid'], id=source['uid'], className='option', n_clicks=0, style=option_STYLE) for source in sources]
        return source_divs
    else:
        return []
    

@callback(
    Output('loop_divs', 'children'),
    [Input('store-atmosphere-params', 'data')]
)
def display_sources(data):
    if data is not None:       
        loops = data['loops']
        #lista
        loop_divs = [html.Div(loop['uid'], id=loop['uid'], className='option', n_clicks=0, style=option_STYLE) for loop in loops]
        return loop_divs
    else:
        return []
    
@callback(
    Output('sensor_divs', 'children'),
    [Input('store-atmosphere-params', 'data')]
)
def display_sensor(data):
    if data is not None:
        sensors = data['wavefront_sensors']
        sensor_divs = [html.Div(source['uid'], id=source['uid'], className='option', n_clicks=0, style=option_STYLE) for source in sensors]
        return sensor_divs
    else:
        return []
    
@callback(
    Output('corrector_divs', 'children'),
    [Input('store-atmosphere-params', 'data')]
)
def display_corrector(data):
    if data is not None:
        correctors = data['wavefront_correctors']
        corrector_divs = [html.Div(corrector['uid'], id=corrector['uid'], className='option', n_clicks=0, style=option_STYLE) for corrector in correctors]
        return corrector_divs
    else:
        return []
    
@callback(
    Output('atm_divs', 'children'),
    [Input('store-atmosphere-params', 'data')]
)
def display_corrector(data):
    if data is not None:
        atmosphere = data['atmosphere_params']
        atm_divs = [html.Div(atm['uid'], id=atm['uid'], className='option', n_clicks=0, style=option_STYLE) for atm in atmosphere]
        return atm_divs
    else:
        return []
    

