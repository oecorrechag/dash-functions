import time
from dash import Dash, Input, Output, callback, html, dcc

app = Dash()
app.layout = html.Div(
    [
        html.Button("Load div 1", id="loading-target-button1", n_clicks=0),
        html.Button("Load div 2", id="loading-target-button2", n_clicks=0),
        html.Hr(),
        dcc.Loading([
            html.Div(id="loading-target-output1"),
            html.Div(id="loading-target-output2"),
        ], target_components={"loading-target-output1": "children"}),
    ]
)


@callback(
    Output("loading-target-output1", "children"),
    Input("loading-target-button1", "n_clicks"),
)
def load_output(n):
    if n:
        time.sleep(2)
        return f"Output loaded {n} times.  This callback triggers the loading spinner"
    return "Callback 1 output not reloaded yet"



@app.callback(
    Output("loading-target-output2", "children"),
    Input("loading-target-button2", "n_clicks"),
)
def load_output(n):
    if n:
        time.sleep(.5)
        return f"Output loaded {n} times.  No  loading spinner"
    return "Callback 2 output not reloaded yet"

app.run(debug=True)
