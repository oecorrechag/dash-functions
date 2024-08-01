import time
from dash import Dash, Input, Output, callback, html, dcc, no_update
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        dbc.Button("Start", id="loading-overlay-button", n_clicks=0),
        dcc.Loading(
            [dbc.Alert("My Data", id="loading-overlay-output", className="h4 p-4 mt-3")],
            overlay_style={"visibility":"visible", "filter": "blur(2px)"},
            type="circle",
        ),
    ]
)


@callback(
    Output("loading-overlay-output", "children"),
    Input("loading-overlay-button", "n_clicks"),
)
def load_output(n):
    if n:
        time.sleep(1)
        return f"Data updated {n} times."
    return no_update

if __name__ == "__main__":
    app.run(debug=True)
