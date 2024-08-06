from dash import Dash, dcc

app = Dash(__name__)

app.layout = dcc.RadioItems([
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF', 'disabled': True}
    ],
    'MTL'
)

if __name__ == "__main__":
    app.run(debug=True)
