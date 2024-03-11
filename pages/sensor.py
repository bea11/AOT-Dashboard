import dash
from dash import dcc
from dash import html, callback
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

dash.register_page(__name__, suppress_callback_exceptions=True)

layout = html.Div([
    html.H1("Shack-Hartmann", style={'text-align': 'left', 'margin-left': '12vw', 'marginBottom' : '0px'}),
    html.Div([],style={'background-color': '#1C2634', 'color': 'white', 'position': 'absolute', 'left': '200px', 'marginTop': '1vw', 'width': '1290px', 'height': '620px'}),
])

@callback(Output('some-output', 'children'),
          Input('store', 'data'))  
def update_some_output(atm):
    if atm is not None:
        return f'The stored atm value is {atm}'
    else:
        return 'No atm value is stored'