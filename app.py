import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Load and sort the data
df = pd.read_csv('./data/formatted_daily_sales.csv')
df = df.sort_values(by='date')

# Initialize the Dash app
app = dash.Dash(__name__)

# Create the line chart figure
fig = px.line(
    df, 
    x='date', 
    y='sales', 
    title='Pink Morsel Sales Over Time',
    labels={'sales': 'Sales ($)', 'date': 'Date'},
    color='region'
)

# Define the app layout
app.layout = html.Div(children=[
    html.H1(
        children='Pink Morsel Sales Visualizer', 
        style={'textAlign': 'center', 'fontFamily': 'Arial, sans-serif'}
    ),
    
    html.Div(
        children='Observe the impact of the January 15th, 2021 price increase on sales.', 
        style={'textAlign': 'center', 'fontFamily': 'Arial, sans-serif', 'marginBottom': '20px'}
    ),
    
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
