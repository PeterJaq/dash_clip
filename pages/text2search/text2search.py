import warnings

import dash
from dash import callback
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

import plotly.express as px

from pages.text2search.cards_text2search.card_text_search_controls import card_db_search_controls
# from pages.text2search.cards_text2search.card_image_callback import card_image_callback


warnings.simplefilter(action="ignore", category=FutureWarning)

dash.register_page(
    __name__,
    path="/text2search",
    title="Use text search image.",
    name="Text2Clip",
    description="dash widget to search image by text use multi modle",
)

def layout():
    page = dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(card_db_search_controls)
                ]
            ),
        ],
        class_name="mt-2",
        fluid="md",
    )

    return page