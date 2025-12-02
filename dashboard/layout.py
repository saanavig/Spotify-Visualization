from dash import html, dcc
import dash

def create_layout(app):

    return html.Div(
        style={"padding": "30px", "fontFamily": "Inter, sans-serif"},
        children=[

            # Title
            html.H1(
                "Spotify Music Analytics Dashboard",
                style={
                    "textAlign": "center",
                    "marginBottom": "20px",
                },
            ),

            html.Div(
                style={"maxWidth": "400px", "margin": "0 auto 25px"},
                children=[
                    html.Label("Select Feature:", style={"fontWeight": "600"}),

                    dcc.Dropdown(
                        id="feature-dropdown",
                        options=[
                            {"label": "Danceability", "value": "danceability"},
                            {"label": "Energy", "value": "energy"},
                            {"label": "Acousticness", "value": "acousticness"},
                            {"label": "Valence", "value": "valence"},
                            {"label": "Tempo", "value": "tempo"},
                        ],
                        value="danceability",
                        clearable=False,
                        style={"borderRadius": "8px"},
                    ),

                    dcc.Dropdown(
                        id="genre-dropdown",
                        options=[{"label": g, "value": g} for g in sorted(df["genre"].unique())],
                        value=None,
                        placeholder="Select a genre (optional)"
                    )

                ],
            ),

            html.Div(
                dcc.Graph(id="valence-scatter"),
                style={
                    "backgroundColor": "white",
                    "padding": "20px",
                    "borderRadius": "12px",
                    "boxShadow": "0 2px 15px rgba(0,0,0,0.08)",
                    "marginBottom": "40px",
                },
            ),
        ],
    )
