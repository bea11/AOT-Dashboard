import dash
from dash import Dash, dcc, html, dash_table, Input, Output, State, callback, register_page
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import base64
import datetime
import io
import aotpy
import gzip


dash.register_page(__name__, path='/sensor')

layout = html.Div([
    html.H1("Shack-Hartmann", style={'text-align': 'left', 'margin-left': '12vw', 'marginBottom' : '0px'}),
    #html.Div([],style={'background-color': '#1C2634', 'color': 'white', 'position': 'absolute', 'left': '200px', 'marginTop': '1vw', 'width': '1290px', 'height': '620px'}),

    html.Div(id='sensor-output')  # Placeholder for displaying sensor data
])

@callback(
    Output('sensor-output', 'children'),
    [Input('store-data', 'data')]
)
def process_fits_file(encoded):
    print("Cheguei aqui dentro")
    if encoded is not None:
        print("estou no encoded")
        compressed = base64.b64decode(encoded)
        decoded = gzip.decompress(compressed)
        sys = aotpy.read_system_from_fits(io.BytesIO(decoded))
        print("sai do sys")
        atm = len(sys.atmosphere_params)
        print("sai do atm")
        return html.Div([
            html.P(f"Processed FITS file"),
            html.P(f"Number of atmosphere parameters: {atm}")
        ])
    return html.P("No FITS file uploaded or invalid file format")