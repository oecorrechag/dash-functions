from dash import Dash, dcc, html

app = Dash(__name__)

markdown = """
Lorem ipsum dolor sit amet, consectetur
adipiscing elit. Cras non lacus maximus,
tincidunt nibh in, finibus nisi. Cras
ut lacus sed lacus tempus rutrum. Integer
ut feugiat nisi, nec tempus velit.

Proin placerat erat odio, et laoreet
sapien mattis et. Curabitur laoreet imperdiet
congue. Integer congue a augue non vulputate.
Ut a leo auctor, sodales sem ac, cursus
ipsum. Fusce in est nec urna pretium
aliquet. Nunc nisl eros, blandit eu diam
convallis, elementum dictum tortor.
"""

app.layout = html.Div([
    dcc.Markdown(
        markdown,
        id="copyable-markdown",
        style={"width": 500, "height": 200, "overflow": "auto"},
    ),
    dcc.Clipboard(
        target_id="copyable-markdown",
        style={
            "position": "absolute",
            "top": 0,
            "right": 20,
            "fontSize": 15,
        },
    ),
], style={"width": 500, "height": 200, "position": "relative"})


if __name__ == "__main__":
    app.run(debug=True)
    