import dash
import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("ImageProcess", href="/")),
        dbc.NavItem(dbc.NavLink("TextSearch", href="/text2search")),
    ],
    brand="clip widgets",
    brand_href="/",
    color="primary",
    dark=True,
)