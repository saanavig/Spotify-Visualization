import dash
from dash import html
import pandas as pd
from layout import create_layout
from callbacks import register_callbacks

app = dash.Dash(
    __name__,
    external_stylesheets=["./dashboard/styles.css"]
)

#call the layout
app.layout = create_layout(app)
register_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)
