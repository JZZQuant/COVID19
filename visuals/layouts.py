import plotly.graph_objects as go
import base64


def get_bar_layout(city):
    layout = dict(
        title=dict(
            text='SEIR Model for {0}'.format(city),
            font=dict(family="Open Sans, sans-serif", size=15, color="#515151"),
        ),
        paper_bgcolor="rgb(247, 247, 245)",
        plot_bgcolor="rgb(247, 247, 245)",
        updatemenus=list([
            dict(active=1,
                 buttons=list([
                     dict(label='Log Scale',
                          method='update',
                          args=[{'visible': [True, True]},
                                {'title': 'Log scale',
                                 'yaxis': {'type': 'log'}}]),
                     dict(label='Linear Scale',
                          method='update',
                          args=[{'visible': [True, True]},
                                {'title': 'Linear scale',
                                 'yaxis': {'type': 'linear'}}])
                 ]),
                 )
        ]),
        legend=dict(
            x=-0.265,
            y=-0.1,
            traceorder="reverse",
            font=dict(
                family="sans-serif",
                size=12,
                color="black"
            ),
            bgcolor="rgb(247, 247, 245)",
            bordercolor="rgb(247, 247, 245)",
            borderwidth=2
        ),
        # barmode='stack',
        width=900,
        height=400,
        font=dict(family="Open Sans, sans-serif", size=13),
        hovermode="all",
        xaxis=dict(title="Days",rangemode="nonnegative"), yaxis=dict(title="Records"),rangemode="nonnegative",autorange = False,rangeslider=dict(visible = True))
    return layout
