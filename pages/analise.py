import dash
from dash import dcc
from dash import html, register_page, callback
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash import callback
import pickle
from flask import session
import json
import aotpy
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
    html.H1("Information", style={'text-align': 'left', 'margin-left': '12vw'}),
    
#nomes/blocos -Juntar os 2
    #primeiros2
    html.Div([
            
                html.Div('System Name:', style={'margin-top': '2vw'}),
                html.A(id='system_name', style={
                    'display': 'inline-block',
                    'width': '170px',
                    'height': '50px',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),

            ], style={'position': 'absolute', 'margin-left': '8vw'}),

html.Div([
                html.Div('Mode:', style={'margin-top': '2vw'}),
                html.A(id='system_mode', style={
                    'display': 'inline-block',
                    'width': '170px',
                    'height': '50px',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),
                 ], style={'position': 'absolute', 'margin-left': '23vw'}),

    #segundos2
    
            html.Div([
                html.Div('Beginning date:', style={'margin-top': '2vw'}),
                html.A(id='beginning-date', style={
                    'display': 'inline-block',
                    'width': '170px',
                    'height': '50px',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),

            ], style={'position': 'absolute', 'margin-left': '37vw'}),



    html.Div([
                html.Div('End date:', style={'margin-top': '2vw'}),
                html.A(id='end-date', style={
                    'display': 'inline-block',
                    'width': '170px',
                    'height': '50px',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),
                 ], style={'position': 'absolute', 'margin-left': '51vw'}),
#terceiros2
    html.Div([
            html.Div([
                html.Div('Strehl Ratio:', style={'margin-top': '2vw'}),
                html.A(id='ratio', style={
                    'display': 'inline-block',
                    'width': '170px',
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

            ], style={'position': 'absolute', 'margin-left': '65vw'}),

]),

#quartos2
    html.Div([
            html.Div([
                html.Div('Config:', style={'margin-top': '2vw'}),
                html.A(id='config', style={
                    'display': 'inline-block',
                    'width': '170px',
                    'height': '50px',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),
               

            ], style={'position': 'absolute', 'margin-left': '79vw'}),


    #importante quando quero variar entre estados
    #html.Button('Source', id='source'),

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
                    'margin-left': '8vw'
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
], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'margin-left': '5vw', 'width': '23vw'}),

#Terceiro

        html.Div([
            html.Div([
                
                html.Label( id='verified_corrector_container', style={'color': 'white'}),
    ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start'}),
    #        dcc.Link(
    #            dbc.Button('Commands', id='submit-button', style={'background-color':'#243343', 'color': 'white','margin-left':'2vw', 'width': '10vw'}),
     #           href='/commands'),
], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center','margin-left': '5vw', 'width': '25vw'}),
    


    ], style={'display': 'flex'}),
], style={'background-color': '#1C2634', 'color': 'white', 'position': 'absolute', 'left': '110px', 'top': '430px', 'width': '1500px', 'height': '200px'}),

    dcc.Store(id='pickle_store', storage_type='local'),
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

#Funções

def source_to_dict(source):
    return {
        'uid': source.uid,
        'right_ascension': source.right_ascension,
        'declination': source.declination,
        'elevation_offset': source.elevation_offset,
        'azimuth_offset': source.azimuth_offset,
        'width': source.width
    }

def wavefront_sensors_to_dict(wavefront_sensor):
    return {
        'uid': wavefront_sensor.uid,
        'n_valid_subapertures': wavefront_sensor.n_valid_subapertures,
        'subaperture_size': wavefront_sensor.subaperture_size,
        'wavelength': wavefront_sensor.wavelength,
    }

def create_dict_ws(sys):
    e = {}
    for wavefront_sensor in sys.wavefront_sensors:
        if wavefront_sensor.uid not in e:
            e[wavefront_sensor.uid] = []
        e[wavefront_sensor.uid].append(wavefront_sensor.source.uid)
    print(f"e:{e} type :{type(e)}")
    return e


def create_dict_image(sys):
    f = {}
    for wavefront_sensor in sys.wavefront_sensors:
        if wavefront_sensor.measurements is not None:
            image_name = wavefront_sensor.measurements.name
            if image_name not in f:
                f[image_name] = []
            f[image_name].append(wavefront_sensor.uid)
    print(f"f: {f} type: {type(f)}")
    return f

#wavefront sensors dos loops -> eu ao certificar me que são control loops uso a instancia da função input_sensor
def create_dict_wc(sys):
    k = {}
    for loop in sys.loops:
        if isinstance(loop, aotpy.core.loop.ControlLoop):
            if loop.uid not in k:
                k[loop.uid] = {'input_sensors': []}
            k[loop.uid]['input_sensors'].append(loop.input_sensor.uid)
    print(f"k: {k}, type: {type(k)}")        
    return k

#comandos dos loops
def create_dict_command(sys):
    l = {}
    for loop in sys.loops:
        if loop.commands is not None:
            command_name = loop.commands.name
            if command_name not in l:
                l[command_name] = []
            l[command_name].append(loop.uid)
    print(f"l: {l} type: {type(l)}")
    return l

#detetores
def create_dict_detector(sys):
    h = {}
    for wavefront_sensor in sys.wavefront_sensors:
        if wavefront_sensor.detector is not None:
            detector_name = wavefront_sensor.detector.uid
            if detector_name not in h:
                h[detector_name] = []
            h[detector_name].append(wavefront_sensor.uid)
    print(f"h: {h} type: {type(h)}")
    return h

#LOOP
def loop_to_dict(loop):
    return {
        'uid': loop.uid, 
        'commands':loop.commands.name if loop.commands is not None else None,
    }

#correctores dos loops
def create_dict_lp(sys):
    d = {}
    for loop in sys.loops:
        #print(f"loop: {loop}, type: {type(loop)}")
        if loop.uid not in d:
            d[loop.uid] = []
        d[loop.uid].append(loop.commanded_corrector.uid)
        print(f"d: {d}, type: {type(d)}")
    return d

def wavefront_correctors_to_dict(wavefront_corrector):
    return {
        'uid': wavefront_corrector.uid,
    }

def atmosphere_params_to_dict(atmosphere_param):
    return {
        'uid': atmosphere_param.uid,
    }

#@callback(
#    Output('beginning-date', 'children'),
#    [Input('store-atmosphere-params', 'data'),
#    Input('url', 'pathname')]
#)
#def display_beginning_date(data, pathname):
#    if pathname == '/analise' and data is not None:
        
#        beginning_date = data['date_beginning']
#        return f'{beginning_date}'
#    else:
#        return ''   

#Callbacks    

@callback(
    Output('beginning-date', 'children'),
    Input('pickle_store', 'data'),
    Input('url', 'pathname')
)
def display_beg_data(pickle_file, pathname):
    if pathname == '/analise' and pickle_file is not None:
        #pickle file
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        date_beginning = sys.date_beginning
        #print(f"date_beginning: {date_beginning}")
        return f"{date_beginning}"
        
    else:
        return ''
    
@callback(
    Output('end-date', 'children'),
     Input('pickle_store', 'data'),
     Input('url', 'pathname')

)
def display_end_data(pickle_file, pathname):
    if pathname == '/analise' and pickle_file is not None:
        #pickle file
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        date_end = sys.date_end

        return f"{date_end}"
        
    else:
        return ''

@callback(
    Output('config', 'children'),
    Input('pickle_store', 'data'),
    Input('url', 'pathname')
)
def display_config_data(pickle_file, pathname):
    if pathname == '/analise' and pickle_file is not None:
        #pickle file
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        config = sys.config

        return f"{config}"
        
    else:
        return ''

@callback(
    Output('ratio', 'children'),
    Input('pickle_store', 'data'),
    Input('url', 'pathname')
)
def display_ratio_data(pickle_file, pathname):
    if pathname == '/analise' and pickle_file is not None:
        #pickle file
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        ratio = sys.strehl_ratio

        return f"{ratio}"
        
    else:
        return ''
    
@callback(
    Output('system_name', 'children'),
    Input('pickle_store', 'data'),
    Input('url', 'pathname')
)
def display_name_data(pickle_file, pathname):
    if pathname == '/analise' and pickle_file is not None:
        #pickle file
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        system_name = sys.name

        return f"{system_name}"
        
    else:
        return ''

@callback(
    Output('main_telescope', 'children'),
    Input('pickle_store', 'data'),
    Input('url', 'pathname')
)
def display_main_data(pickle_file, pathname):
    if pathname == '/analise' and pickle_file is not None:
        #pickle file
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        main_telescope = sys.main_telescope.uid

        return f"{main_telescope}"
        
    else:
        return ''
    
@callback(
    Output('system_mode', 'children'),
    Input('pickle_store', 'data'),
    Input('url', 'pathname')
)
def display_data(pickle_file, pathname):
    if pathname == '/analise' and pickle_file is not None:
        #pickle file
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        system_mode = sys.ao_mode

        return f"{system_mode}"
        
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
    Input('pickle_store', 'data'),
    Input('url', 'pathname')
)
def display_sources1(pickle_file, pathname):
    if pathname == '/analise' and pickle_file is not None:
        #pickle file
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        sources = [source_to_dict(source) for source in sys.sources]
        source_divs = [html.Button(source['uid'], id={'type': 'source-button', 'index': source['uid']}, className='option', n_clicks=0, style=option_STYLE) for source in sources]
        return source_divs
    else:
        return []


#WAVEFRONT SENSORS
@callback(
    Output('sensor_divs1', 'children'),
    Input('pickle_store', 'data'),
    Input('url', 'pathname')
)
def display_sensor1(pickle_file, pathname):
    if pathname == '/analise' and pickle_file is not None:
        #pickle file
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        sensors = [wavefront_sensors_to_dict(wavefront_sensor) for wavefront_sensor in sys.wavefront_sensors]
        sensor_divs = [html.Div(sensor['uid'], id=sensor['uid'], className='option', n_clicks=0, style=option_STYLE) for sensor in sensors]
        return sensor_divs
    else:
        return []


    
@callback(
    [Output('sensor_source_div', 'children'),
     Output('just_sensors', 'children')],
    [Input({'type': 'source-button', 'index': ALL}, 'n_clicks'),
     Input('url', 'pathname')],
    [State('pickle_store', 'data')]
)
def update_wavefront_sensor_and_display_names(n_clicks, pathname, pickle_file):
    if pathname == '/analise' and pickle_file is not None:
        #pickle file
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        ctx = dash.callback_context
        if not ctx.triggered:
            return [], []
        else:
            button_id = ctx.triggered[0]['prop_id'].split('.')[0]
            source_id = json.loads(button_id)['index']

            sensor_sources = create_dict_ws(sys)
            associated_sensors = [sensor for sensor, sources in sensor_sources.items() if source_id in sources]

            image_name_dict = create_dict_image(sys)
            image_name_labels = [name for name, sensors in image_name_dict.items() if any(sensor in sensors for sensor in associated_sensors)]

            detector_name_dict = create_dict_detector(sys)
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
    [State('pickle_store', 'data')]
)
def update_verified_loop(just_sensors, pathname, pickle_file):
    if pathname == '/analise' and pickle_file is not None:
        #pickle file
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        ws_loops = create_dict_wc(sys)
        command_loop_mapping = create_dict_command(sys)

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

        return labels, associated_loops
    else:
        return [], []
      


#LOOPS
@callback(
    Output('loop_divs', 'children'),
    [Input('pickle_store', 'data'),
     Input('url', 'pathname')]
)
def display_loop(pickle_file, pathname):
    if pathname == '/analise' and pickle_file is not None:
        #pickle file
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        loops2 = [loop_to_dict(loop) for loop in sys.loops]
        loop_buttons = [html.Button(loop['uid'], id={'type': 'loop-button', 'index': loop['uid']}, className='option', n_clicks=0, style=option_STYLE) for loop in loops2]
        return loop_buttons
    else:
        return []
    
#WAVEFRONT CORRECTORS
@callback(
    Output('verified_corrector_container', 'children'),
    [Input('just_loops', 'children'),
     Input('url', 'pathname')],
    [State('pickle_store', 'data')]
)
def update_corrector_labels(loops, pathname, pickle_file):
    if pathname == '/analise' and pickle_file is not None:
        #pickle file
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        other_WC_loops = create_dict_lp(sys)
        labels = []
        for loop, correctors in other_WC_loops.items():
            for corrector in correctors:
                labels.append(html.Label(f'For the Loop {loop}, the corrector is {corrector}.', style={'color': 'white'}))

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
    [Input('pickle_store', 'data'),
     Input('url', 'pathname')]
)
def display_corrector1(pickle_file, pathname):
    if pathname == '/analise' and pickle_file is not None:
        #pickle file
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        wavefront_correctors = [wavefront_correctors_to_dict(wavefront_corrector) for wavefront_corrector in sys.wavefront_correctors]
        corrector_divs = [html.Div(corrector['uid'], id=corrector['uid'], className='option', n_clicks=0, style=option_STYLE) for corrector in wavefront_correctors]
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
    [Input('pickle_store', 'data'),
     Input('url', 'pathname')]
)
def display_atm(pickle_file, pathname):
    if pathname == '/analise' and pickle_file is not None:
        #pickle file
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)

        atmosphere = [atmosphere_params_to_dict(atmosphere_param) for atmosphere_param in sys.atmosphere_params]
       
        atm_divs = [html.Div(atm['uid'], id=atm['uid'], className='option', n_clicks=0, style=option_STYLE) for atm in atmosphere]
        return atm_divs
    else:
        return []

