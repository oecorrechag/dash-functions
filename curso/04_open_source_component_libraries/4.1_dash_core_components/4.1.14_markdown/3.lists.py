from dash import Dash, dcc

app = Dash(__name__)


app.layout = dcc.Markdown('''
    * Item 1
    * Item 2
    * Item 2a
    * Item 2b
''')


if __name__ == '__main__':
    app.run(debug=True)
