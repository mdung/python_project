import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import random
from datetime import datetime, timedelta
import threading

# Sample real-time data source simulation
def generate_real_time_data():
    while True:
        yield {
            'timestamp': datetime.now(),
            'metric_1': random.randint(10, 100),
            'metric_2': random.randint(50, 200),
            'metric_3': random.randint(5, 20)
        }

# Initialize Dash app
app = dash.Dash(__name__)

# Initial empty DataFrame
df = pd.DataFrame(columns=['timestamp', 'metric_1', 'metric_2', 'metric_3'])

# Layout of the dashboard
app.layout = html.Div(children=[
    html.H1("Real-Time Dashboard"),

    dcc.Graph(id='metric-1-graph'),
    dcc.Graph(id='metric-2-graph'),
    dcc.Graph(id='metric-3-graph'),

    dcc.Interval(
        id='interval-component',
        interval=1*1000,  # in milliseconds
        n_intervals=0
    )
])

# Update data and graphs in the interval callback
@app.callback(Output('metric-1-graph', 'figure'),
              Output('metric-2-graph', 'figure'),
              Output('metric-3-graph', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_graphs(n_intervals):
    global df

    # Append new data to the DataFrame
    new_data = next(generate_real_time_data())
    df = df.append(new_data, ignore_index=True)

    # Create individual graphs for each metric
    fig1 = px.line(df, x='timestamp', y='metric_1', title='Metric 1')
    fig2 = px.line(df, x='timestamp', y='metric_2', title='Metric 2')
    fig3 = px.line(df, x='timestamp', y='metric_3', title='Metric 3')

    return fig1, fig2, fig3

# Run the Dash app
if __name__ == '__main__':
    threading.Thread(target=lambda: app.run_server(debug=True, use_reloader=False)).start()
