import plotly.graph_objects as go
import pandas as pd
import streamlit as st
from typing import List, Optional


def create_slope_chart(
    df: pd.DataFrame,
    x_col: str,
    y_cols: List[str],
    title: str = "Slope Chart",
    x_title: Optional[str] = None,
    y_title: Optional[str] = None,
    colors: Optional[List[str]] = None,
    text_format: str = "{:.1f}",
    show_legend: bool = False,
    template: str = 'plotly_white'
):
    """
    Creates a generic slope chart using Plotly.

    Args:
        df (pd.DataFrame): DataFrame containing the data. Must have at least two rows.
        x_col (str): The name of the column to be used for the x-axis (e.g., 'year').
        y_cols (List[str]): A list of column names to be plotted on the y-axis.
        title (str, optional): The title of the chart. Defaults to "Slope Chart".
        x_title (Optional[str], optional): The title for the x-axis. Defaults to x_col name.
        y_title (Optional[str], optional): The title for the y-axis. Defaults to None (hidden).
        colors (Optional[List[str]], optional): A list of colors for the lines.
                                                If None, Plotly's default colors are used.
        text_format (str, optional): A format string for the data point labels. Defaults to "{:.1f}".
        show_legend (bool, optional): Whether to display the legend. Defaults to False.
        template (str, optional): The Plotly template to use. Defaults to 'plotly_white'.

    Returns:
        go.Figure: A Plotly figure object.
    """
    fig = go.Figure()

    if colors is None:
        # Use plotly's default color cycle if no colors are provided
        colors = fig.layout['template']['layout']['colorway']

    color_map = {y_col: colors[i % len(colors)] for i, y_col in enumerate(y_cols)}

    x_values = df[x_col]
    x_start = x_values.iloc[0]
    x_end = x_values.iloc[-1]

    for y_col in y_cols:
        y_values = df[y_col]
        y_start = y_values.iloc[0]
        y_end = y_values.iloc[-1]
        color = color_map[y_col]

        # Add the slope line
        fig.add_trace(go.Scatter(
            x=x_values,
            y=y_values,
            mode='lines+markers',
            name=y_col,
            line=dict(color=color),
            marker=dict(color=color, size=8)
        ))

        # Add annotations
        # Left side: Category name and value
        fig.add_annotation(
            x=x_start, y=y_start,
            text=f"<b>{y_col}</b><br>{text_format.format(y_start)}",
            showarrow=False,
            xanchor='right',
            align='right',
            xshift=-8
        )
        # Right side: Value
        fig.add_annotation(
            x=x_end, y=y_end,
            text=text_format.format(y_end),
            showarrow=False,
            xanchor='left',
            xshift=8
        )

    # Update layout for a clean slope chart appearance
    fig.update_layout(
        title_text=title,
        xaxis_title=x_title if x_title else x_col.capitalize(),
        yaxis_title=y_title,
        showlegend=show_legend,
        template=template,
        yaxis=dict(visible=False),
        xaxis=dict(tickmode='array', tickvals=x_values, showgrid=False, zeroline=False)
    )
    return fig


# --- Original Data Example ---
st.header("Original Slope Chart (Generic Function)")
df_temps = pd.DataFrame({'year': [2012, 2022], 
                         'London': [24.2, 27.2], 
                         'Cardiff': [19.2, 21.2], 
                         'Wick': [14.8, 17.3]})

fig1 = create_slope_chart(
    df=df_temps,
    x_col='year',
    y_cols=['London', 'Wick', 'Cardiff'],
    title="Temperature Change (2012 vs 2022)",
    colors=['red', 'blue', 'green'],
    text_format="{:.1f}°C"
)
st.plotly_chart(fig1)
