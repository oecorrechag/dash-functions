from dash import dcc, html, Input, Output, callback, State
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc


# Display 
display1 = dbc.Row(children=[
    dcc.Markdown(id='display1')
])
@callback(
    Output('display1', 'children'),
    Input('page1_menu', 'value'),
)
def graphics(value):
    return f'You have selected {value}'


# Grafico 
grafico1 = html.Div([
    dcc.Graph(id='grafico', figure={}),
])
@callback(
    Output('grafico', 'figure'),
    Input('original_data', 'data'),
    Input('page1_menu', 'value'),
    )
def display_value(data, value):
    df = pd.DataFrame.from_dict(data)
    df = df[df['City'] == value]
    grafico = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
    return grafico
