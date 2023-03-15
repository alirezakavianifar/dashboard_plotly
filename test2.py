from dash import html, dcc, Dash
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import plotly.express as px
import seaborn as sns
import pandas as pd

df = sns.load_dataset('anscombe')

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H3("Anscombe's Quartet"),
        dcc.Dropdown(id='dropdown', options = list(df['dataset'].unique())),
        dcc.Graph(id='visual')
    ]
)


@app.callback(
    Output('visual', 'figure'),
    Input('dropdown', 'value')
)
def interactive_visual(selection):
    fig = px.scatter(
        df.query(f"dataset == '{selection}'"),
        x='x',
        y='y'
    )
    
    return fig

if __name__ == '__main__':
    app.run_server()