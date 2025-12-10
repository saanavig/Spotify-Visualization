from dash import Input, Output, State

def register_about_callbacks(app):
    @app.callback(
        Output("collapse-big-picture", "is_open"),
        [Input("toggle-big-picture", "n_clicks")],
        [State("collapse-big-picture", "is_open")],
    )
    def toggle_big_picture(n, is_open):
        if n:
            return not is_open
        return is_open

    @app.callback(
        Output("collapse-details", "is_open"),
        [Input("toggle-details", "n_clicks")],
        [State("collapse-details", "is_open")],
    )
    def toggle_details(n, is_open):
        if n:
            return not is_open
        return is_open
