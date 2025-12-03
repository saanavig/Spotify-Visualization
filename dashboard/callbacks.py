import pandas as pd
import plotly.express as px
from dash import Input, Output, html

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

    @app.callback(
        Output("feature-distribution", "figure"),
        [
            Input("feature-dropdown", "value"),
            Input("genre-dropdown", "value"),
        ]
    )
    def update_distribution(feature, genre):

        # filter
        d = df if genre is None else df[df["genre"] == genre]

        # histogram
        fig = px.histogram(
            d,
            x=feature,
            nbins=40,
            opacity=0.75,
            color="genre" if genre is None else None,
            title=f"Distribution of {feature.capitalize()}",
            color_discrete_sequence=px.colors.qualitative.Set2,
        )

        fig.update_layout(
            height=550,
            template="simple_white",
            margin=dict(l=40, r=40, t=60, b=40)
        )

        return fig

    # genre comparsion

    @app.callback(
        Output("genre-comparison-chart", "figure"),
        [
            Input("feature-dropdown", "value"),
            Input("genreA-dropdown", "value"),
            Input("genreB-dropdown", "value"),
        ]
    )
    def compare_genres(feature, genreA, genreB):

        # filter
        dA = df[df["genre"] == genreA]
        dB = df[df["genre"] == genreB]

        # Build summary for bar plot
        summary_df = pd.DataFrame({
            "genre": [genreA, genreB],
            feature: [dA[feature].mean(), dB[feature].mean()]
        })

        # bar chart
        fig = px.bar(
            summary_df,
            x="genre",
            y=feature,
            color="genre",
            title=f"Average {feature.capitalize()} — {genreA} vs {genreB}",
            color_discrete_sequence=px.colors.qualitative.Set2,
            text=feature
        )

        fig.update_traces(
            texttemplate='%{text:.3f}',
            textposition='outside'
        )

        fig.update_layout(
            height=550,
            template="simple_white",
            margin=dict(l=40, r=40, t=70, b=40),
            showlegend=False,
            yaxis_title=feature.capitalize(),
        )

        return fig
    
    @app.callback(
        Output("genre-radar-chart", "figure"),
        Input("radar-genre-dropdown", "value")
    )
    def update_radar_chart(selected_genre):

        d = df[df["genre"] == selected_genre]

        # key features
        radar_features = [
            "danceability",
            "energy",
            "valence",
            "acousticness",
            "instrumentalness",
            "speechiness",
            "loudness"
        ]

        # mean
        values = []
        for f in radar_features:
            if f == "loudness":
                values.append((d[f].mean() + 60) / 60)  # scale to 0–1
            else:
                values.append(d[f].mean())

        # radar-friendly dataframe
        radar_df = pd.DataFrame({
            "feature": radar_features,
            "value": values
        })

        fig = px.line_polar(
            radar_df,
            r="value",
            theta="feature",
            line_close=True,
            title=f"Radar Profile for {selected_genre}",
            range_r=[0, 1],
        )

        fig.update_traces(fill="toself")

        fig.update_layout(
            height=650,
            template="simple_white",
            margin=dict(l=40, r=40, t=80, b=40)
        )

        return fig

    # heatmap
    @app.callback(
        Output("correlation-heatmap", "figure"),
        Input("heatmap-genre-dropdown", "value")
    )
    def update_heatmap(selected_genre):

        # Filter dataset if a genre is chosen
        d = df if selected_genre is None else df[df["genre"] == selected_genre]

        # Features to include
        features = [
            "danceability", "energy", "valence", "acousticness",
            "instrumentalness", "speechiness", "loudness",
            "tempo", "duration_ms", "popularity"
        ]

        corr = d[features].corr()

        fig = px.imshow(
            corr,
            text_auto=True,
            color_continuous_scale="RdBu_r",
            title="Correlation Heatmap" if selected_genre is None else f"Correlation Heatmap — {selected_genre}",
            aspect="auto"
        )

        fig.update_layout(
            height=650,
            template="simple_white",
            margin=dict(l=40, r=40, t=80, b=40),
            coloraxis_colorbar=dict(
                title="Correlation",
                ticks="outside"
            )
        )

        return fig
    
    # track search

    @app.callback(
        Output("track-profile-plot", "figure"),
        Input("track-dropdown", "value")
    )
    def update_track_profile(track_name):

        if track_name is None:
            return px.scatter(title="Select a track to display its feature profile.")

        # Get the selected track row
        row = df[df["track_name"] == track_name].iloc[0]

        # Features to display
        features = [
            "danceability", "energy", "valence", "acousticness",
            "instrumentalness", "speechiness", "loudness",
            "tempo", "duration_ms", "popularity"
        ]

        # Normalize loudness + tempo + duration to 0–1 for radar
        normalized = row.copy()
        normalized["loudness"] = (row["loudness"] + 60) / 60  # loudness: -60 to 0
        normalized["tempo"] = row["tempo"] / 220               # approx max tempo
        normalized["duration_ms"] = row["duration_ms"] / df["duration_ms"].max()

        radar_values = [normalized[f] for f in features]

        fig = px.line_polar(
            r=radar_values,
            theta=[f.capitalize() for f in features],
            line_close=True,
            title=f"Feature Profile — {track_name}",
        )

        fig.update_traces(fill="toself")

        fig.update_layout(
            height=650,
            template="simple_white",
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 1]),
            ),
            margin=dict(l=40, r=40, t=80, b=40),
        )

        return fig