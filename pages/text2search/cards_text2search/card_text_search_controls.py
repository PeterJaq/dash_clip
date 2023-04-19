import warnings

import dash_bootstrap_components as dbc
from dash import html, dcc


card_db_search_controls = dbc.Card(
    dbc.CardBody(
        [
            html.Div(
                [
                    html.H4(children="Search Image from Database"),
                    html.Div(
                        [
                            dbc.Row(
                                [
                                    dbc.Col(
                                        html.Label("Search Prompt"),
                                        lg=8,
                                        md=8,
                                        sm=12,
                                    ),
                                    dbc.Col(
                                        html.Label("Model"),
                                        lg=4,
                                        md=4,
                                        sm=12,
                                    )
                                ]   
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        dbc.Input(
                                            id = "text-search-input",
                                            placeholder="Text to search",
                                            type="text",
                                        ),
                                        lg=8,
                                        md=8,
                                        sm=12,
                                    ),
                                    dbc.Col(
                                        dcc.Dropdown(
                                            id = "text-search-model-type",
                                            multi = False,
                                            options = ["CLIP"],
                                            value = ["CLIP"],
                                            placeholder = "Select a use model type"
                                        ),
                                        lg=4,
                                        md=4,
                                        sm=12,
                                    )
                                ]
                            )
                        ]
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Div(
                                    [
                                        dbc.Button("search", id="text-search-button", n_clicks=0, outline=True, color="secondary", className="me-1")
                                    ],
                                    style={"text-align": "center"},
                                    className="p-3",
                                )
                            )
                        ]
                    )
                ]
            )
        ]
    ),
    class_name="mb-3",
)