from dash import html
import dash_bootstrap_components as dbc

def create_about():
    return dbc.Container(
        [
            # main heading
            dbc.Container(
                [
                    html.H1(
                        "Spotify Analytics Dashboard",
                        className="display-5 fw-bold text-center",
                    ),
                    html.P(
                        """
                        This project transforms a large collection of Spotify audio features into a structured,
                        data-driven narrative. It aims to uncover relationships, trends, and patterns that define
                        modern music consumption. The dashboard showcases how quantifiable musical traits can be
                        explored and interpreted to reveal deeper insights.
                        """,
                        className="text-center lead mt-3",
                    ),
                ],
                fluid=True,
                className="py-5",
            ),

            # big picture
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H2("The Big Picture", className="fw-semibold mb-3 text-center", style={"color": "#09702D"}),
                        html.P(
                            """
                            Music can be understood not only through emotion and cultural context, but also through
                            measurable acoustic dimensions. By transforming audio signals into structured data, we
                            gain a unique opportunity to analyze music at scale and observe how listeners respond
                            to different sonic characteristics.
                            """,
                            className="mb-3",
                        ),
                        dbc.Collapse(
                            html.Div(
                                [
                                    html.P(
                                        """
                                        The dataset reveals large-scale behavioral patterns: which types of tracks
                                        tend to gain popularity, which acoustic traits dominate across genres, and how
                                        artists differentiate themselves through signature sound profiles.
                                        """
                                    ),
                                ],
                                className="mt-2"
                            ),
                            id="collapse-big-picture",
                            is_open=False,
                        ),
                        dbc.Button(
                            "Read More",
                            id="toggle-big-picture",
                            color="secondary",
                            className="mt-2",
                            n_clicks=0,
                        ),
                    ]
                ),
                className="mb-5 shadow-sm",
            ),

            # dataset details
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H2("Dataset Composition & Structure", className="fw-semibold mb-3 text-center", style={"color": "#09702D"}),
                        html.P(
                            """
                            The dataset consists of track-level metadata and audio-derived features sourced from
                            both the Spotify API and a curated Kaggle dataset. Each track includes objective,
                            quantitative measurements of acoustic characteristics.
                            """,
                            className="mb-3",
                        ),

                        html.H4("Key Variables", className="fw-semibold mt-3", style={"color": "#09702D"}),
                        html.P("The following fields form the analytical foundation of the dashboard:"),
                        html.Ul(
                            [
                                html.Li("Danceability — Motion-based rhythmic measure (0–1)"),
                                html.Li("Energy — Intensity and dynamism measurement (0–1)"),
                                html.Li("Valence — Positivity and emotional tone (0–1)"),
                                html.Li("Popularity — Track consumption score (0–100)"),
                                html.Li("Tempo — Beats per minute (BPM)"),
                            ],
                            className="ms-3"
                        ),

                        html.H4("Narrative Goals", className="fw-semibold mt-4", style={"color": "#09702D"}),
                        html.P("This dashboard aims to explore questions such as:"),
                        html.Ul(
                            [
                                html.Li("Do energetic tracks tend to be more popular?"),
                                html.Li("Which artists consistently produce highly rhythmic or danceable music?"),
                                html.Li("How do emotional features such as valence correlate with tempo?"),
                                html.Li("Can acoustic profiles help predict track-level popularity?"),
                            ],
                            className="ms-3"
                        ),

                        dbc.Collapse(
                            html.Div(
                                [
                                    html.P(
                                        """
                                        These analytical questions are enabled by the numerical structure of the
                                        dataset. Because each feature is standardized and quantifiable, the dashboard
                                        supports pattern recognition, comparative analysis, and exploratory visual
                                        storytelling across thousands of tracks.
                                        """
                                    ),
                                ],
                                className="mt-2",
                            ),
                            id="collapse-details",
                            is_open=False,
                        ),
                        dbc.Button(
                            "Expand Section",
                            id="toggle-details",
                            color="secondary",
                            className="mt-2",
                            n_clicks=0,
                        ),
                    ]
                ),
                className="mb-5 shadow-sm",
            ),
        ],
        fluid=True,
        className="pb-5",
    )
