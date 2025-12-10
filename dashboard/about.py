from dash import html
import dash_bootstrap_components as dbc


def create_about():
    # Navbar
    navbar = dbc.NavbarSimple(
        brand="Spotify Dashboard",
        color="dark",
        dark=True,
        children=[
            dbc.DropdownMenu(
                label="About",
                nav=True,
                children=[
                    dbc.DropdownMenuItem("Big Picture", id="about-big-picture"),
                    dbc.DropdownMenuItem("Dataset Details", id="about-dataset-details"),
                ],
            )
        ]
    )

    # About modals
    about_modals = html.Div([
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Big Picture")),
                dbc.ModalBody(
                    "This dataset contains Spotify tracks with features like danceability, energy, popularity, valence, and tempo. "
                    "It allows us to analyze music trends, create visualizations, and explore relationships between features."
                ),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close-big-picture", className="ms-auto", n_clicks=0)
                ),
            ],
            id="modal-big-picture",
            is_open=False,
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Dataset Details")),
                dbc.ModalBody(
                    "Columns include:\n"
                    "- name: Track name\n"
                    "- artist: Track artist\n"
                    "- album: Album name\n"
                    "- danceability: Measure of how danceable the track is (0-1)\n"
                    "- energy: Measure of intensity (0-1)\n"
                    "- popularity: Popularity score (0-100)\n"
                    "- valence: Musical positiveness (0-1)\n"
                    "- tempo: Beats per minute\n\n"
                    "This information lets us tell stories like: 'Which artists have the most energetic tracks?' or 'Which tracks are more danceable?'"
                ),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close-dataset-details", className="ms-auto", n_clicks=0)
                ),
            ],
            id="modal-dataset-details",
            is_open=False,
        )
    ])

    return html.Div([navbar, about_modals])
