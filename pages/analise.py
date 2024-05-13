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
                html.Div(id='main_telescope', style={
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
    ], style={'position': 'absolute', 'top': '220px', 'width': '100%'}),


#3parte
html.Div([
        html.Div([
    
        # Primeiro

 html.Div([
            html.Div([
                html.Label('Corresponding Wavefront Sensor', id='sensor_source_div', style={'color': 'white'}),
                html.Div([
                #    html.Label('Measurements: ', style={'color': 'white'}),
                #    dcc.Link(
                #        dbc.Button(id='image_name_ws', style={'background-color':'#1C2634', 'color': 'white','width': '7vw'}),
                #        href='/measurements'
                #            )
            ], style={'display': 'flex', 'flex-direction': 'row', 'align-items': 'center'}),

                #html.Div([
                 #   html.Label('Detector: ', style={'color': 'white'}),
                    #dcc.Link(
                     #   dbc.Button(id='detector_name_ws', style={'background-color':'#1C2634', 'color': 'white','width': '7vw'}),
                     #   href='/pixels'
                  #          )
            #], style={'display': 'flex', 'flex-direction': 'row', 'align-items': 'center'}),
                
    ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start'}),
#                dcc.Link(
#                    dbc.Button('Measurements', id='submit-button', style={'background-color':'#243343', 'color': 'white','margin-left':'2vw', 'width': '10vw'}),
#                    href='/measurements'),
], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'margin-left': '1vw', 'width': '20vw'}),

       # Segundo
       
        
        html.Div([
            html.Div([
                html.Label('Corresponding loops: ', style={'color': 'white'}),
                html.Div(id='verified_loop_container'),
    ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start'}),
 #               dcc.Link(
 #                   dbc.Button('Pixels', id='submit-button', style={'background-color':'#243343', 'color': 'white','margin-left':'2vw', 'width': '10vw'}),
 #                   href='/pixels'),
], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'margin-left': '5vw', 'width': '20vw'}),

#Terceiro

        html.Div([
            html.Div([
                
                html.Label( id='verified_corrector_container', style={'color': 'white'}),
    ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start'}),
    #        dcc.Link(
    #            dbc.Button('Commands', id='submit-button', style={'background-color':'#243343', 'color': 'white','margin-left':'2vw', 'width': '10vw'}),
     #           href='/commands'),
], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center','margin-left': '5vw', 'width': '20vw'}),
    


    ], style={'display': 'flex'}),
], style={'background-color': '#1C2634', 'color': 'white', 'position': 'absolute', 'left': '160px', 'top': '430px', 'width': '1100px', 'height': '200px'}),

    dcc.Store(id='store-atmosphere-params', storage_type='local'),
    html.Div(id='output-atmosphere-params'),
    # html.Div(id='img_data2', style={'color': 'white'}),
    #html.Div(id='mo2', style={'color': 'red'}),
    #html.Div(id='sm2', style={'color': 'blue'}),
    #html.Div(id='ss2', style={'color': 'black'}),


    html.Div(id='just_sensors', style={'display': 'none'}),  # para poder chamar sem ter problemas
    html.Div(id='just_loops', style={'display': 'none'}),
])

#dcc.Store(id='store-atmosphere-params', storage_type='local'),
#returnar dados todos

"""@callback(
    Output('img_data2', 'children'),
    [Input('store-atmosphere-params', 'data'),
     Input('url', 'pathname')]
)
def display_img_data(data, pathname):
    if pathname == '/analise' and data is not None:
        
        img_data = data['np_image_data']
        print(f"recebi {img_data}")
        return img_data
    else: []

@callback(
    Output('sm2', 'children'),
    [Input('store-atmosphere-params', 'data'),
     Input('url', 'pathname')]
)
def display_sm_data(data, pathname):
    if pathname == '/analise' and data is not None:
        
        sm = data['subaperture_mask']
        print(f"recebi {sm}")
        return sm
    else: []

@callback(
    Output('mo2', 'children'),
    [Input('store-atmosphere-params', 'data'),
     Input('url', 'pathname')]
)
def display_ss_data(data, pathname):
    if pathname == '/analise' and data is not None:
        
        mo = data['mask_offsets']
        print(f"recebi {mo}")
        return mo
    else: []

@callback(
    Output('ss2', 'children'),
    [Input('store-atmosphere-params', 'data'),
     Input('url', 'pathname')]
)
def display_ss_data(data, pathname):
    if pathname == '/analise' and data is not None:
        
        ss = data['subaperture_size']
        print(f"recebi {ss}")
        return ss
    else: []"""

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
    Output('main_telescope', 'children'),
    [Input('store-atmosphere-params', 'data'),
     Input('url', 'pathname')]
)
def display_telescope_data(data, pathname):  
    if pathname == '/analise' and data is not None:
        
        main_telescope = data['main_telescope']
        return f'{main_telescope}'
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
    # from .inicial import _sys
    if pathname == '/analise' and data is not None:
        # _sys.wavefront_sensors
        sensors = data['wavefront_sensors']
        sensor_divs = [html.Div(sensor, id=sensor, className='option', n_clicks=0, style=option_STYLE) for sensor in sensors]
        return sensor_divs
    else:
        return []
    


    
@callback(
    [Output('sensor_source_div', 'children'),
     Output('just_sensors', 'children')],
    [Input({'type': 'source-button', 'index': ALL}, 'n_clicks'),
     Input('url', 'pathname')],
    [State('store-atmosphere-params', 'data')]
)
def update_wavefront_sensor_and_display_names(n_clicks, pathname, data):
    if pathname == '/analise' and data is not None:
        ctx = dash.callback_context
        if not ctx.triggered:
            return [], []
        else:
            button_id = ctx.triggered[0]['prop_id'].split('.')[0]
            source_id = json.loads(button_id)['index']
            sensor_sources = data.get('other_sensor_sources')
            if sensor_sources is None:
                return []
            associated_sensors = [sensor for sensor, sources in sensor_sources.items() if source_id in sources]
            
            image_name_dict = data.get('image_name')
            if image_name_dict is None:
                image_name_labels = []
            else:
                image_name_labels = [name for name, sensors in image_name_dict.items() if any(sensor in sensors for sensor in associated_sensors)]

            detector_name_dict = data.get('detector_name')
            if detector_name_dict is None:
                detector_name_labels = []
            else:
                detector_name_labels = [name for name, sensors in detector_name_dict.items() if any(sensor in sensors for sensor in associated_sensors)]

            labels = []
            for i, sensor in enumerate(associated_sensors):
                image_name = image_name_labels[i] if i < len(image_name_labels) else 'N/A'
                detector_name = detector_name_labels[i] if i < len(detector_name_labels) else 'N/A'
                labels.append(
                    html.Div([
                        html.Span(f'Sensor: {sensor}, Measurements: '),
                        dcc.Link(f'{image_name}', href='/measurements'),
                        html.Span(', Detector: '),
                        dcc.Link(f'{detector_name}', href='/pixels'),
                        ], id=f'verified_sensor[{i+1}]', style={'color': 'white'})
            )

            return labels, associated_sensors
    else:
        return [], []
    
#verificar os loops com os wavefront sensor correspondentes:
@callback(
    [Output('verified_loop_container', 'children'),
     Output('just_loops', 'children')],
    [Input('just_sensors', 'children'),
     Input('url', 'pathname')],
    [State('store-atmosphere-params', 'data')]
)
def update_verified_loop(just_sensors, pathname, data):
    if pathname == '/analise' and data is not None:
        ws_loops = data.get('other_WS_loops')
        command_loop_mapping = data.get('command_name')  
        #print(f'commandmapping {command_loop_mapping}')
        if ws_loops is None:
            return None  
        associated_loops = [loop for loop, sensors in ws_loops.items() if any(sensor in sensors['input_sensors'] for sensor in just_sensors)]
        labels = []
        for i, loop in enumerate(associated_loops):
            command = next((cmd for cmd, loops in command_loop_mapping.items() if loop in loops), None)
            labels.append(
                html.Div([
                    html.Span(f'Loop: {loop}, Command: '),
                    dcc.Link(f'{command}', href='/commands'),
            ], id=f'verified_loop[{i+1}]', style={'color': 'white'})
)
        #print(labels)
        return labels, associated_loops
    else:
        return [], []
      

  

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
    
#WAVEFRONT CORRECTORS
@callback(
    Output('verified_corrector_container', 'children'),
    [Input('just_loops', 'children'),
     Input('url', 'pathname')],
    [State('store-atmosphere-params', 'data')]
)
def update_corrector_labels(loops, pathname, data):
    if pathname == '/analise' and data is not None:
        #print(f'loops {loops}')
        other_WC_loops = data.get('other_WC_loops')
        #print(f'other_WC_loops {other_WC_loops}')
        if other_WC_loops is None:
            return []
        labels = []
        for loop, correctors in other_WC_loops.items():
            for corrector in correctors:
                labels.append(html.Label(f'For the Loop {loop}, the corrector is {corrector}.', style={'color': 'white'}))
        #print(labels)
        return labels
    else:
        return []

#@callback(
#    Output('loop_corrector_div', 'children'),
#    [Input({'type': 'loop-button', 'index': ALL}, 'n_clicks')],
#    [State('store-atmosphere-params', 'data')]
#)
#def update_corrector(n_clicks, data):
#    ctx = dash.callback_context
#    if not ctx.triggered or data is None:
#        return None
#    else:
#        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
#        loop_id = json.loads(button_id)['index']
#        corrector = data['other_WC_lopps'][loop_id]
#        return corrector

#Para já não preciso de mostrar os control loops
#@callback(
#    Output('control_loop', 'children'),
#    [Input('store-atmosphere-params', 'data'),
#     Input('url', 'pathname')]
#)
#def display_controloop(data, pathname):
#    if pathname == '/analise' and data is not None:
#        control_loops = data.get('control_loops')
#        if control_loops is None:
#            return []  
#        control_loop_divs = [html.Div(control_loop['uid'], id=control_loop['uid'], className='option', n_clicks=0, style=option_STYLE) for control_loop in control_loops]
#        return control_loop_divs
#    else:
#        return []


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
    

