from dash import html, dcc
import pandas as pd

df = pd.read_csv("../data/cleanDataset.csv")

def create_layout(app):

    return html.Div(
        style={
            "padding": "30px",
            "fontFamily": "Inter, sans-serif",
            "maxWidth": "1100px",
            "margin": "0 auto"
        },
        children=[

            # title
            html.H1(
                "Spotify Music Analytics Dashboard",
                style={
                    "textAlign": "center",
                    "marginBottom": "25px",
                },
            ),

            # feature & genre selection
            html.Div(
                style={
                    "display": "flex",
                    "gap": "20px",
                    "justifyContent": "center",
                    "marginBottom": "25px",
                },
                children=[

                    # feature Dropdown
                    html.Div(
                        style={"width": "300px"},
                        children=[
                            html.Label("Select Feature:", style={"fontWeight": "600"}),
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
                                value="danceability",
                                clearable=False,
                            )
                        ],
                    ),

                    # genre Dropdown
                    html.Div(
                        style={"width": "300px"},
                        children=[
                            html.Label("Select Genre (Optional):", style={"fontWeight": "600"}),
                            dcc.Dropdown(
                                id="genre-dropdown",
                                options=[{"label": g, "value": g} for g in sorted(df["genre"].unique())],
                                value=None,
                                placeholder="All Genres",
                                clearable=True,
                            )
                        ],
                    ),

                ],
            ),

            # scatter plot
            html.Div(
                dcc.Graph(id="valence-scatter"),
                style={
                    "backgroundColor": "white",
                    "padding": "25px",
                    "borderRadius": "12px",
                    "boxShadow": "0 2px 18px rgba(0,0,0,0.07)",
                    "minHeight": "900px",
                },
            ),

            # histogram
            html.Div(
                dcc.Graph(id="feature-distribution"),
                style={
                    "backgroundColor": "white",
                    "padding": "25px",
                    "borderRadius": "12px",
                    "boxShadow": "0 2px 18px rgba(0,0,0,0.07)",
                    "marginTop": "40px",
                    "minHeight": "600px"
                },
            ),

            # genre comparison
            html.H2(
                "Genre Comparison",
                style={
                    "marginTop": "50px",
                    "marginBottom": "15px",
                    "textAlign": "center"
                }
            ),

            html.Div(
                style={
                    "display": "flex",
                    "gap": "20px",
                    "justifyContent": "center",
                    "marginBottom": "25px",
                },
                children=[

                    # first genre
                    html.Div(
                        style={"width": "300px"},
                        children=[
                            html.Label("Select Genre A:", style={"fontWeight": "600"}),
                            dcc.Dropdown(
                                id="genreA-dropdown",
                                options=[{"label": g, "value": g} for g in sorted(df["genre"].unique())],
                                value="Pop",
                                clearable=False,
                            )
                        ],
                    ),

                    # second genre
                    html.Div(
                        style={"width": "300px"},
                        children=[
                            html.Label("Select Genre B:", style={"fontWeight": "600"}),
                            dcc.Dropdown(
                                id="genreB-dropdown",
                                options=[{"label": g, "value": g} for g in sorted(df["genre"].unique())],
                                value="Rock",
                                clearable=False,
                            )
                        ],
                    ),
                ],
            ),

            #heatmap
            html.Div(
                dcc.Graph(id="genre-comparison-chart"),
                style={
                    "backgroundColor": "white",
                    "padding": "25px",
                    "borderRadius": "12px",
                    "boxShadow": "0 2px 18px rgba(0,0,0,0.07)",
                    "minHeight": "600px",
                },
            ),

            # radar chart
            html.H2(
                "Genre Feature Profile (Radar Chart)",
                style={
                    "marginTop": "50px",
                    "marginBottom": "15px",
                    "textAlign": "center"
                }
            ),

            html.Div(
                style={
                    "width": "300px",
                    "margin": "0 auto 25px",
                },
                children=[
                    html.Label("Select Genre:", style={"fontWeight": "600"}),
                    dcc.Dropdown(
                        id="radar-genre-dropdown",
                        options=[{"label": g, "value": g} for g in sorted(df["genre"].unique())],
                        value="Pop",
                        clearable=False,
                    ),
                ],
            ),

            html.Div(
                dcc.Graph(id="genre-radar-chart"),
                style={
                    "backgroundColor": "white",
                    "padding": "25px",
                    "borderRadius": "12px",
                    "boxShadow": "0 2px 18px rgba(0,0,0,0.07)",
                    "minHeight": "650px",
                },
            ),

            html.H2(
                "Correlation Heatmap",
                style={
                    "marginTop": "50px",
                    "marginBottom": "15px",
                    "textAlign": "center"
                }
            ),

            html.Div(
                style={
                    "width": "300px",
                    "margin": "0 auto 25px",
                },
                children=[
                    html.Label("Select Genre (Optional):", style={"fontWeight": "600"}),
                    dcc.Dropdown(
                        id="heatmap-genre-dropdown",
                        options=[{"label": g, "value": g} for g in sorted(df["genre"].unique())],
                        value=None,
                        clearable=True,
                        placeholder="All Genres"
                    ),
                ],
            ),

            html.Div(
                dcc.Graph(id="correlation-heatmap"),
                style={
                    "backgroundColor": "white",
                    "padding": "25px",
                    "borderRadius": "12px",
                    "boxShadow": "0 2px 18px rgba(0,0,0,0.07)",
                    "minHeight": "650px",
                },
            ),

            # track search option'

            html.H2(
                "Track Search & Feature Profile",
                style={
                    "marginTop": "60px",
                    "textAlign": "center",
                }
            ),

            html.Div(
                style={
                    "width": "400px",
                    "margin": "0 auto 25px",
                    "textAlign": "center"
                },
                children=[
                    html.Label("Search Track:", style={"fontWeight": "600"}),
                    dcc.Dropdown(
                        id="track-dropdown",
                        options=[{"label": name, "value": name} for name in sorted(df["track_name"].unique())],
                        placeholder="Type or scroll to select a track...",
                        multi=False,
                        value=None,
                    ),
                ],
            ),

            html.Div(
                [
                    dcc.Graph(id="track-profile-plot"),
                ],
                style={
                    "backgroundColor": "white",
                    "padding": "25px",
                    "borderRadius": "12px",
                    "boxShadow": "0 2px 18px rgba(0,0,0,0.07)",
                    "minHeight": "650px",
                    "marginBottom": "35px"
                },
            ),
    ],
    )
