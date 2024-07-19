from dash import Dash, dcc, html

app = Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(['New York City', 'Montréal', 'San Francisco'], 'Montréal', multi=True)
])

if __name__ == '__main__':
    app.run(debug=True)
    