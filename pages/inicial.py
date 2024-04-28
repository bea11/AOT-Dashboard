import base64
import datetime
import io
import dash
from dash import Dash, dcc, html, dash_table, Input, Output, State, callback, register_page, no_update
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import aotpy
from astropy.io import fits

import tempfile
import os
import plotly as plt
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import gzip
import base64



dash.register_page(__name__, path='/')

#estilo
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

#layout
layout = html.Div([
    html.H1("Dashboard AOTPY", style={'textAlign': 'left', 'marginLeft': '12vw'}),
    html.Div([
        html.Div(["Upload the FITS File"], style={'textAlign': 'left', 'textDecoration': 'underline', 'textDecorationColor': '#8CE397', 'fontSize':'18px','marginLeft':'20vw', 'marginTop':'5vw'}),
        #Fazer upload
        
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                        html.Div(['Drag and Drop file here (.FITS)'],style={'display': 'inline-block', 'color': 'white','fontWeight': 'bold', 'position': 'absolute', 'marginLeft': '4vw', 'marginTop': '2.5vw'}),
                         html.A('Browse Files', style={
                            'display': 'inline-block',
                            'padding': '10px 20px',
                            'backgroundColor': '#243343',
                            'color': 'white',
                            'textDecoration': 'none',
                            'position': 'absolute',
                            'marginLeft': '40vw',
                            'marginTop': '2vw',
                            'borderRadius': '5px'
})
            ]),
            style=DRAG_STYLE,
            multiple=False,
        ),
       
       
       
    ]),
    dcc.Store(id='store-atmosphere-params'),
     html.Div(id='output-data-upload'),
])

def telescope_to_dict(telescope):
    return {
        'uid': telescope.uid,
    }

#tentar extrair dicionário
def source_to_dict(source):
    return {
        'uid': source.uid,
        'right_ascension': source.right_ascension,
        'declination': source.declination,
        'elevation_offset': source.elevation_offset,
        'azimuth_offset': source.azimuth_offset,
        'width': source.width
    }

#WAVEFRONT SENSORS
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


#->> PARA QUE ISTO
#def create_dict_command(sys):
#    i = {}
#    for loop in sys.loops:
#        if loop.commands is not None:
#            command_name = loop.commands.name
#            if command_name not in i:
#                i[command_name] = []
#            i[command_name].append(loop.commanded_corrector.uid)
#    print(f"i: {i} type: {type(i)}")
#    return i

   
#def control_loop_dict(sys):
    #print(f"uid: {loop.iud}, input_sensor: {loop.input_sensor.uid}"),
    #return {
    #    'uid': aotpy.core.loop.ControlLoop.uid,
        #'input_sensor': aotpy.core.loop.ControlLoop.uid

    #}


#def telescope_to_dict(telescope):
#    return {
#        'uid': telescope.uid,
#    }


def wavefront_correctors_to_dict(wavefront_corrector):
    return {
        'uid': wavefront_corrector.uid,
    }

def atmosphere_params_to_dict(atmosphere_param):
    return {
        'uid': atmosphere_param.uid,
    }


@callback(
    Output('store-atmosphere-params', 'data'),
    [Input('upload-data', 'contents')]
)
def store_uploaded_file(contents):
    if contents is not None:
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        sys = aotpy.read_system_from_fits(io.BytesIO(decoded))
        #teste
        atmosphere_params = len(sys.atmosphere_params)
        #date beginning
        date_beginning = sys.date_beginning  
        #end data
        date_end = sys.date_end 
        #config
        config = sys.config
        #ratio
        ratio = sys.strehl_ratio
        #name 
        system_name = sys.name
        #mode
        system_mode = sys.ao_mode
        #main telescope
        #main_telescope = telescope_to_dict(sys.main_telescope)
        main_telescope = sys.main_telescope.uid
        #sources list
        sources = [source_to_dict(source) for source in sys.sources]  # dicionário

        #todos os wavefront sensors
        sensors = [wavefront_sensors_to_dict(wavefront_sensor)['uid'] for wavefront_sensor in sys.wavefront_sensors] 
        #os wavefront sensors com as sources correspondentes
        other_sensor_sources = create_dict_ws(sys)
        #Measurements
        image_name = create_dict_image(sys)
        #Detector
        detector_name = create_dict_detector(sys)
        #testes: print(f"other_WC_lopps: {other_sensor_sources}, type: {type(other_sensor_sources)}")
        #LOOPS TODOS
        loops2 = [loop_to_dict(loop) for loop in sys.loops]
        #OFFLOAD LOOPS
        offload_loops = [loop_to_dict(loop) for loop in sys.loops if isinstance(loop, aotpy.core.loop.OffloadLoop)]
        print(f"offload_loops: {offload_loops}")
        #CONTROL LOOPS
        control_loops = [loop_to_dict(loop) for loop in sys.loops if isinstance(loop, aotpy.core.loop.ControlLoop)]
        print(f"control_loops: {control_loops}")

        #os wavefront sensors dos loops
        other_WS_loops= create_dict_wc(sys)

        #novo_teste = control_loop_dict(sys)
        #print(f"novo_teste: {novo_teste}")
        #SÃO OS WAVEFRONT CORRECTORS DO LOOPS
        other_WC_loops = create_dict_lp(sys)
        #print(f"other_WC_lopps:{other_WC_lopps}, type:{type(other_WC_lopps)}")
        command_name = create_dict_command(sys)
        print(f"command_name: {command_name}, type: {type(command_name)}")
        
        #wavefront corrector
        correctors = [wavefront_correctors_to_dict(wavefront_corrector) for wavefront_corrector in sys.wavefront_correctors]
       
        #atmospheric parameters
        atmosphere = [atmosphere_params_to_dict(atmosphere_param) for atmosphere_param in sys.atmosphere_params]

        #Para a página Measurements
        n_subapertures = [wavefront_sensors_to_dict(wavefront_sensor)['n_valid_subapertures'] for wavefront_sensor in sys.wavefront_sensors] 
        subapertures_size = [wavefront_sensors_to_dict(wavefront_sensor)['subaperture_size'] for wavefront_sensor in sys.wavefront_sensors] 
        wavelength = [wavefront_sensors_to_dict(wavefront_sensor)['wavelength'] for wavefront_sensor in sys.wavefront_sensors] 

        return {
            'atmosphere_params': atmosphere_params,
            'date_beginning': date_beginning,
            'date_end': date_end,
            'config': config,
            'ratio': ratio,
            'system_name': system_name,
            'system_mode': system_mode,
            'main_telescope': main_telescope,
            'loops2': loops2,
            'offload_loops': offload_loops,
            'control_loops': control_loops,
            'other_WC_loops': other_WC_loops, 
            'other_WS_loops': other_WS_loops,
            'command_name': command_name,
            'sources': sources,
            
            'wavefront_sensors': sensors,
            'image_name': image_name,
            'detector_name': detector_name,

            'other_sensor_sources': other_sensor_sources,
            
            'wavefront_correctors': correctors,
            'atmosphere_params': atmosphere,

            'n_subapertures': n_subapertures,
            'subapertures_size': subapertures_size,
            'wavelength': wavelength,
        }
    else:
        raise PreventUpdate

@callback(
    Output('output-data-upload', 'children'),
    Input('upload-data', 'filename')
)
def display_uploaded_filename(filename):
    if filename is not None:
        return html.Div([
            html.H6(f"Uploaded FITS file: {filename}", style={'textAlign': 'left', 'marginLeft': '20vw', 'marginTop': '6vw'})
        ])
    else:
        return html.Div()
    



#mais funções: sys.wavefront_sensors
        # len(sys.atmosphere_sensors)
        # wfs = sys.wavefront_sensors[0]
        #det = wfs.detector
        #pixels = det.pixel_intensities
        #pixels.data
        #frame= pixels.data[0]
        #frame.shape
