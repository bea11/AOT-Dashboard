import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import base64
import datetime
from dash import Dash, dcc, html, dash_table, Input, Output, State, callback


app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

#server = app.server

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


navbar = dbc.Navbar(
    [
        dbc.NavItem(dbc.NavLink("Home", href="/")),
        dbc.NavItem(dbc.NavLink("Analise", href="/analise")),
        dbc.NavItem(dbc.NavLink("Pixels", href="/pixels")),
        dbc.NavItem(dbc.NavLink("Measurements", href="/measurements")),
        dbc.NavItem(dbc.NavLink("Commands", href="/commands")),
    ],
    color="dark",
    dark=True,
)

app.layout = html.Div([
    dcc.Store(id='store'),
    dcc.Location(id='url', refresh=False),
    navbar,
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
