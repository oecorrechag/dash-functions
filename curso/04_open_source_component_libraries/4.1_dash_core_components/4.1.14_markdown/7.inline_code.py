from dash import Dash, dcc

app = Dash(__name__)


app.layout = dcc.Markdown('''

Inline code snippet: `my_bool = True`

Block code snippet:
```python

def sum(a, b):
    return a+b

sum(2,2)

```''')


if __name__ == '__main__':
    app.run(debug=True)
