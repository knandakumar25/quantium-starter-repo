import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Load and sort the data
df = pd.read_csv('./data/formatted_daily_sales.csv')
df = df.sort_values(by='date')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define a color palette for our styling
colors = {
    'background': '#1e1e1e',
    'surface': '#2d2d2d',
    'text': '#f5f5f5',
    'accent': '#ff66b2',  # Pink color for Pink Morsels
    'border': '#444444'
}

# Define the app layout
app.layout = html.Div(style={
    'backgroundColor': colors['background'], 
    'minHeight': '100vh', 
    'padding': '40px', 
    'fontFamily': '"Segoe UI", Tahoma, Geneva, Verdana, sans-serif'
}, children=[
    
    # Header Section
    html.Header(children=[
        html.H1(
            children='Pink Morsel Sales Visualizer', 
            style={'textAlign': 'center', 'color': colors['accent'], 'margin': '0 0 10px 0', 'fontSize': '2.5rem'}
        ),
        html.P(
            children='Observe the impact of the January 15th, 2021 price increase on sales.', 
            style={'textAlign': 'center', 'color': colors['text'], 'fontSize': '1.2rem', 'margin': '0'}
        ),
    ], style={
        'paddingBottom': '30px', 
        'borderBottom': f'2px solid {colors["border"]}', 
        'marginBottom': '40px'
    }),
    
    # Controls Section
    html.Div(children=[
        html.Label(
            'Select Region:', 
            style={'color': colors['text'], 'fontWeight': 'bold', 'marginRight': '20px', 'fontSize': '1.1rem'}
        ),
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': ' North', 'value': 'north'},
                {'label': ' East', 'value': 'east'},
                {'label': ' South', 'value': 'south'},
                {'label': ' West', 'value': 'west'},
                {'label': ' All Regions', 'value': 'all'}
            ],
            value='all',
            inline=True,
            style={'color': colors['text'], 'display': 'inline-block'},
            labelStyle={'marginRight': '25px', 'cursor': 'pointer', 'fontSize': '1.1rem'}
        )
    ], style={
        'textAlign': 'center', 
        'marginBottom': '40px', 
        'backgroundColor': colors['surface'], 
        'padding': '20px', 
        'borderRadius': '12px',
        'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.3)'
    }),
    
    # Chart Section
    html.Div(children=[
        dcc.Graph(id='sales-line-chart')
    ], style={
        'boxShadow': '0 8px 16px rgba(0, 0, 0, 0.4)', 
        'borderRadius': '12px', 
        'overflow': 'hidden',
        'backgroundColor': colors['surface']
    })
])

# Callback to update the graph based on the selected region
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    # Filter the dataframe based on the radio button value
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]
    
    # Generate the line chart
    fig = px.line(
        filtered_df, 
        x='date', 
        y='sales', 
        title=f'Sales Over Time ({selected_region.capitalize()})',
        labels={'sales': 'Sales ($)', 'date': 'Date', 'region': 'Region'},
        color='region' if selected_region == 'all' else None,
        template='plotly_dark'  # Use Plotly's dark theme to match our CSS
    )
    
    # Customize the figure layout to perfectly match our app's color palette
    fig.update_layout(
        plot_bgcolor=colors['surface'],
        paper_bgcolor=colors['surface'],
        font_color=colors['text'],
        title_font_color=colors['accent'],
        title_font_size=24,
        title_x=0.5,
        margin=dict(l=60, r=40, t=80, b=60),
        xaxis=dict(showgrid=True, gridcolor=colors['border']),
        yaxis=dict(showgrid=True, gridcolor=colors['border'], tickprefix="$")
    )
    
    # If a specific region is selected, force the line color to be our pink accent
    if selected_region != 'all':
        fig.update_traces(line_color=colors['accent'])
        
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
