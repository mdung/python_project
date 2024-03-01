import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import requests

# Function to fetch COVID-19 data
def get_covid_data():
    url = "https://corona.lmao.ninja/v2/all"
    response = requests.get(url)
    data = response.json()
    return data

# Function to create a simple dashboard layout
def create_dashboard_layout():
    return html.Div([
        html.H1("COVID-19 Dashboard"),

        dcc.Interval(
            id='interval-component',
            interval=60 * 1000,  # in milliseconds
            n_intervals=0
        ),

        dcc.Graph(id='world-map'),
        dcc.Graph(id='bar-chart'),

        html.Div([
            html.P("Total Cases: "),
            html.P(id='total-cases'),
            html.P("Total Deaths: "),
            html.P(id='total-deaths'),
            html.P("Total Recovered: "),
            html.P(id='total-recovered'),
        ]),
    ])

# Function to update dashboard data
def update_dashboard_data():
    data = get_covid_data()
    total_cases = f"{data['cases']:,}"
    total_deaths = f"{data['deaths']:,}"
    total_recovered = f"{data['recovered']:,}"

    return total_cases, total_deaths, total_recovered

# Function to update world map and bar chart
def update_charts():
    url = "https://corona.lmao.ninja/v2/countries?sort=cases"
    response =     requests.get(url)
    countries_data = response.json()

    # Create a DataFrame from the API response
    df = pd.DataFrame(countries_data)

    # World map visualization
    world_map = px.scatter_geo(df, locations="country", locationmode="country names",
                               color="cases", size="cases", hover_name="country",
                               color_continuous_scale="Viridis",
                               title="COVID-19 World Map")

    # Bar chart visualization
    bar_chart = px.bar(df.head(10), x="country", y="cases",
                       title="Top 10 Countries with Most Cases")

    return world_map, bar_chart

# Create the Dash app
app = dash.Dash(__name__)
app.layout = create_dashboard_layout()

# Callback to update data and charts every minute
@app.callback(
    [Output('total-cases', 'children'),
     Output('total-deaths', 'children'),
     Output('total-recovered', 'children'),
     Output('world-map', 'figure'),
     Output('bar-chart', 'figure')],
    [Input('interval-component', 'n_intervals')]
)
def update_dashboard(n_intervals):
    total_cases, total_deaths, total_recovered = update_dashboard_data()
    world_map, bar_chart = update_charts()

    return total_cases, total_deaths, total_recovered, world_map, bar_chart

if __name__ == '__main__':
    app.run_server(debug=True)

