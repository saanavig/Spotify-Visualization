import pandas as pd
from dash import Input, Output
import plotly.express as px

df = pd.read_csv("../data/cleanDataset.csv")

def register_callbacks(app):

    @app.callback(
        Output("valence-scatter", "figure"),
        Input("feature-dropdown", "value"),
    )
    def update_graph(feature):
        sample_df = df.sample(3000, random_state=42)

        fig = px.scatter(
            sample_df,
            x=feature,
            y="valence",
            color="genre",
            opacity=0.35,
            title=f"Valence vs {feature.capitalize()}",
            color_discrete_sequence=px.colors.qualitative.Set2,
        )
        # global trendline
        trend_data = px.scatter(
            sample_df,
            x=feature,
            y="valence",
            trendline="ols"
        ).data[1]

        fig.add_trace(trend_data)

        fig.update_layout(
            height=550,
            margin=dict(l=40, r=40, t=60, b=40),
            legend=dict(
                title="Genre",
                orientation="v",
                bgcolor="rgba(255,255,255,0.6)",
            ),
        )
        return fig

        # def update_scatter(feature, genre):
        # d = df

        # if genre:
        #     d = d[d["genre"] == genre]

        # fig = px.scatter(
        #     d.sample(min(3000, len(d))),
        #     x=feature,
        #     y="valence",
        #     color="genre" if not genre else None,
        #     trendline="ols",
        #     opacity=0.45,
        #     title=f"Valence vs {feature}"
        # )

        # fig.update_layout(height=600, margin=dict(l=40, r=40, t=80, b=40))
        # return fig

