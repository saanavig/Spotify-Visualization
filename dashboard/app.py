import dash
from dash import html, dcc, Output, Input
import dash_bootstrap_components as dbc

from pages import get_page_layout
from callbacks import register_callbacks
from callbacks_about import register_about_callbacks

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, "./dashboard/styles.css"],
    suppress_callback_exceptions=True
)

# navbar
navbar = dbc.NavbarSimple(
    brand="Spotify Insights",
    color="dark",
    dark=True,
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/")),
        dbc.NavItem(dbc.NavLink("Dashboard", href="/dashboard")),
    ],
    className="mb-4"
)

# main app layout
app.layout = html.Div([
    dcc.Location(id="url"),
    navbar,
    html.Div(id="page-content")
])

# url routing
@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def display_page(pathname):
    return get_page_layout(pathname, app)

# register callbacks
register_callbacks(app)
register_about_callbacks(app)

if __name__ == "__main__":
    app.run(debug=True)
