from dash import dcc, html

dcc.Dropdown(
    [
        {
            "label": html.Span(
                [
                    html.Img(src="/assets/images/language_icons/python_50px.svg", height=20),
                    html.Span("Python", style={'font-size': 15, 'padding-left': 10}),
                ], style={'align-items': 'center', 'justify-content': 'center'}
            ),
            "value": "Python",
        },
        {
            "label": html.Span(
                [
                    html.Img(src="/assets/images/language_icons/julia_50px.svg", height=20),
                    html.Span("Julia", style={'font-size': 15, 'padding-left': 10}),
                ], style={'align-items': 'center', 'justify-content': 'center'}
            ),
            "value": "Julia",
        },
        {
            "label": html.Span(
                [
                    html.Img(src="/assets/images/language_icons/r-lang_50px.svg", height=20),
                    html.Span("R", style={'font-size': 15, 'padding-left': 10}),
                ], style={'align-items': 'center', 'justify-content': 'center'}
            ),
            "value": "R",
        },
    ],
    value="Python"
)
