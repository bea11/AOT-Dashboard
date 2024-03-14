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
                html.Div('System Name:', style={'margin-top': '4vw'}),
                html.A(id='system_name', style={
                    'display': 'inline-block',
                    'width': '150px',
                    'height': '50px',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),
                html.Div('Mode:', style={'margin-top': '2vw'}),
                html.A(id='system_mode', style={
                    'display': 'inline-block',
                    'width': '150px',
                    'height': '50px',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),

            ], style={'position': 'absolute', 'margin-left': '14vw', 'margin-top': '1vw'}),

]),
    #segundos2
    html.Div([
            html.Div([
                html.Div('Beginning date:', style={'margin-top': '4vw'}),
                html.A(id='beginning-date', style={
                    'display': 'inline-block',
                    'width': '150px',
                    'height': '50px',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),
                html.Div('End date:', style={'margin-top': '2vw'}),
                html.A(id='end-date', style={
                    'display': 'inline-block',
                    'width': '150px',
                    'height': '50px',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),

            ], style={'position': 'absolute', 'margin-left': '28vw', 'margin-top': '1vw'}),

]),
#terceiros2
    html.Div([
            html.Div([
                html.Div('Strehl Ratio:', style={'margin-top': '4vw'}),
                html.A(id='ratio', style={
                    'display': 'inline-block',
                    'width': '150px',
                    'height': '50px',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),
                html.Div('Strehl Wavelength:', style={'margin-top': '2vw'}),
                html.A(id = 'wavelength', style={
                    'display': 'inline-block',
                    'width': '150px',
                    'height': '50px',
                    'background-color': '#1C2634',
                    'margin-top': '0vw'
                }),

            ], style={'position': 'absolute', 'margin-left': '42vw', 'margin-top': '1vw'}),

]),

#quartos2
    html.Div([
            html.Div([
                html.Div('Config:', style={'margin-top': '4vw'}),
                html.A(id='config', style={
                    'display': 'inline-block',
                    'width': '150px',
                    'height': '50px',
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
                html.Div(id='source-list-dynamic', style={
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

        html.Div([
                html.Div(id='output_container'),
                html.Div('Atmosphere Parameters ', style={'margin-left':'7vw'}),
                html.Div([
                    html.Div('D0', id='B0', className='option', n_clicks=0, style=option_STYLE),
                    html.Div('D1', id='B1', className='option', n_clicks=0, style=option_STYLE),
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

    dcc.Store(id='store-atmosphere-params'),
    html.Div(id='output-atmosphere-params'),
])

#@callback(
#    Output('output_container', 'children'),
#    [Input('source', 'n_clicks'),
#     Input('A0', 'n_clicks'),
#     Input('A1', 'n_clicks'),
#     Input('A2', 'n_clicks')],
#    [State('source', 'id'),
 #    State('A0', 'id'),
 #    State('A1', 'id'),
 #    State('A2', 'id')]
#)
#def on_option_click(source, A0, A1, A2, source_id, A0_id, A1_id, A2_id):
#    ctx = dash.callback_context
#    if not ctx.triggered:
#        return ''
#    else:
#        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
      #  return f'You selected: {button_id}'
        

@callback(
    Output('beginning-date', 'children'),
    [Input('store-atmosphere-params', 'data')]
)
def display_beginning_date(data):
    if data is not None:
        # Extract the beginning date from the data.
        beginning_date = data[2]
        return f'{beginning_date}'
    else:
        return ''
    
@callback(
    Output('end-date', 'children'),
    [Input('store-atmosphere-params', 'data')]
)
def display_end_date(data):
    if data is not None:
        # Extract the end date from the data.
        end_date = data[3]
        return f'{end_date}'
    else:
        return ''
    
@callback(
    Output('config', 'children'),
    [Input('store-atmosphere-params', 'data')]
)
def display_end_date(data):
    if data is not None:
        # Extract the end date from the data.
        config = data[4]
        return f'{config}'
    else:
        return ''
    
@callback(
    Output('ratio', 'children'),
    [Input('store-atmosphere-params', 'data')]
)
def display_end_date(data):
    if data is not None:
        # Extract the end date from the data.
        ratio = data[5]
        return f'{ratio}'
    else:
        return ''

@callback(
    Output('system_name', 'children'),
    [Input('store-atmosphere-params', 'data')]
)
def display_end_date(data):
    if data is not None:
        # Extract the end date from the data.
        system_name = data[6]
        return f'{system_name}'
    else:
        return ''

@callback(
    Output('system_mode', 'children'),
    [Input('store-atmosphere-params', 'data')]
)
def display_end_date(data):
    if data is not None:
        # Extract the end date from the data.
        system_mode = data[7]
        return f'{system_mode}'
    else:
        return ''


@callback(
    Output('source-list-dynamic', 'children'),
    [Input('store-atmosphere-params', 'data')]
)
def display_sources(data):
    if data is not None:
        # Extract the sources from the data.
        sources = data[8]
        # Create a list of html.Div elements for each source.
        source_divs = [html.Div(source['uid'], id=source['uid'], className='option', n_clicks=0, style=option_STYLE) for source in sources]
        return source_divs
    else:
        return []

#def display_atmosphere_params(atmosphere_params):
#    ctx = dash.callback_context
#    if not ctx.triggered:
#        return dash.no_update

    # Get the id of the input that triggered the callback.
#    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # Only return the atmosphere parameters when 'store-atmosphere-params' is the trigger.
#    if trigger_id == 'store-atmosphere-params' and atmosphere_params is not None:
#        return html.Div([
#            html.P(f"Atmosphere params: {atmosphere_params}")
#        ])
#    else:
#        return dash.no_update

#@callback(
#    Output('output-atmosphere-params', 'children'),
#    [Input('store-atmosphere-params', 'data')]
#)
#def display_atmosphere_params(atmosphere_params):
#    if atmosphere_params is not None:
#        return html.Div([
#            html.P(f"Atmosphere params: {atmosphere_params}")
#        ])
#    else:
#        return dash.no_update
    