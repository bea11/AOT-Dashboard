import dash
from dash import dcc
from dash import html, callback
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import aotpy

dash.register_page(__name__, suppress_callback_exceptions=True)

layout = html.Div([
    html.H1("Shack-Hartmann", style={'text-align': 'left', 'margin-left': '12vw', 'marginBottom' : '0px'}),
    #html.Div([],style={'background-color': '#1C2634', 'color': 'white', 'position': 'absolute', 'left': '200px', 'marginTop': '1vw', 'width': '1290px', 'height': '620px'}),

    html.Div(id='sensor-output')  # Display
])

@callback(
    Output('sensor-output', 'children'),
    [Input('store-data', 'data')]
)
def process_fits_file(store_data):
    if store_data is not None:
        contents = store_data.get('contents')
        filename = store_data.get('filename')
        if contents is not None and filename.endswith('.fits'):
            
            sys = aotpy.read_system_from_fits(filename)
            atm = len(sys.atmosphere_params)
            return html.Div([
                html.P(f"Processed FITS file: {filename}"),
                html.P(f"Number of atmosphere parameters: {atm}")
            ])
    return html.P("No FITS file uploaded or invalid file format")