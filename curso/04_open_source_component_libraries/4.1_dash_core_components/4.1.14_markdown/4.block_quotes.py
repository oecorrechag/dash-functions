from dash import Dash, dcc

app = Dash(__name__)


app.layout = dcc.Markdown('''
    >
    > Block quotes are used to highlight text.
    >
''')


if __name__ == '__main__':
    app.run(debug=True)
