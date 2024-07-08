from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import random

app = Dash(__name__)

app.layout = html.Div(
    [
        html.Button("Update Graph Color", id="update-color-button"),
        dcc.Graph(id="update-color-fig"),
    ]
)


@callback(
    Output("update-color-fig", "figure"),
    Input("update-color-button", "n_clicks"),
)
def my_callback(n_clicks):
    df = px.data.iris()
    fig = px.scatter(
    df, title="Updating Title Color", x="sepal_length", y="sepal_width", color="species"
    )
    if n_clicks:
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        new_color = f"rgb({red}, {green}, {blue})"
        fig.update_layout(
            title_font_color=new_color,
        )
    # Here we return the entire figure, though we've just updated the title font color
    return fig

if __name__ == "__main__":
    app.run(debug=True)
