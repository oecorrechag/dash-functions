from dash import Dash, dcc, html

app = Dash(__name__)

app.layout = html.Div([
    dcc.Slider(0, 9, marks={i: f'Label{i}' for i in range(10)}, value=5)
])

if __name__ == '__main__':
    app.run(debug=True)
    