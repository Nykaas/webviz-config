import dash_html_components as html
from webviz_config import WebvizPluginABC
import dash
import dash_core_components as dcc
import pandas as pd




class DummyClass2(WebvizPluginABC):
    
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')

    @property
    def layout(self):
        return html.Div([
                html.Label('Dropdown'),
                dcc.Dropdown(
                    options=[
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': u'Montréal', 'value': 'MTL'},
                        {'label': 'San Francisco', 'value': 'SF'}
                    ],
                    value='MTL'
                ),

                html.Label('Multi-Select Dropdown'),
                dcc.Dropdown(
                    options=[
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': u'Montréal', 'value': 'MTL'},
                        {'label': 'San Francisco', 'value': 'SF'}
                    ],
                    value=['MTL', 'SF'],
                    multi=True
                ),

                html.Label('Radio Items'),
                dcc.RadioItems(
                    options=[
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': u'Montréal', 'value': 'MTL'},
                        {'label': 'San Francisco', 'value': 'SF'}
                    ],
                    value='MTL'
                ),

                html.Label('Checkboxes'),
                dcc.Checklist(
                    options=[
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': u'Montréal', 'value': 'MTL'},
                        {'label': 'San Francisco', 'value': 'SF'}
                    ],
                    value=['MTL', 'SF']
                ),

                html.Label('Text Input'),
                dcc.Input(value='MTL', type='text'),

                html.Label('Slider'),
                dcc.Slider(
                    min=0,
                    max=9,
                    marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
                    value=5,
                ),
            ], style={'columnCount': 2})











