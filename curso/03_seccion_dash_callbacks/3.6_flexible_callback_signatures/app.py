from dash import Dash, html, dcc, callback, ctx, Output, Input
import plotly.express as px
import pandas as pd

app = Dash()

app.layout = [
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    html.Button(id="btn-1", children="Run Job!"),
    html.Button(id="btn-2", children="Run Job2!"),
    html.Button(id="btn-3", children="Run Job3!"),
]

def display(all_inputs):
    c = ctx.args_grouping.all_inputs
    if c.btn1.triggered:
        return f"Button 1 clicked {c.btn1.value} times"
    elif c.btn2.triggered:
        return f"Button 2 clicked {c.btn2.value} times"
    elif c.btn3.triggered:
        return f"Button 3 clicked {c.btn3.value} times"

if __name__ == '__main__':
    app.run(debug=True)