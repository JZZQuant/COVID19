from core.seir import network_epidemic_calc
import dash_core_components as dcc
import dash_html_components as html
from core.scrap import node_config_list

map_column = html.Div(id="selectors",children=[
    html.H3("Covid-19 India SEIR Model"),
    html.Div([
        dcc.Dropdown(
            id='map',
            style={"width":500},
            options= [{'label':node["node"],'value':node["node"]} for node in node_config_list],
            value=node_config_list[0]["node"])]),

    html.Div(children=[dcc.Upload(
        id="upload-data",
        children=html.Div(
            ["Upload Config and refresh after 30s"]
        ),
        style={
            "width": "100",
            "height": "20",
            'marginTop': 10, 'marginBottom': 10,
            "borderStyle": "dashed",
            "textAlign": "center",
        },
        multiple=False,
    )]),
    html.Div(children=[
        html.A("Global Dict", href="/download_global/"),
        html.A("Nodal Dict", href="/download_nodal/",style={'margin':10})
    ])
])

graph_column = html.Div(id="plots",children=[
    dcc.Graph(id="seir", figure=network_epidemic_calc("India")),
    dcc.Graph(id="seir2", figure=network_epidemic_calc("India"))
])
