from dash import Dash, dcc, html

app = Dash(__name__)

app.layout = html.Div([
    dcc.Textarea(
        id="textarea_id",
        value="Copy and paste here",
        style={"height": 100},
    ),
    dcc.Clipboard(
        target_id="textarea_id",
        title="copy",
        style={
            "display": "inline-block",
            "fontSize": 20,
            "verticalAlign": "top",
        },
    ),
])

if __name__ == "__main__":
    app.run(debug=True)
    