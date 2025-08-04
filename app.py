import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load processed data
df = pd.read_csv("output.csv")

# Convert date column to datetime for sorting
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

# Group by date to get total sales per day
daily_sales = df.groupby('date')['sales'].sum().reset_index()

#Dash app
app = dash.Dash(__name__)

# layout
app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales Over Time', style={'textAlign': 'center'}),

    dcc.Graph(
        id='sales-line-chart',
        figure=px.line(
            daily_sales,
            x='date',
            y='sales',
            title='Sales Before and After Price Increase (Jan 15, 2021)',
            labels={'date': 'Date', 'sales': 'Total Sales ($)'},
        )
    )
])

# Run server
if __name__ == '__main__':
    app.run(debug=True)
