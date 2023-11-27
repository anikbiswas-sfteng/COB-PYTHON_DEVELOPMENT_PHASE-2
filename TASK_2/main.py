import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html

# Load sample data (replace this with your own dataset)
df = px.data.tips()

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Professional Dashboard Example"),
    
    # Chart 1: Scatter plot
    dcc.Graph(
        id='scatter-plot',
        figure=px.scatter(df, x='total_bill', y='tip', color='sex', size='size')
    ),

    # Chart 2: Bar chart
    dcc.Graph(
        id='bar-chart',
        figure=px.bar(df, x='day', y='total_bill', color='sex', barmode='group')
    ),

    # Chart 3: Line chart
    dcc.Graph(
        id='line-chart',
        figure=px.line(df, x='day', y='total_bill', color='sex', line_group='size')
    ),

    # Chart 4: Pie chart
    dcc.Graph(
        id='pie-chart',
        figure=px.pie(df, names='day', title='Distribution of meals by day')
    ),

    # Chart 5: Custom chart using Plotly graph objects
    dcc.Graph(
        id='custom-chart',
        figure=go.Figure(
            data=[
                go.Scatter(x=df['total_bill'], y=df['tip'], mode='markers', marker=dict(color='red')),
                go.Histogram(x=df['total_bill'], nbinsx=20, marker=dict(color='blue'))
            ],
            layout=dict(title='Custom Chart')
        )
    )
])
# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
