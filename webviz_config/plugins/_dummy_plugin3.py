import dash_html_components as html
from webviz_config import WebvizPluginABC
import dash
import dash_core_components as dcc
import pandas as pd




class DummyClass3(WebvizPluginABC):
    
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    
    


    
    @property
    def layout(self):
        df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')
        def generate_table(dataframe, max_rows=10):
            return html.Table([
                html.Thead(
                    html.Tr([html.Th(col) for col in dataframe.columns])
                ),
                html.Tbody([
                    html.Tr([
                        html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
                    ]) for i in range(min(len(dataframe), max_rows))
                ])
            ])
        return html.Div(children=[
            html.H4(children='US Agriculture Exports (2011)'), 
            generate_table(df)
        ])














