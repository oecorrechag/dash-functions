from dash import Dash, dcc

app = Dash(__name__)


app.layout = dcc.Markdown('''
    *This text will be italic*

    _This will also be italic_


    **This text will be bold**

    __This will also be bold__

    _You **can** combine them_
''')


if __name__ == '__main__':
    app.run(debug=True)
