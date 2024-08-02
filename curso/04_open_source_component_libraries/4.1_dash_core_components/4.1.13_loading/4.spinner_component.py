import time
from dash import Dash, Input, Output, callback, html, dcc, no_update
import plotly.express as px
import dash_bootstrap_components as dbc

data_canada = px.data.gapminder().query("country == 'Canada'")

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        dbc.Button("Start", id="custom-spinner-button", n_clicks=0),
        html.Hr(),
        dcc.Loading(
            [dcc.Graph(id="custom-spinner-output", figure=px.line(data_canada, x="year", y="pop"))],
            overlay_style={"visibility":"visible", "opacity": .5, "backgroundColor": "white"},
            custom_spinner=html.H2(["My Custom Spinner", dbc.Spinner(color="danger")]),
        ),
    ]
)


@callback(
    Output("custom-spinner-output", "figure"),
    Input("custom-spinner-button", "n_clicks"),
)
def load_output(n):
    if n:
        time.sleep(1)
        return px.bar(data_canada, x="year", y="pop")
    return no_update

if __name__ == "__main__":
    app.run(debug=True)
