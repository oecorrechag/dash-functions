# Dash-Course

New course in plotly 2024-2

## Table of Contents

- <a href='#1'>1. 01_seccion_quickstart</a>
    - <a href='#1.1'> 1.1_minimal-app</a>
    - <a href='#1.2'> 1.2_tutorial</a>
- <a href='#2'>2. 02_seccion_fundamentals</a>
    - <a href='#2.1'> 2.1_minimal-app</a>
    - <a href='#2.2'> 2.2_basic_callbacks</a>
    - <a href='#2.3'> 2.3_interactive_visualizations</a>

<hr>

## <a id='1'>1. 01_seccion_quickstart </a>

### <a id='1.2'>1.2_tutorial </a> 

# Hello World

# Initialize the app
app = Dash()

# App layout
app.layout = [html.Div(children='Hello World')]

The app layout represents the app components that will be displayed in the web browser and here is provided as a list, though it could also be a Dash component.

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

These lines are for running your app, and they are almost always the same for any Dash app you create.


Nota: El archivo 7.mantine.py no funciona








<hr>

[Go to Top](#Table-of-Contents)