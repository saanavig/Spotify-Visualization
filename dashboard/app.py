import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

df = pd.read_csv("../data/cleanDataset.csv")

# initialize app
# app = dash.Dash(__name__)
app = dash.Dash(__name__, external_stylesheets=["./styles.css"])

# Layout
app.layout = html.Div([
    html.H1("Spotify Valence Explorer Dashboard"),

    dcc.Dropdown(
        id="feature-dropdown",
        options=[
            {"label": "Danceability", "value": "danceability"},
            {"label": "Energy", "value": "energy"},
            {"label": "Acousticness", "value": "acousticness"},
            {"label": "Loudness", "value": "loudness"},
            {"label": "Tempo", "value": "tempo"},
            {"label": "Instrumentalness", "value": "instrumentalness"},
            {"label": "Speechiness", "value": "speechiness"},
        ],
        value="danceability"
    ),

    dcc.Graph(id="valence-scatter")
])

# Callback
@app.callback(
    dash.dependencies.Output("valence-scatter", "figure"),
    [dash.dependencies.Input("feature-dropdown", "value")]
)
def update_scatter(feature):
    fig = px.scatter(
        df.sample(8000),  # sampling for performance
        x=feature,
        y="valence",
        color="genre",
        trendline="ols",
        opacity=0.4,
        title=f"Valence vs {feature}"
    )
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
