from dash import Dash, html, dcc

app = Dash(__name__)

app.layout = html.Div([
    dcc.RangeSlider(-5, 6,
        marks={i: f'Label{i}' for i in range(-5, 7)},
        value=[-3, 4]
    )
])

if __name__ == '__main__':
    app.run(debug=True)
    