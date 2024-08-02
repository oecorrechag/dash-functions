import time
from dash import Dash, Input, Output, callback, html, dcc, no_update

app = Dash()

app.layout = html.Div(
    [
        html.Div("Select mode"),
        html.Button("Start", id="loading-display-button", n_clicks=0),
        dcc.Dropdown(["auto", "show", "hide"], value="auto", id="dd-display", clearable=False, style={"marginBottom": 50}),
        dcc.Loading(
            html.Div("Demo of manually controlling  loading status", id="loading-display-output"),
            id="loading-display"
        ),
    ]
)

@callback(
    Output("loading-display", "display"),
    Input("dd-display", "value")
)
def update_display(display):
    return display


@app.callback(
    Output("loading-display-output", "children"),
    Input("loading-display-button", "n_clicks"),
)
def load_output(n):
    if n:
        time.sleep(2)
        return f"Updated content {n}"
    return no_update


app.run(debug=True)
