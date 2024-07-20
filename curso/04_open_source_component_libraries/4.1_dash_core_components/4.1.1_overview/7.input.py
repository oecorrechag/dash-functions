from dash import Dash, dcc, html

app = Dash(__name__)

app.layout = html.Div([
    dcc.Input(
        placeholder='Enter a value...',
        type='text',
        value=''
    )
])

if __name__ == '__main__':
    app.run(debug=True)
