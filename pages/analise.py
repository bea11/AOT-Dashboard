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


dash.register_page(__name__, path='/analise')


#Edit each space on AOT:
option_STYLE = {
    'width': '100%',
    'background-color': '#1C2634',
    'color': 'white',
    'cursor': 'pointer',
    'border': '1px solid #243343',
}


layout = html.Div([
    html.H1("Overview", style={'text-align': 'left', 'margin-left': '12vw'}),
    
#Blocks
 
    html.Div([
            
                html.Div('System Name:', style={'margin-top': '2vw'}),
                html.A(id='system_name', style={
                    'display': 'inline-block',
                    'width': '12.25vw',
                    'height': '3.75vw',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),

            ], style={'position': 'absolute', 'margin-left': '8vw'}),

html.Div([
                html.Div('Mode:', style={'margin-top': '2vw'}),
                html.A(id='system_mode', style={
                    'display': 'inline-block',
                    'width': '12.25vw',
                    'height': '3.75vw',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),
                 ], style={'position': 'absolute', 'margin-left': '23vw'}),


    
            html.Div([
                html.Div('Beginning date:', style={'margin-top': '2vw'}),
                html.A(id='beginning-date', style={
                    'display': 'inline-block',
                    'width': '12.25vw',
                    'height': '3.75vw',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),

            ], style={'position': 'absolute', 'margin-left': '37vw'}),



    html.Div([
                html.Div('End date:', style={'margin-top': '2vw'}),
                html.A(id='end-date', style={
                    'display': 'inline-block',
                    'width': '12.25vw',
                    'height': '3.75vw',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),
                 ], style={'position': 'absolute', 'margin-left': '51vw'}),

    html.Div([
            html.Div([
                html.Div('Strehl Ratio:', style={'margin-top': '2vw'}),
                html.A(id='ratio', style={
                    'display': 'inline-block',
                    'width': '12.25vw',
                    'height': '3.75vw',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),

            ], style={'position': 'absolute', 'margin-left': '65vw'}),

]),

    html.Div([
            html.Div([
                html.Div('Config:', style={'margin-top': '2vw'}),
                html.A(id='config', style={
                    'display': 'inline-block',
                    'width': '12.25vw',
                    'height': '3.75vw',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),
               

            ], style={'position': 'absolute', 'margin-left': '79vw'}),

]),



#AO Scheme details
    html.Div([
        html.H3("AO System", style={'text-align': 'center', 'text-decoration': 'underline', 'text-decoration-color': '#C17FEF', 'margin-bottom': '1vw','margin-top': '1vw'}),

#SOURCES
        html.Div([
           html.Div([
                html.Div(id='output_container'),
                html.Div('Sources', style={'margin-left':'12vw'}),
                html.Div(id='source_divs1',n_clicks=0, style={
                    'width': "12vw",
                    'height': '6.5vw',
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
                    'height': '3.75vw',
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
                'height': '6.65vw',
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
                'height': '6.65vw',
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
                'height': '6.65vw',
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
                'height': '6.65vw',
                'overflowY': 'scroll',
                'backgroundColor': '#1C2634',
                'color': 'white',
                'margin-left': '2vw'
            }),
        ]),

        
        ], style={'display': 'flex', 'justifyContent': 'flex-start', 'flexWrap': 'wrap'}),
    ], style={'position': 'absolute', 'top': '16vw', 'width': '100%'}),


#Hierarchy Section
html.Div([
        html.Div([

#Wavefront sensors associated with the clicked source
  
        html.Div([
            html.Div([
                html.Div(id='sensor_source_div'),
    ], style={'display': 'flex', 'flex-direction': 'column', 'margin-top':'1vw'}),
], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'margin-left': '2vw', 'width': '30vw'}),
#Wavefront corrector and loops associated with the wavefront sensor
        
        html.Div([
            html.Div([
                html.Div(id='verified_loop_container'),
    ], style={'display': 'flex', 'flex-direction': 'column', 'margin-top':'1vw'}),
], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'margin-left': '5vw', 'width': '43vw'}),

    ], style={'display': 'flex'}),
], style={'background-color': '#1C2634', 'color': 'white', 'position': 'absolute', 'left': '8vw', 'top': '31.5vw', 'width': '82.5vw', 'height': '13vw'}),

    dcc.Store(id='pickle_store', storage_type='local'),
    html.Div(id='output-atmosphere-params'),
  
    html.Div(id='just_sensors', style={'display': 'none'}),  # para poder chamar sem ter problemas
    html.Div(id='just_loops', style={'display': 'none'}),
])



#Functions
#Dictionary of the source
def source_to_dict(source):
    return {
        'uid': source.uid,
        'right_ascension': source.right_ascension,
        'declination': source.declination,
        'elevation_offset': source.elevation_offset,
        'azimuth_offset': source.azimuth_offset,
        'width': source.width
    }
#Dictionary of the wavefront sensor
def wavefront_sensors_to_dict(wavefront_sensor):
    return {
        'uid': wavefront_sensor.uid,
        'n_valid_subapertures': wavefront_sensor.n_valid_subapertures,
        'subaperture_size': wavefront_sensor.subaperture_size,
        'wavelength': wavefront_sensor.wavelength,
    }
#Dictionary of the loops
def loop_to_dict(loop):
    return {
        'uid': loop.uid, 
        'commands':loop.commands.name if loop.commands is not None else None,
    }
#Dictionary of the wavefront corrector
def wavefront_correctors_to_dict(wavefront_corrector):
    return {
        'uid': wavefront_corrector.uid,
    }
#Dictionary of the atmosphere parameters
def atmosphere_params_to_dict(atmosphere_param):
    return {
        'uid': atmosphere_param.uid,
    }
#Iterate over the sources of the wavefront sensor and add its associated sources
def create_dict_ws(sys):
    e = {}
    for wavefront_sensor in sys.wavefront_sensors:
        if wavefront_sensor.uid not in e:
            e[wavefront_sensor.uid] = []
        e[wavefront_sensor.uid].append(wavefront_sensor.source.uid)
    print(f"e:{e} type :{type(e)}")
    return e

#Names of the measurements of the wavefront sensor
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

#first compare the loop to check if its control loop, if it is add the corresponding input sensors to the list
def create_dict_wc(sys):
    k = {}
    for loop in sys.loops:
        if isinstance(loop, aotpy.core.loop.ControlLoop):
            if loop.uid not in k:
                k[loop.uid] = {'input_sensors': []}
            k[loop.uid]['input_sensors'].append(loop.input_sensor.uid)
    print(f"k: {k}, type: {type(k)}")        
    return k

#loops commands
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

#Detectors of the wavefront sensors, iterate for each wavefront sensor
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

#Iterate over each loop and add the associated wavefront corrector for that loop
def create_dict_lp(sys):
    d = {}
    for loop in sys.loops:
        #print(f"loop: {loop}, type: {type(loop)}")
        if loop.uid not in d:
            d[loop.uid] = []
        d[loop.uid].append(loop.commanded_corrector.uid)
        print(f"d: {d}, type: {type(d)}")
    return d


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


#SOURCES, need to create a button for the user to select and source (hierarchy section)

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

#All in one section, display the detector and measurements associated with the wavefront sensor
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
#trigger detected, if the trigger is from the button it continues with the function
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
                        html.Span(f'Wavefront Sensor: {sensor}, Measurements: '),
                        dcc.Link(f'{image_name}', href='/measurements'),
                        html.Span(', Detector: '),
                        dcc.Link(f'{detector_name}', href='/pixels'),
                        ], id=f'verified_sensor[{i+1}]', style={'color': 'white'})
            )
            print(f"associated_sensors: {associated_sensors}")
            return labels, associated_sensors
    else:
        return [], []
    
#All in one, wavefront correctors, loops and commands
@callback(
    Output('verified_loop_container', 'children'),
    [Input('just_sensors', 'children'),
     Input('url', 'pathname')],
    [State('pickle_store', 'data')]
)
def update_verified_loop(just_sensors, pathname, pickle_file):
    if pathname == '/analise' and pickle_file is not None:
        #pickle file
        with open(pickle_file, 'rb') as f:
            sys = pickle.load(f)
#Lists for loops and comanded loops
        ws_loops = create_dict_wc(sys)
        command_loop_mapping = create_dict_command(sys)

        associated_loops = [loop for loop, sensors in ws_loops.items() if any(sensor in sensors['input_sensors'] for sensor in just_sensors)]
    
        for i, loop in enumerate(associated_loops):
            command = next((cmd for cmd, loops in command_loop_mapping.items() if loop in loops), None)

        command_wfc_mapping = create_dict_lp(sys)
        labels_wfc = []
        for i, loop_id in enumerate(associated_loops):  
            loop = next((l for l in sys.loops if l.uid == loop_id), None)
            if loop:               
                corrector_uids = command_wfc_mapping.get(loop.uid, [])
                for corrector_uid in corrector_uids:
                    command = next((cmd for cmd, loops in command_loop_mapping.items() if loop_id in loops), None)
                    labels_wfc.append(
                        html.Div([
                            html.Span(f'Wavefront Corrector: {corrector_uid}, Loop: {loop_id}, Command: '),
                            dcc.Link(f'{command}', href='/commands'),
                        ], id=f'loop-{i+1}', style={'color': 'white'})
                    )
        return labels_wfc
    else:
        return []
      

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
#Atmosphere Parameters
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

