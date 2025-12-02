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

            html.H1(
                "Spotify Music Analytics Dashboard",
                style={
                    "textAlign": "center",
                    "marginBottom": "25px",
                },
            ),

            # Dropdown container
            html.Div(
                style={
                    "display": "flex",
                    "gap": "20px",
                    "justifyContent": "center",
                    "marginBottom": "25px",
                },
                children=[

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
        ],
    )
