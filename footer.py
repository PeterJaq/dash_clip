import dash
from dash import html, dcc


def footer():
    return html.Footer(
        html.Div(
            [
                html.Hr(),
                dcc.Markdown(
                    """
                **Dash-CLIP** for edy3 project. *MIT License*  
                """
                ),
                # html.P(
                #     [
                #         html.Img(src=dash.get_asset_url("GitHub-Mark-32px.png")),
                #         html.Span("   "),
                #         html.A("GitHub Repository", href="https://github.com/mbk-dev/okama-dash", target="_blank"),
                #     ]
                # ),
            ],
            style={"text-align": "center"},
            className="p-3",
        ),
    )