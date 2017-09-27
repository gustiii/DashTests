import dash
from dash.dependencies import Input, Output, Event
import dash_core_components as dcc
import dash_html_components as html
import datetime
from random import randint
import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import random

global liste
liste = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]

app = dash.Dash(__name__)
app.config['suppress_callback_exceptions']=True
app.layout = html.Div(
        
    html.Div([
            
        html.H4('LiveRandom'),
        dcc.Graph(id='live-update-graph'),
        dcc.Graph(id='live-update-graph2'),
        html.Div(id='live-update-graph3'),
        dcc.Interval(
            id='interval-component',
            interval=1*2000),
        dcc.Interval(
            id='interval-component2',
            interval=1*500),
        dcc.Interval(
            id='interval-component3',
            interval=1*50)
        
    ])
)

@app.callback(Output('live-update-graph', 'figure'),
              events=[Event('interval-component', 'interval')])
def update_graph_live():
    
    fig = plotly.tools.make_subplots(rows=1, cols=1, vertical_spacing=0.2)
    
    liste.append(random.randint(1,99))
    
    liste.pop(0)
    
    fig.append_trace({
        #'x': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,],
        'y': liste,
        'name': 'Altitude',
        'mode': 'lines+markers',
        'type': 'scatter'
    }, 1, 1)

    return (fig)

@app.callback(Output('live-update-graph2', 'figure'),
              events=[Event('interval-component2', 'interval')])
def update_graph_live():
    
    
    fig = {
      "data": [
        {
          "values": [16, 15, 12, random.randint(1,99), 5, random.randint(1,99), 43, 43, 43, 43],
          "labels": [
            "US",
            "China",
            "European Union",
            "Russian Federation",
            "Brazil",
            "India",
            "Rest of World"
          ],
          "domain": {"x": [0, .60]},
          "name": "GHG Emissions",
          "hoverinfo":"label+percent+name",
          "hole": .4,
          "type": "pie"
        }],
      "layout": {
            "title":"Global Emissions 1990-2011",
            "annotations": [
                {
                    "font": {
                        "size": 20
                    },
                    "showarrow": False,
                    "text": "CO2",
                    "x": 0.8,
                    "y": 0.5
                }
            ]
        }
    }
    return (fig)
    
@app.callback(Output('live-update-graph3', 'children'),
              events=[Event('interval-component3', 'interval')])
def text():
    
    t = datetime.datetime.now()

    return (html.H4(t))


if __name__ == '__main__':
    app.run_server(debug=True)