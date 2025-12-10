from dash import html
from about import create_about
from layout import create_layout   # your visualizations layout

def get_page_layout(page, app):
    if page == "/":
        return create_about()  # Home page

    elif page == "/dashboard":
        return create_layout(app)  # Visualizations Dashboard

    else:
        return html.H1("404 - Page Not Found", className="text-center mt-5")
