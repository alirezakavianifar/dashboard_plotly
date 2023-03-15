from dash import Dash, html, dcc
from dash.dependencies import Input, Output


app = Dash(__name__)

app.layout = html.Div([
    'Pick a Country',
    dcc.Dropdown(
        options=['USA','India','China','Iran'],
                 value='USA',
                 id='country-dropdown'),
    html.H3(id='country-output')
])


@app.callback(
    Output('country-output', 'children'), 
    Input('country-dropdown', 'value')
)
def country_picker(country):
    return f'I live in {country}'


if __name__ == '__main__':
    app.run_server()
