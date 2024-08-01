import time
from dash import Dash, Input, Output, callback, html, dcc, no_update

app = Dash()
app.layout = html.Div(
    [
        html.Label("Set delay_show time (ms)"),
        dcc.Input(type="number", value=0, id="delay-show", debounce=True),
        html.Label("Set delay_hide time (ms)"),
        dcc.Input(type="number", value=0, id="delay-hide", debounce=True),
        html.Hr(),
        html.Button("Load", id="loading-delay-button", n_clicks=0),
        dcc.Loading(html.Div(id="loading-delay-output"), id="loading-component"),
    ]
)


@callback(
    Output("loading-delay-output", "children"),
    Input("loading-delay-button", "n_clicks"),
)
def load_output(n):
    if n:
        time.sleep(.1)
        return f"Output loaded {n} times"
    return "Output not reloaded yet"

@callback(
    Output("loading-component", "delay_show"),
    Output("loading-component", "delay_hide"),
    Input("delay-show", "value"),
    Input("delay-hide", "value")
)
def update_delay_show_hide(show, hide):
    if show is None or hide is None:
        return no_update
    return int(show), int(hide)

app.run(debug=True)
