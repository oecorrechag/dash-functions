from dash import Dash, dcc, html

app = Dash(__name__)

app.layout = html.Div([
    dcc.Textarea(
        placeholder='Enter a value...',
        value='This is a TextArea component',
        style={'width': '100%'}
    )
])

if __name__ == '__main__':
    app.run(debug=True)
