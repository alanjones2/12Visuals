import plotly.graph_objects as go
import pandas as pd
import streamlit as st

def metric(title, value, delta=None, suffix="", prefix="", delta_suffix="", delta_prefix="",
           number_font_size=36, delta_font_size=24, title_font_size=36, 
           number_font_color="Blue", title_font_color="Black", 
           paper_color="white", align="center", 
           margin=dict(l=5, r=5, t=30, b=0), width=300, height=200):
    """
    A function to mimic Streamlit's st.metric using Plotly.
    
    Parameters:
        title (str): Label or title of the metric.
        value (float | str): Main metric value.
        delta (float | str): Optional delta/change value.
        suffix (str): Optional suffix for the main value.
        prefix (str): Optional prefix for the main value.
        delta_suffix (str): Optional suffix for the delta.
        delta_prefix (str): Optional prefix for the delta.
        number_font_size (int): Optional font size for the main value.
        delta_font_size (int): Optional font size for the delta.
        title_font_size (int): Optional font size for the title.
        number_font_color (str): Optional color for the main value.
        title_font_color (str): Optional color for the title.
        paper_color (str): Optional background color for the chart.
        width (int): Optional width of the chart 
        - to set the width in Streamlit use , 'use_container_width=False' when plotting
        height (int): Optional height of the chart.
        
    Returns:
        go.Figure: A Plotly figure representing the metric.
    """
    fig = go.Figure(go.Indicator(
        mode = "number+delta" if delta is not None else "number",
        value = float(value) if isinstance(value, (int, float)) else 0,
        align=align,
        number = {
            "valueformat": ",",
            "suffix": suffix,
            "prefix": prefix,
            "font": {"size": number_font_size, "color": number_font_color}
        },
        delta = {
            "reference": 0,
            "valueformat": ".2f",
            "relative": False,
            "suffix": delta_suffix,
            "prefix": delta_prefix,
            "font": {"size": delta_font_size}
        } if delta is not None else None,
        title = {"text": title, "font_size": title_font_size, "font_color": title_font_color, "align":align},
        domain = {"x": [0, 1], "y": [0, 1]}
    ))

    if delta is not None:
        fig['data'][0]['delta']['reference'] = float(value) - float(delta)
    
    fig.update_layout(
        margin=margin,
        height=height,
        width=width,
        paper_bgcolor = paper_color    )

    return fig


fig = metric("Revenue change", 10500, delta=500, prefix="$", delta_prefix="USD ")


st.plotly_chart(fig, use_container_width=False)

fig = metric("Revenue change", 10500, delta=500, prefix="$", delta_prefix="USD ", 
             number_font_size=56, width=260,
             align="right", paper_color="#F4F4F4", height=160, margin={'l':10, 'r':10, 't':50, 'b':0 })


st.plotly_chart(fig, use_container_width=False)