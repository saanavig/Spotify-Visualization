import dash
from dash import html
from layout import create_layout
from callbacks import register_callbacks
from about import create_about
from callbacks_about import register_about_callbacks
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, "./dashboard/styles.css"]
)

# Create layout
app.layout = html.Div([
    create_about(),
    create_layout(app)
])

# Register callbacks
register_callbacks(app)
register_about_callbacks(app)

if __name__ == "__main__":
    app.run(debug=True)
