from dash import dcc, html, Input, Output, callback
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc


# Display 
display2 = dbc.Row(children=[
    dcc.Markdown(id='display2')
])
@callback(
    Output('display2', 'children'),
    Input('page-2-dropdown', 'value'),
    )
def display_value(value):
    return f'You have selected {value}'


grafico2 = dbc.Row(children=[
    
    dcc.Graph(id='grafico2', figure={})
])
@callback(
    Output('grafico2', 'figure'),
    Input('filter_data', 'data'),
    )
def display_value(data):
    df = pd.DataFrame.from_dict(data)
    df = data.copy()
    grafico = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
    return grafico
