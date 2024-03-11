import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash import callback

#import plotly.graph_objects as go

dash.register_page(__name__, suppress_callback_exceptions=True)

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
                html.Div('System Name:', style={'margin-top': '4vw'}),
                html.A('', style={
                    'display': 'inline-block',
                    'width': '150px',
                    'height': '30px',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),
                html.Div('Mode:', style={'margin-top': '2vw'}),
                html.A('', style={
                    'display': 'inline-block',
                    'width': '150px',
                    'height': '30px',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),

            ], style={'position': 'absolute', 'margin-left': '14vw', 'margin-top': '1vw'}),

]),
    #segundos2
    html.Div([
            html.Div([
                html.Div('Beginning date:', style={'margin-top': '4vw'}),
                html.A('', style={
                    'display': 'inline-block',
                    'width': '150px',
                    'height': '30px',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),
                html.Div('Duration:', style={'margin-top': '2vw'}),
                html.A('', style={
                    'display': 'inline-block',
                    'width': '150px',
                    'height': '30px',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),

            ], style={'position': 'absolute', 'margin-left': '28vw', 'margin-top': '1vw'}),

]),
#terceiros2
    html.Div([
            html.Div([
                html.Div('Strehl Ratio:', style={'margin-top': '4vw'}),
                html.A('', style={
                    'display': 'inline-block',
                    'width': '150px',
                    'height': '30px',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),
                html.Div('Strehl Wavelength:', style={'margin-top': '2vw'}),
                html.A('', style={
                    'display': 'inline-block',
                    'width': '150px',
                    'height': '30px',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),

            ], style={'position': 'absolute', 'margin-left': '42vw', 'margin-top': '1vw'}),

]),

#quartos2
    html.Div([
            html.Div([
                html.Div('Config:', style={'margin-top': '4vw'}),
                html.A('', style={
                    'display': 'inline-block',
                    'width': '150px',
                    'height': '30px',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),
               

            ], style={'position': 'absolute', 'margin-left': '56vw', 'margin-top': '1vw'}),


    #importante quando quero variar entre estados
    html.Button('Source', id='source'),

]),





    #esquema AO
    html.Div([
        html.H2("AO System", style={'text-align': 'center', 'text-decoration': 'underline', 'text-decoration-color': '#C17FEF', 'margin-bottom': '5vw'}),

        html.Div([
           html.Div([
                html.Div(id='output_container'),
                html.Div('Sources', style={'margin-left':'12vw'}),
                html.Div([
                    html.Div('A0', id='A0', className='option', n_clicks=0, style=option_STYLE),
                    html.Div('A1', id='A1', className='option', n_clicks=0, style=option_STYLE),
                    html.Div('A2', id='A2', className='option', n_clicks=0, style=option_STYLE),
            ], style={
                'width': "15vw",
                'height': '100px',
                'overflowY': 'scroll',
                'backgroundColor': '#1C2634',
                'color': 'white',
                'margin-left': '12vw'
            }),
        ]),

        html.Div([
                html.Div(id='output_container'),
                html.Div('Wavefront Sensors', style={'margin-left':'7vw'}),
                html.Div([
                    html.Div('A0', id='A0', className='option', n_clicks=0, style=option_STYLE),
                    html.Div('Shack-Hartmann', id='SH', className='option', n_clicks=0, style=option_STYLE),
                    html.Div('Pyramid', id='PD', className='option', n_clicks=0, style=option_STYLE),
            ], style={
                'width': "15vw",
                'height': '100px',
                'overflowY': 'scroll',
                'backgroundColor': '#1C2634',
                'color': 'white',
                'margin-left': '7vw'
            }),
        ]),
        
        html.Div([
                html.Div(id='output_container'),
                html.Div('Wavefront Correctors', style={'margin-left':'7vw'}),
                html.Div([
                    html.Div('B0', id='B0', className='option', n_clicks=0, style=option_STYLE),
                    html.Div('B1', id='B1', className='option', n_clicks=0, style=option_STYLE),
                    html.Div('B2', id='B2', className='option', n_clicks=0, style=option_STYLE),
            ], style={
                'width': "15vw",
                'height': '100px',
                'overflowY': 'scroll',
                'backgroundColor': '#1C2634',
                'color': 'white',
                'margin-left': '7vw'
            }),
        ]),

            dbc.Select(id="aotpy_loops",
                        options=[
                            {'label': 'Loops', 'value': 'loops'},
                            {'label': 'C0', 'value': 'C0'},
                            {'label': 'C1', 'value': 'C1'},
                            {'label': 'C2', 'value': 'C2'}],
                        value='loops',
                        className='custom-select',
                        style={'width': "15vw",'color': 'white',  'margin-left': '5vw', 'height':'50px' }),
        ], style={'display': 'flex', 'justifyContent': 'flex-start', 'flexWrap': 'wrap'}),
    ], style={'position': 'absolute', 'bottom': '7vw', 'width': '100%'}),
])

@callback(
    Output('output_container', 'children'),
    [Input('source', 'n_clicks'),
     Input('A0', 'n_clicks'),
     Input('A1', 'n_clicks'),
     Input('A2', 'n_clicks')],
    [State('source', 'id'),
     State('A0', 'id'),
     State('A1', 'id'),
     State('A2', 'id')]
)
def on_option_click(source, A0, A1, A2, source_id, A0_id, A1_id, A2_id):
    ctx = dash.callback_context
    if not ctx.triggered:
        return ''
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
      #  return f'You selected: {button_id}'