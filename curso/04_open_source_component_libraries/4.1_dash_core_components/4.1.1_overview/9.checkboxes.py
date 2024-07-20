from dash import Dash, dcc, html

app = Dash(__name__)

app.layout = html.Div([
    dcc.Checklist(['New York City', 'Montréal', 'San Francisco'],
                  ['Montréal', 'San Francisco'])
])

if __name__ == '__main__':
    app.run(debug=True)
