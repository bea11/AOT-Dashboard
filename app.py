import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import base64
import datetime
from dash import Dash, dcc, html, dash_table, Input, Output, State, callback


app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

#estilo
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "10vw",
    "padding": "2rem 1rem",
    "background-color": "#1C2634",
    "color": "#588CF3",
}



sidebar = dbc.Nav(
    [
        dbc.NavLink("Home", href="/", active="exact"),
        dbc.NavLink("Analise", href="/analise", active="exact"),
        dbc.NavLink("Overview", href="/overview", active="exact"),
        dbc.NavLink("Sensor", href="/sensor", active="exact"),
      
    ],
    vertical=True,
    pills=True,
    style=SIDEBAR_STYLE,
)
            

app.layout = html.Div([
    dcc.Store(id='store'),
    dcc.Location(id='url', refresh=False),
    html.Div([
        html.Div(
            dcc.Link(f"{page['name']}", href=page["relative_path"])
        ) for page in dash.page_registry.values()
    ], 
    style=SIDEBAR_STYLE),
    dash.page_container
])


if __name__ == '__main__':
    app.run_server(debug=True)

#html.Div([
#    dcc.link(children=page['name']+" | ",href=page['path'])
#    for page in dash.page_registry.values()

#    html.Hr(),
#    dash.page_container
#    ])