from dash import Dash, dcc, html, Input, Output, no_update, callback
import plotly.express as px

data_x = [1,2,3]
data_y = [1,2,1]
fig = px.scatter(x=data_x, y=data_y)
fig.update_traces(
    hoverinfo="none",
    hovertemplate=None,
    marker=dict(size=30)
)

app = Dash(__name__)

app.layout = html.Div(
    className="container",
    children=[
        dcc.Graph(
            id="graph-3",
            figure=fig,
            clear_on_unhover=True),
        dcc.Tooltip(
            id="graph-tooltip-3",
            background_color="darkblue",
            border_color="blue"),
    ],
)

@callback(
    Output("graph-tooltip-3", "show"),
    Output("graph-tooltip-3", "bbox"),
    Output("graph-tooltip-3", "children"),
    Input("graph-3", "hoverData"),
)
def update_tooltip_content(hoverData):
    if hoverData is None:
        return no_update

    pt = hoverData["points"][0]
    bbox = pt["bbox"]

    children = [
        html.P(f"x: {pt['x']}, y: {pt['y']}")
    ]

    return True, bbox, children

if __name__ == "__main__":
    app.run(debug=True)
