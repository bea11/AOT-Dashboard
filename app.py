import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import base64
import datetime
from dash import Dash, dcc, html, dash_table, Input, Output, State, callback



app = dash.Dash(__name__, use_pages=True, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

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
        dbc.NavItem(dbc.NavLink("Overview", href="/analise")),
        dbc.NavItem(dbc.NavLink("Pixel", href="/pixels")),
        dbc.NavItem(dbc.NavLink("Measurement", href="/measurements")),
        dbc.NavItem(dbc.NavLink("Command", href="/commands")),
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

