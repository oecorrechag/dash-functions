from dash import Dash, dcc

app = Dash(__name__)


app.layout = dcc.Markdown('''

    # This is an <h1> tag

    ## This is an <h2> tag

    ###### This is an <h6> tag
''')


if __name__ == '__main__':
    app.run(debug=True)
