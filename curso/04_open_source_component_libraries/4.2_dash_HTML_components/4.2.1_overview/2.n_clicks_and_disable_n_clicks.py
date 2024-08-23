from dash import Dash, html, Input, Output, callback

app = Dash(__name__)

app.layout = html.Div(
    [
        html.Div(
            "Div without n_clicks event listener",
            id="click-div-2",
            disable_n_clicks=True,
            style={"color": "red", "font-weight": "bold"},
        ),
        html.P(id="click-output-2", disable_n_clicks=True),
    ]
)


@callback(
    Output("click-output-2", "children"),
    Input("click-div-2", "n_clicks")
    )
def click_counter(n_clicks):
    return f"The html.Div above has been clicked this many times: {n_clicks}"


app.run(debug=True)
