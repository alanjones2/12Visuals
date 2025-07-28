import plotly.graph_objects as go
import pandas as pd
import streamlit as st

def create_text_chart(
    text: str,
    title: str = "",
    font_size: int = 24,
    font_color: str = "black",
    template: str = 'plotly_white'
):
    """
    Creates a Plotly figure that displays a text string.

    Args:
        text (str): The text string to display.
        title (str, optional): The title of the chart. Defaults to "".
        font_size (int, optional): The font size of the text. Defaults to 24.
        font_color (str, optional): The color of the text. Defaults to "black".
        template (str, optional): The Plotly template to use. Defaults to 'plotly_white'.

    Returns:
        go.Figure: A Plotly figure object.
    """
    fig = go.Figure()

    fig.add_annotation(
        x=0.5,
        y=0.5,
        xref="paper",
        yref="paper",
        text=text,
        showarrow=False,
        font=dict(size=font_size, color=font_color),
        xanchor="center",
        yanchor="middle"
    )

    fig.update_layout(
        title_text=title,
        xaxis=dict(visible=False, showgrid=False, zeroline=False),
        yaxis=dict(visible=False, showgrid=False, zeroline=False),
        template=template,
        height=200,  # Adjust height as needed
        margin=dict(l=20, r=20, t=50, b=20)
    )
    return fig



# --- Example Usage ---
st.header("Text Chart (Generic Function)")

text_to_display = "Hello, Plotly!"
fig_text = create_text_chart(
    text=text_to_display,
    #title="My Custom Text Display",
    font_size=36,
    font_color="darkblue"
)
st.plotly_chart(fig_text)

text_to_display_2 = "This is another example with different styling."
fig_text2 = create_text_chart(
    text=text_to_display_2,
    font_size=18,
    font_color="red"
)

st.plotly_chart(fig_text2)

