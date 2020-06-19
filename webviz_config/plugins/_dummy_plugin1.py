import dash_html_components as html
from webviz_config import WebvizPluginABC
import dash
import dash_core_components as dcc
import pandas as pd




class DummyClass1(WebvizPluginABC):
    
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')



    @property
    def layout(self):
        return html.Div([
            html.H1('This is a header', style={'textAlign': 'center', 'color': '#7FDBFF'}),
            html.Div('Small centered text under heading.', style = {'textAlign': 'center'}),
            dcc.Graph(
                id='example-graph',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Blueberries'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Oranges'},
                    ],
                    'layout': {
                        'title': 'Fruitful barplot'
                    }
                }
            )





        ])















