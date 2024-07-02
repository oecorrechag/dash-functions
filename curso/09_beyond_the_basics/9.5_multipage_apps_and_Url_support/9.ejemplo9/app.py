from dash import Dash, dcc, html, Input, Output, callback

from layouts import layout_home, layout1, layout2
import callbacks

app = Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@callback(Output('page-content', 'children'),
          Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return layout_home
    elif pathname == '/page1':
        return layout1
    elif pathname == '/page2':
        return layout2
    else:
        return '404'


if __name__ == '__main__':
    app.run(debug=True)
    