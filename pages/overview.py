import dash
from dash import dcc
from dash import html, register_page
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/overview')

layout = html.Div([
   html.H1("Wavefront Sensor", style={'text-align': 'left', 'margin-left': '12vw'}),
   #1 coluna
    html.Div([
        html.P("Properties", style={'text-align': 'left', 'margin-left': '1vw'}),
        
    #Strings    
        html.Div([
            html.Label("Name of sensor: ", style={'color': 'white'}),
            html.Div([], style={'background-color': '#243343', 'width': '170px', 'height': '24px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '10px'}),
    
        html.Div([
            html.Label("Shutter Type: ", style={'color': 'white'}),
            html.Div([], style={'background-color': '#243343', 'width': '170px', 'height': '24px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '10px'}),

        html.Div([
            html.Label("String: ", style={'color': 'white'}),
            html.Div([], style={'background-color': '#243343', 'width': '170px', 'height': '24px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '10px'}),
     
    #Integers
        html.Div([
            html.Label("Unique Identifier: ", style={'color': 'white'}),
            html.Div([], style={'background-color': '#243343', 'width': '170px', 'height': '24px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '10px', 'margin-top': '13px'}),

        html.Div([
            html.Label("Integer: ", style={'color': 'white'}),
            html.Div([], style={'background-color': '#243343', 'width': '170px', 'height': '24px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '10px'}),

        html.Div([
            html.Label("Number of valid subapertures: ", style={'color': 'white'}),
            html.Div([], style={'background-color': '#243343', 'width': '170px', 'height': '24px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '10px'}),

    #Floats
        html.Div([
            html.Label("Subapertures Size: ", style={'color': 'white'}),
            html.Div([], style={'background-color': '#243343', 'width': '170px', 'height': '24px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '10px', 'margin-top': '13px'}),

        html.Div([
            html.Label("Altitudes: ", style={'color': 'white'}),
            html.Div([], style={'background-color': '#243343', 'width': '170px', 'height': '24px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '10px'}),
   
        html.Div([
            html.Label("Float: ", style={'color': 'white'}),
            html.Div([], style={'background-color': '#243343', 'width': '170px', 'height': '24px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '10px'}),
   
    #Extra

        html.Div([
            html.Label("Extra: ", style={'color': 'white'}),
            html.Div([], style={'background-color': '#243343', 'width': '170px', 'height': '24px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '10px', 'margin-top': '15px'}),
    
        html.Div([
            html.Label("Extra: ", style={'color': 'white'}),
            html.Div([], style={'background-color': '#243343', 'width': '170px', 'height': '24px', 'margin-left': '10px'})
    ], style={'background-color': '#1C2634', 'color': 'white', 'display': 'flex', 'align-items': 'center', 'padding': '10px'}),

    ], style={'background-color': '#1C2634', 'color': 'white', 'position': 'absolute', 'left': '200px', 'top': '80px', 'width': '420px', 'height': '597px'}),
    
   #2 coluna 
    html.Div([
        html.P("Objects", style={'text-align': 'left','margin-left': '1vw'}),
  
    #1 bloco
        html.Div([
            html.P("Source", style={'text-align': 'left', 'margin-left': '1vw'}),
            html.Div([
                html.Label("Name: ", style={'color': 'white'}),
                html.Button("Example_Name", style={'border-radius': '10%', 'border': '1.5px solid blue', 'background-color': '#1C2634', 'color':'white','font-size':'15px', 'width': '150px', 'height': '20px', 'margin-left': '10px'})
            ], style={'display': 'flex', 'align-items': 'center', 'margin-left': '1vw'}),
            html.P("Type: Natural Guide Star", style={'text-align': 'left', 'margin-left': '1vw', 'color': 'white'}),
    ], style={'background-color': '#243343', 'color': 'white', 'display': 'flex', 'flex-direction': 'column', 'width':'350px', 'height': '100px','margin-left': '1.5vw'}),

    #2 bloco
        html.Div([
            html.P("Detector", style={'text-align': 'left', 'margin-left': '1vw'}),
            html.Div([
                html.Label("Name: ", style={'color': 'white'}),
                html.Button("Other_Name", style={'border-radius': '10%', 'border': '1.5px solid blue', 'background-color': '#1C2634', 'color':'white','font-size':'15px', 'width': '150px', 'height': '20px', 'margin-left': '10px'})
            ], style={'display': 'flex', 'align-items': 'center', 'margin-left': '1vw'}),
            html.P("Type: CMOS", style={'text-align': 'left', 'margin-left': '1vw', 'color': 'white'}),
    ], style={'background-color': '#243343', 'color': 'white', 'display': 'flex', 'flex-direction': 'column', 'width':'350px', 'height': '100px','margin-left': '1.5vw', 'margin-top': '15px'}),

    #3 bloco
        html.Div([
            html.P("Aberration 1", style={'text-align': 'left', 'margin-left': '1vw'}),
            html.Div([
                html.Label("Name: ", style={'color': 'white'}),
                html.Button("Example", style={'border-radius': '10%', 'border': '1.5px solid blue', 'background-color': '#1C2634', 'color':'white','font-size':'15px', 'width': '150px', 'height': '20px', 'margin-left': '10px'})
            ], style={'display': 'flex', 'align-items': 'center', 'margin-left': '1vw'}),
            html.P("Type: Other", style={'text-align': 'left', 'margin-left': '1vw', 'color': 'white'}),
    ], style={'background-color': '#243343', 'color': 'white', 'display': 'flex', 'flex-direction': 'column', 'width':'350px', 'height': '100px','margin-left': '1.5vw', 'margin-top': '15px'}),

    #3 bloco
        html.Div([
            html.P("Aberration 2", style={'text-align': 'left', 'margin-left': '1vw'}),
            html.Div([
                html.Label("Name: ", style={'color': 'white'}),
                html.Button("Example", style={'border-radius': '10%', 'border': '1.5px solid blue', 'background-color': '#1C2634', 'color':'white','font-size':'15px', 'width': '150px', 'height': '20px', 'margin-left': '10px'})
            ], style={'display': 'flex', 'align-items': 'center', 'margin-left': '1vw'}),
            html.P("Type: Other", style={'text-align': 'left', 'margin-left': '1vw', 'color': 'white'}),
    ], style={'background-color': '#243343', 'color': 'white', 'display': 'flex', 'flex-direction': 'column', 'width':'350px', 'height': '100px','margin-left': '1.5vw', 'margin-top': '15px'}),



    ], style={'background-color': '#1C2634', 'color': 'white', 'position': 'absolute', 'left': '655px', 'top': '80px', 'width': '400px', 'height': '597px'}),
    
    #3 coluna
    html.Div([
        html.P("Images", style={'text-align': 'left','margin-left': '1vw'}),

    #1 bloco
        html.Div([
            html.Div([
                html.P("Name: ExampleAA", style={'text-align': 'left', 'color': 'white'}),
                html.P("Dimensions: 255x255", style={'text-align': 'left', 'color': 'white', 'margin-top': '0px'}),
                html.P("Type: Example", style={'text-align': 'left', 'color': 'white'}),
                html.P("Unit: Meters", style={'text-align': 'left', 'color': 'white'}),
        ], style={'color': 'white', 'display': 'flex', 'flex-direction': 'column','margin-left': '1vw'}),
            html.Button("ExampleAA", style={'border-radius': '10%', 'border': '1.5px solid blue', 'background-color': '#243343', 'color':'white', 'font-size':'15px', 'width': '100px', 'height': '22px', 'position': 'absolute', 'left': '220px', 'top': '100px'}),
    ], style={'color': 'white', 'display': 'flex', 'flex-direction': 'column', 'width':'350px', 'height': '150px','margin-left': '1vw'}),
    
    #2 bloco
        html.Div([
            html.Div([
                html.P("Name: ExampleBB", style={'text-align': 'left', 'color': 'white'}),
                html.P("Dimensions: 255x255", style={'text-align': 'left', 'color': 'white', 'margin-top': '0px'}),
                html.P("Type: Example", style={'text-align': 'left', 'color': 'white'}),
                html.P("Unit: Meters", style={'text-align': 'left', 'color': 'white'}),
        ], style={'color': 'white', 'display': 'flex', 'flex-direction': 'column','margin-left': '1vw'}),
            html.Button("ExampleBB", style={'border-radius': '10%', 'border': '1.5px solid blue', 'background-color': '#243343', 'color':'white', 'font-size':'15px', 'width': '100px', 'height': '22px', 'position': 'absolute', 'left': '220px', 'top': '280px'}),
    ], style={'color': 'white', 'display': 'flex', 'flex-direction': 'column', 'width':'350px', 'height': '150px','margin-left': '1vw','margin-top':'20px'}),

    #1 bloco
        html.Div([
            html.Div([
                html.P("Name: ExampleCC", style={'text-align': 'left', 'color': 'white'}),
                html.P("Dimensions: 100x100x100", style={'text-align': 'left', 'color': 'white', 'margin-top': '0px'}),
                html.P("Type: Example", style={'text-align': 'left', 'color': 'white'}),
                html.P("Unit: Meters", style={'text-align': 'left', 'color': 'white'}),
        ], style={'color': 'white', 'display': 'flex', 'flex-direction': 'column','margin-left': '1vw'}),
            html.Button("ExampleCC", style={'border-radius': '10%', 'border': '1.5px solid blue', 'background-color': '#243343', 'color':'white', 'font-size':'15px', 'width': '100px', 'height': '22px', 'position': 'absolute', 'left': '220px', 'top': '460px'}),
    ], style={'color': 'white', 'display': 'flex', 'flex-direction': 'column', 'width':'350px', 'height': '150px','margin-left': '1vw','margin-top':'20px'}),

    


    ], style={'background-color': '#1C2634', 'color': 'white', 'position': 'absolute', 'left': '1090px', 'top': '80px', 'width': '400px', 'height': '597px'}),
 
], style={'position': 'relative'})


