import streamlit as st

st.set_page_config(layout='wide')

# make any grid with a function

def make_grid(cols,rows):
    grid = [0 for i in range(cols)]
    for i in range(cols):
        with st.container():
            grid[i] = st.columns(rows)
    return grid
        

mygrid = make_grid(2,6)

mygrid[0][0].subheader('Simple Text:')
mygrid[0][1].image('images/plttext.png',use_column_width=True)
mygrid[0][2].subheader('Table:')
mygrid[0][3].image('images/dataframe.png', width = 300)
mygrid[0][4].subheader('Heatmap:')
mygrid[0][5].image('images/heatmapsns.png')
mygrid[1][0].subheader('Scatter plot:')
mygrid[1][1].image('images/scatter.png')
mygrid[1][2].subheader('Line plot:')
mygrid[1][3].image('images/lineplotshaded.png')
mygrid[1][4].subheader('Slopegraph:')
mygrid[1][5].image('images/slope.png')

mygrid2 = make_grid(2,3)
mygrid2[0][0].image('images/plttext.png',use_column_width=True)
mygrid2[0][1].image('images/dataframe.png', width = 500)
mygrid2[0][2].image('images/heatmapsns.png')
mygrid2[1][0].image('images/scatter.png')
mygrid2[1][1].image('images/lineplotshaded.png')
mygrid2[1][2].image('images/slope.png')

mygrid3 = make_grid(3,3)
mygrid3[0][0].image('images/norwaybarvert.png',use_column_width=True)
mygrid3[0][1].image('images/top5barvert.png', width = 500)
mygrid3[0][2].image('images/top5barhoriz.png')
mygrid3[1][0].image('images/top5barvert.png')
mygrid3[1][1].image('images/top5barvertstack.png')
mygrid3[1][2].image('images/top5barhorizstack.png')
mygrid3[2][0].image('images/waterfall1.png')
mygrid3[2][1].image('images/waterfall2.png')
mygrid3[2][2].image('images/squarearea.png')