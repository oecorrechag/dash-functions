from dash import dcc, html
import dash_bootstrap_components as dbc

header = html.Div([
    html.H1('Hello Dash'),
    
    dbc.Checklist(
        options=[
            {"label": "English", "value": 1},
        ],
        value=[1],
        id="select_language",
        switch=True,
    ),

    html.Div([
        html.P('Dash converts Python classes into HTML'),
        html.P("This conversion happens behind the scenes by Dash's JavaScript front-end")
        ]),
    ])


header2 = html.Div([
    html.H1('Hello Dash'),
    html.Div([
        html.P('Dash converts Python classes into HTML'),
        html.P("This conversion happens behind the scenes by Dash's JavaScript front-end")
        ]),
    ])