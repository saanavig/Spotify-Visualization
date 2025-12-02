import pandas as pd
import plotly.express as px
from dash import Input, Output

df = pd.read_csv("../data/cleanDataset.csv")

def register_callbacks(app):

    @app.callback(
        Output("valence-scatter", "figure"),
        [
            Input("feature-dropdown", "value"),
            Input("genre-dropdown", "value"),
        ]
    )
    def update_graph(feature, genre):

        # filter by genre if selected
        d = df if genre is None else df[df["genre"] == genre]

        sample = d.sample(min(3000, len(d)), random_state=42)

        fig = px.scatter(
            sample,
            x=feature,
            y="valence",
            color=None if genre else "genre",
            opacity=0.35,
            title=f"Valence vs {feature.capitalize()}",
            color_discrete_sequence=px.colors.qualitative.Set2,
        )

        # global trendline
        trend = px.scatter(
            sample,
            x=feature,
            y="valence",
            trendline="ols"
        ).data[1]

        trend.line.color = "black"
        trend.line.width = 3
        trend.name = "Trendline"

        fig.add_trace(trend)

        fig.update_layout(
            height=850,
            template="simple_white",
            margin=dict(l=40, r=40, t=80, b=40),
            legend=dict(
                title="Genre" if not genre else "",
                bgcolor="rgba(255,255,255,0.7)",
            ),
        )

        fig.update_traces(marker=dict(size=6, opacity=0.4))
        return fig
