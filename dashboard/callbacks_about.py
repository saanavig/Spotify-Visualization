from dash import Input, Output, State
import dash_bootstrap_components as dbc

def register_about_callbacks(app):
    @app.callback(
        Output("modal-big-picture", "is_open"),
        [Input("about-big-picture", "n_clicks"), Input("close-big-picture", "n_clicks")],
        [State("modal-big-picture", "is_open")],
    )
    def toggle_big_picture(n1, n2, is_open):
        if n1 or n2:
            return not is_open
        return is_open

    @app.callback(
        Output("modal-dataset-details", "is_open"),
        [Input("about-dataset-details", "n_clicks"), Input("close-dataset-details", "n_clicks")],
        [State("modal-dataset-details", "is_open")],
    )
    def toggle_dataset_details(n1, n2, is_open):
        if n1 or n2:
            return not is_open
        return is_open
