from dash import Dash, html, dcc, Input, Output, Patch, callback
import plotly.graph_objects as go

app = Dash(__name__)

fig = go.Figure(
    [
        go.Scatter(x=[0, 1, 2, 3, 4, 5, 6, 7, 8], y=[0, 1, 3, 2, 4, 3, 4, 6, 5]),
        go.Scatter(x=[0, 1, 2, 3, 4, 5, 6, 7, 8], y=[0, 4, 5, 1, 2, 2, 3, 4, 2]),
    ],
    go.Layout(
        dict(
            annotations=[
                dict(
                    x=2,
                    y=5,
                    text="Text annotation with arrow",
                    showarrow=True,
                    arrowhead=1,
                ),
                dict(
                    x=4,
                    y=4,
                    text="Text annotation without arrow",
                    showarrow=False,
                    yshift=10,
                ),
            ]
        ),
        showlegend=False,
    ),
)

app.layout = html.Div(
    [
        html.Button("Show/Clear Annotations", id="clear-button"),
        dcc.Graph(id="clear-example", figure=fig),
    ]
)


@callback(Output("clear-example", "figure"), Input("clear-button", "n_clicks"))
def add_data_to_fig(n_clicks):
    patched_figure = Patch()
    if n_clicks and n_clicks % 2 != 0:
        patched_figure["layout"]["annotations"].clear()
    else:
        patched_figure["layout"]["annotations"].extend(
            [
                dict(
                    x=2,
                    y=5,
                    text="Text annotation with arrow",
                    showarrow=True,
                    arrowhead=1,
                ),
                dict(
                    x=4,
                    y=4,
                    text="Text annotation without arrow",
                    showarrow=False,
                    yshift=10,
                ),
            ]
        )
    return patched_figure


if __name__ == "__main__":
    app.run(debug=True)
