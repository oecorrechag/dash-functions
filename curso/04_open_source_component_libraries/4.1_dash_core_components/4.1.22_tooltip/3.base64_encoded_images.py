import io
import base64

from dash import Dash, dcc, html, Input, Output, no_update, callback
import plotly.express as px

from PIL import Image

data_x = [1,1,2,2]
data_y = [1,2,1,2]
fig = px.scatter(x=data_x, y=data_y)
fig.update_traces(
    hoverinfo="none",
    hovertemplate=None,
    marker=dict(size=30)
)
fig.update_layout(
    xaxis=dict(range=[-1,4]),
    yaxis=dict(range=[-1,4])
)

# Set up the app now
app = Dash(__name__)

app.layout = html.Div(
    className="container",
    children=[
        dcc.Graph(id="graph-2-dcc", figure=fig, clear_on_unhover=True),
        dcc.Tooltip(id="graph-tooltip-2", direction='bottom'),
    ],
)

@callback(
    Output("graph-tooltip-2", "show"),
    Output("graph-tooltip-2", "bbox"),
    Output("graph-tooltip-2", "children"),
    Output("graph-tooltip-2", "direction"),

    Input("graph-2-dcc", "hoverData"),
)
def display_hover(hoverData):
    if hoverData is None:
        return False, no_update, no_update, no_update

    # Load image with pillow
    image_path = 'dash_docs/assets/images/sample.jpg'
    im = Image.open(image_path)

    # dump it to base64
    buffer = io.BytesIO()
    im.save(buffer, format="jpeg")
    encoded_image = base64.b64encode(buffer.getvalue()).decode()
    im_url = "data:image/jpeg;base64, " + encoded_image

    # demo only shows the first point, but other points may also be available
    hover_data = hoverData["points"][0]
    bbox = hover_data["bbox"]

    # control the position of the tooltip
    y = hover_data["y"]
    direction = "bottom" if y > 1.5 else "top"

    children = [
        html.Img(
            src=im_url,
            style={"width": "150px"},
        ),
        html.P("Image from base64 string"),
    ]

    return True, bbox, children, direction

if __name__ == "__main__":
    app.run(debug=True)
