import dash
from dash import dcc
from dash import html, register_page, callback
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash import callback
import json
from dash.dependencies import Input, Output, State, ALL

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
            
                html.Div('System Name:', style={'margin-top': '2vw'}),
                html.A(id='system_name', style={
                    'display': 'inline-block',
                    'width': '150px',
                    'height': '50px',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),

            ], style={'position': 'absolute', 'margin-left': '12vw'}),

html.Div([
                html.Div('Mode:', style={'margin-top': '2vw'}),
                html.A(id='system_mode', style={
                    'display': 'inline-block',
                    'width': '150px',
                    'height': '50px',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),
                 ], style={'position': 'absolute', 'margin-left': '26vw'}),

    #segundos2
    
            html.Div([
                html.Div('Beginning date:', style={'margin-top': '2vw'}),
                html.A(id='beginning-date', style={
                    'display': 'inline-block',
                    'width': '150px',
                    'height': '50px',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),

            ], style={'position': 'absolute', 'margin-left': '40vw'}),



    html.Div([
                html.Div('End date:', style={'margin-top': '2vw'}),
                html.A(id='end-date', style={
                    'display': 'inline-block',
                    'width': '150px',
                    'height': '50px',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),
                 ], style={'position': 'absolute', 'margin-left': '54vw'}),
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
                #html.Div('Strehl Wavelength:', style={'margin-top': '1vw'}),
                #html.A(id = 'wavelength', style={
                #    'display': 'inline-block',
                #    'width': '150px',
                #    'height': '50px',
                #    'background-color': '#1C2634',
                #    'margin-top': '0vw'
                #}),

            ], style={'position': 'absolute', 'margin-left': '68vw'}),

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
               

            ], style={'position': 'absolute', 'margin-left': '82vw'}),


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
                html.Div(id='source_divs1',n_clicks=0, style={
                    'width': "12vw",
                    'height': '90px',
                    'overflowY': 'scroll',
                    'backgroundColor': '#1C2634',
                    'color': 'white',
                    'margin-left': '12vw'
            }),
        ]),

#Main Telescope
           html.Div([
                html.Div(id='output_container'),
                html.Div('Main Telescope', style={'margin-left':'2vw'}),
                html.Div('AAA', style={
                    'width': "10vw",
                    'height': '50px',
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
                'width': "12vw",
                'height': '90px',
                'overflowY': 'scroll',
                'backgroundColor': '#1C2634',
                'color': 'white',
                'margin-left': '2vw'
            }),
        ]),

#WAVEFRONT SENSORS
        html.Div([
                html.Div(id='output_container'),
                html.Div('Wavefront Sensors', style={'margin-left':'2vw'}),
                html.Div(id='sensor_divs1', style={
                'width': "12vw",
                'height': '90px',
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
                'width': "12vw",
                'height': '90px',
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
                html.Div(id='corrector_divs1', style={
                'width': "12vw",
                'height': '90px',
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
        html.Div([
    
        # Primeiro
        html.Div([
            html.Div([
                html.P("1 Tabela hierarquia", style={'text-align': 'left'}),
                html.Label("Dimensions: ", style={'color': 'white'}),
                html.Label("Type: ", style={'color': 'white'}),
              
    ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start'}),
 #               dcc.Link(
 #                   dbc.Button('Pixels', id='submit-button', style={'background-color':'#243343', 'color': 'white','margin-left':'2vw', 'width': '10vw'}),
 #                   href='/pixels'),
], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'margin-left': '1vw'}),
       # Segundo
        html.Div([
            html.Div([
                html.P("2 Tabela hierarquia", style={'text-align': 'left'}),
                html.Label(id='sensor_source_div', style={'color': 'white'}),
                html.Label("Dimensions: ", style={'color': 'white'}),
                
    ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start'}),
#                dcc.Link(
#                    dbc.Button('Measurements', id='submit-button', style={'background-color':'#243343', 'color': 'white','margin-left':'2vw', 'width': '10vw'}),
#                    href='/measurements'),
], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'margin-left': '20vw'}),
       # Terceiro
        html.Div([
            html.Div([
                html.P("3 Tabela hierarquia", style={'text-align': 'left'}),
                html.Label( id='loop_corrector_div', style={'color': 'white'}),
                html.Label("mas", style={'color': 'white'}),
    ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start'}),
    #        dcc.Link(
    #            dbc.Button('Commands', id='submit-button', style={'background-color':'#243343', 'color': 'white','margin-left':'2vw', 'width': '10vw'}),
     #           href='/commands'),
], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'margin-left': '20vw'}),
    
    ], style={'display': 'flex'}),
], style={'background-color': '#1C2634', 'color': 'white', 'position': 'absolute', 'left': '160px', 'top': '460px', 'width': '1100px', 'height': '160px'}),

    dcc.Store(id='store-atmosphere-params', storage_type='local'),
    html.Div(id='output-atmosphere-params'),
])

#dcc.Store(id='store-atmosphere-params', storage_type='local'),
#returnar dados todos
@callback(
    Output('beginning-date', 'children'),
    [Input('store-atmosphere-params', 'data'),
    Input('url', 'pathname')]
)
def display_beginning_date(data, pathname):
    if pathname == '/analise' and data is not None:
        
        beginning_date = data['date_beginning']
        return f'{beginning_date}'
    else:
        return ''
    
@callback(
    Output('end-date', 'children'),
    [Input('store-atmosphere-params', 'data'),
    Input('url', 'pathname')]
)
def display_end_date(data, pathname):  
    if pathname == '/analise' and data is not None:
        
        end_date = data['date_end']
        return f'{end_date}'
    else:
        return ''
    
@callback(
    Output('config', 'children'),
    [Input('store-atmosphere-params', 'data'),
    Input('url', 'pathname')]
)
def display_config_data(data, pathname):  
    if pathname == '/analise' and data is not None:
        
        config = data['config']
        return f'{config}'
    else:
        return ''
    
@callback(
    Output('ratio', 'children'),
    [Input('store-atmosphere-params', 'data'),
     Input('url', 'pathname')]
)
def display_ratio_data(data, pathname):  
    if pathname == '/analise' and data is not None:
        
        ratio = data['ratio']
        return f'{ratio}'
    else:
        return ''

@callback(
    Output('system_name', 'children'),
    [Input('store-atmosphere-params', 'data'),
     Input('url', 'pathname')]
)
def display_name_data(data, pathname):  
    if pathname == '/analise' and data is not None:
        
        system_name = data['system_name']
        return f'{system_name}'
    else:
        return ''

@callback(
    Output('system_mode', 'children'),
    [Input('store-atmosphere-params', 'data'),
     Input('url', 'pathname')]
)
def display_mode_data(data, pathname):
    if pathname == '/analise' and data is not None:
        
        system_mode = data['system_mode']
        return f'{system_mode}'
    else:
        return ''

#Main Telescope
#@callback(
#    Output('main_telescope1', 'children'),
#    [Input('store-atmosphere-params', 'data')]
#)
#def display_main_data(data):
#    if data is not None:
#        main_telescope = data
#        main_telescope_dict = html.Div(main_telescope['uid'], id=main_telescope['uid'], className='option', n_clicks=0, style=option_STYLE)
#        return [main_telescope_dict]
#    else:
#        return []

#SOURCES

@callback(
    Output('source_divs1', 'children'),
    [Input('store-atmosphere-params', 'data'),
     Input('url', 'pathname')]
)
def display_sources1(data, pathname):
    if pathname == '/analise' and data is not None:       
        sources = data['sources']
        #lista
        source_divs = [html.Button(source['uid'], id={'type': 'source-button', 'index': source['uid']}, className='option', n_clicks=0, style=option_STYLE) for source in sources]
        return source_divs
    else:
        return []


#WAVEFRONT SENSORS
@callback(
    Output('sensor_divs1', 'children'),
    [Input('store-atmosphere-params', 'data'),
     Input('url', 'pathname')]
)
def display_sensor1(data, pathname):
    if pathname == '/analise' and data is not None:
        sensors = data['wavefront_sensors']
        sensor_divs = [html.Div(sensor['uid'], id=sensor['uid'], className='option', n_clicks=0, style=option_STYLE) for sensor in sensors]
        return sensor_divs
    else:
        return []

    
@callback(
    Output('sensor_source_div', 'children'),
    [Input({'type': 'source-button', 'index': ALL}, 'n_clicks')],
    [State('store-atmosphere-params', 'data')]
)
def update_wavefront_corrector(n_clicks, data):
    ctx = dash.callback_context
    if not ctx.triggered or data is None:
        return None
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        source_id = json.loads(button_id)['index']
        sensor_sources = data['other_sensor_sources']
        associated_sensors = [sensor for sensor, sources in sensor_sources.items() if source_id in sources]
        return associated_sensors
      
  

#LOOPS

@callback(
    Output('loop_divs', 'children'),
    [Input('store-atmosphere-params', 'data'),
     Input('url', 'pathname')]
)
def display_loop(data, pathname):
    if pathname == '/analise' and data is not None:       
        loops2 = data['loops2']
        loop_buttons = [html.Button(loop['uid'], id={'type': 'loop-button', 'index': loop['uid']}, className='option', n_clicks=0, style=option_STYLE) for loop in loops2]
        return loop_buttons
    else:
        return []

@callback(
    Output('loop_corrector_div', 'children'),
    [Input({'type': 'loop-button', 'index': ALL}, 'n_clicks')],
    [State('store-atmosphere-params', 'data')]
)
def update_corrector(n_clicks, data):
    ctx = dash.callback_context
    if not ctx.triggered or data is None:
        return None
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        loop_id = json.loads(button_id)['index']
        corrector = data['other_WC_lopps'][loop_id]
        return corrector




#WAVEFRONT CORRECTORS

@callback(
    Output('corrector_divs1', 'children'),
    [Input('store-atmosphere-params', 'data'),
     Input('url', 'pathname')]
)
def display_corrector1(data, pathname):
    if pathname == '/analise' and data is not None:
        correctors = data['wavefront_correctors']
        corrector_divs = [html.Div(corrector['uid'], id=corrector['uid'], className='option', n_clicks=0, style=option_STYLE) for corrector in correctors]
        return corrector_divs
    else:
        return []

#@callback(
#    Output('corrector_divs2', 'children'),
#    [Input('store-atmosphere-params', 'data')]
#)
#def display_corrector2(data):
#    if data is not None:
#        correctors = data['wavefront_correctors']
#        corrector_divs = [html.Div(corrector['uid'], id=corrector['uid'], className='option', n_clicks=0, style=option_STYLE) for corrector in correctors]
#        return corrector_divs
#    else:
#        return []
    
@callback(
    Output('atm_divs', 'children'),
    [Input('store-atmosphere-params', 'data'),
     Input('url', 'pathname')]
)
def display_atm(data, pathname):
    if pathname == '/analise' and data is not None:
        atmosphere = data['atmosphere_params']
        atm_divs = [html.Div(atm['uid'], id=atm['uid'], className='option', n_clicks=0, style=option_STYLE) for atm in atmosphere]
        return atm_divs
    else:
        return []
    

