from dash import Dash, dcc

app = Dash(__name__)

app.layout = dcc.Markdown('''
    [Dash User Guide](/)
''',
    link_target="_blank",
)


if __name__ == "__main__":
    app.run(debug=True)
