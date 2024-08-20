from dash import Dash, dcc, html, Input, Output, no_update, callback, clientside_callback
import plotly.express as px
import time

data_x = [1,1,2,2]
data_y = [1,2,1,2]
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
            id="graph-4",
            figure=fig,
            clear_on_unhover=True),
        dcc.Tooltip(
            id="graph-tooltip-4",
            loading_text="LOADING",
            direction="bottom"),
    ],
)

# This callback is executed very quickly
clientside_callback(
    """
    function show_tooltip(hoverData) {
        if(!hoverData) {
            return [false, dash_clientside.no_update];
        }
        var pt = hoverData.points[0];
        return [true, pt.bbox];
    }
    """,
    Output("graph-tooltip-4", "show"),
    Output("graph-tooltip-4", "bbox"),
    Input("graph-4", "hoverData"),
)

# This callback is executed after 1s to simulate a long-running process
@callback(
    Output("graph-tooltip-4", "children"),
    Input("graph-4", "hoverData"),
)
def update_tooltip_content(hoverData):
    if hoverData is None:
        return no_update

    time.sleep(1)

    # Display the x0 and y0 coordinate
    bbox = hoverData["points"][0]["bbox"]
    return [
        html.P(f"x0={bbox['x0']}, y0={bbox['y0']}"),
    ]

if __name__ == "__main__":
    app.run(debug=True)
