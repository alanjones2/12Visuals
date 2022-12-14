# 12 Essential Visualizations and how to implement them

## We look at how to create the 12 most useful graphs and charts in Python and Streamlit.

![Image by author](https://github.com/alanjones2/12Visuals/raw/main/images/6viz.png)

> ### "When I look back over the 150+ visuals that I created for workshops and consulting projects in the past year, there were only a dozen different types of visuals that I used", _Cole Nussbaumer Knaflic in Storytelling with Data_

I'm sure that many people will have heard of the book, _Storytelling with Data_ by Cole Nussbaumer Knaflic (see note 1), who, according to the book's foreword, has "worked at and with some of the most data-driven organizations on the planet", has taught data visualization at Google over several years and now has created her own teaching company.

The book is dedicated to describing how to effectively communicate using charts and graphs and provides a wealth of information about many aspects of communicating with graphics. But one of the first things you learn in the book is that the author relies on only 12 different types of visualization. The book describes these visuals and their use but does not go into implementation.

The aim of this article is to describe the 12 visuals and show how they can be implemented in Python. All of the code and data used in this article are available to freely download from my Github page. The downloadable code may include additional examples not included below.

TK add code and description of the 12 visuals and a __grid of the 12 visuals thumbnails and labels__
![Image by author](https://github.com/alanjones2/12Visuals/raw/main/images/6vizwithtext.png)

## 1. Simple text

Sometimes, as Cole Nussbaumer Knaflic (CNK, from now on) tells us, a graphic isn't necessary, or even the best option to communicate data. When only a couple values are to be presented, simple text is fine and may even be better than a graph. Let's take an example.

The weather in London, UK, seems to getting hotter in the Summer. The maximum temperature in July 2022 was 27.2 degrees Celcius, which is quite hot for the UK. In 2012 it was 24.2 degrees.

Let's set up some variables that represent the situation in Londo that we can use in a number of different formats.

```` Python
# Set up variables
years = ['2012','2022']
temps = [24.2,27.2]
caption = f"The maximum temperature in July 2022 was {temps[1]}°C"
caption2 =  f"That's {temps[1]-temps[0]}° up from 2012"
````

Now, look at the bar graph, below - it shows a temperature change from one year to another. And while it's clear that the temperature went up a few degrees, you can't quite see exactly how much or precisely what those temperatures are.

![Image by author](https://github.com/alanjones2/12Visuals/raw/main/images/1-bar.png)
*Image by author*

So, let's see how some text only visuals can give us a better idea of what is going on.

Streamlit gives us an attractive method of displaying two values and the change between them - ``st.metric()``. This gives us a more attractive and effective way of showing the same data and is coded very simply, like this:

````Python
col3.metric("Temperature", temps[1],temps[0])
````

If we then combine this with some explanatory text and use a column layout we can achieve a visual that tells us exactly what is going on without the need for any sort of chart.

````Python
col3, col4 = st.columns([1,4])
col3.metric("Temperature", temps[1],temps[0])
col4.markdown(f"#### {caption}")
col4.markdown(caption2)
````

![Image by author](https://github.com/alanjones2/12Visuals/raw/main/images/metric.png)
*Image by author*

Using markdown you can achieve something quite similar, like this:

````Python
col1, col2 = st.columns([1,4])
col1.markdown(f"# {temps[1]}")
col2.markdown(f"#### {caption}")
col2.markdown(caption2)
````


![](https://github.com/alanjones2/12Visuals/raw/main/images/metricmd.png)

These two methods are specific to Streamlit. An alternative, more generic, Python method is positioning text in a matplotlib chart. The code below does just this.

You can see that it is a Mathplotlib chart but with no figure plotted in it - we simply position text in the right places and turn of the axes, ticks etc. with the statement ``ax3.axis('off')``.

```` Python
fig2, ax2 = plt.subplots(figsize=(5,1))

ax2.text(0, 0.9, temps[1],
        verticalalignment='top', horizontalalignment='left',
        color='red', fontsize=18, fontweight = 'bold')
ax2.text(0.2, 0.9, caption,
        verticalalignment='top', horizontalalignment='left',
        color='Black', fontsize=10)
ax2.text(0.2, 0.55, caption2,
        verticalalignment='top', horizontalalignment='left',
        color='darkgrey', fontsize=6)

ax2.axis('off')

st.pyplot(fig2)
````
This gives us the figure, below.

![](https://github.com/alanjones2/12Visuals/raw/main/images/plttext.png)

This is a bit bolder and eye-catching than the other two methods but, of course, we could make a subtler small figure if we wished by changing the font size, colour and positioning of the text.

## 2. Table

A table can be a suitable visual for showing data to a varied audience each of whom are interested in a particular row or column.

Streamlit gives us two methods for displaying tables, ``st.table()`` and ``st.dataframe()``.

Using the same data as above, here is the code for displaying the data as  a table. 

```` Python
import streamlit as st
import pandas as pd

temps = pd.DataFrame()
temps['Year'] = ('2012', '2022')
temps['Temperature'] = (24.2,27.2)

st.subheader("st.table")
st.table(temps)
`````
Which looks like:

![](https://github.com/alanjones2/12Visuals/raw/main/images/table.png)

If the table is too wide for your liking then it is a simple matter to enclose it a column and adjust that column to the width that you want.

And a dataframe is very similar:

```` Python
st.subheader("st.dataframe")
st.dataframe(temps)
````
![](https://github.com/alanjones2/12Visuals/raw/main/images/dataframe.png)

The advantage of using a dataframe is that the cells are selectable and the clicking on a column header will order the dataframe by that column.

Again, these are Streamlit specific methods. You can display a table with Mathplotlib but this is designed to be an addition to a chart but I'm not sure that it provides a suitable solution for standalone Python programs.

However, if you are not using Streamlit then, as a data scientist, the chances you are using Jupyter Notebooks and they provide a very neat rendering of a dataframe - you simply write the name of the dataframe in a Jupyter cell, for example:

```` Python
import pandas as pd

temps = pd.DataFrame()
temps['Year'] = ('2012', '2022')
temps['Temperature'] = (24.2,27.2)

temps
````
and it is rendered like this:

![](https://github.com/alanjones2/12Visuals/raw/main/images/jupytertable.png)

## 3. Heatmap

A heatmap is a figure that uses colour rather than numbers to highlight value differences in a table.

We are going to look at a very suitable use for a heatmap - one where we want to show increases in heat! Well, temperature, really.

The figure below shows the relative global temperatures over the last 150 years or so and is taken from my article [Topical Plots: Global Warming Heatmaps
](https://towardsdatascience.com/topical-plots-global-warming-6b5fb80a0371). (The data I use here is included in the downloadable code and is freely usable - see note 2).

A heatmap is great for demonstrating the trend of global warming over the last decades. You can easily see the colours getting lighter, meaning rising temperatures, as the decades progress. (The figures are not absolute temperatures, of course, but relative to a period between 1961 and 1990.)

![](https://github.com/alanjones2/12Visuals/raw/main/images/heatmapsns.png)

One of the easiest ways of creating a heatmap is with the Seaborn library. You can see from the code below that Seaborn simply take a Pandas dataframe as a parameter and displays the appropiate map as a matplotlib chart.

```` Python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

url='data/bydecade.csv'
gwdec = pd.read_csv(url)
gwdec=gwdec.set_index('Year')
st.table(gwdec)

import seaborn as sns
fig, ax = plt.subplots()
sns.heatmap(gwdec)
st.pyplot(fig)
````

You can achieve a similar chart using the ``imshow()`` function in matplotlib (see the downloadable code for an example).

## 4. Scatterplot

Scatterplots are used to show the relationship between two variables. The example below uses a data file that records weather data for each month in London in 2018 (see note 4) it plots the level of rainfall in millimetres, against the number of hours of sunshine. 

Of course, when it is raining the sun is not normally shining, so you would expect to see fewer hours of sunshine when it rains more. The scatter diagram clearly shows this relationship.

![](https://github.com/alanjones2/12Visuals/raw/main/images/scatter.png)

The code below uses the Matplotlib scatter plot to create the chart.


```` Python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

weather =  pd.read_csv('data/london2018.csv')

fig, ax = plt.subplots()
weather.plot.scatter(x='Rain', y='Sun', ax=ax)
st.pyplot(fig)
````

## 5. Line

Line graphs are used for continuous data and, often, for time series data, too.

Using the same weather data as above, we are going to look at three different line graphs. 

First, we'll plot the mean temperature over the year, then we'll see how we can place multiple plots in the same figure by plotting mean, maximum and minimum temperatures. Finally, in the third chart we will see how we can show a range of values by plotting the mean temperature with shading around it to indicate the range of maximum and minimum around that mean - you can use the same technique to show confidence levels.

First we read in the data. It contains various monthly readings for temperature, hours of sunshine and rainfall.

```` Python
weather =  pd.read_csv('data/london2018.csv')
weather['Tmean'] = (weather['Tmax'] + weather['Tmin'])/2
````

It looks like this:
![](https://github.com/alanjones2/12Visuals/raw/main/images/weatherdf.png)

It didn't have the _mean_ column originally - we created it on the second line of code, above.

Now, the simple line plot.

```` Python
fig, ax = plt.subplots()
ax = weather.plot.line(x='Month', y = 'Tmean', ax=ax)
st.pyplot(fig)
````
A very straightforward line plot of the mean temperature using Matplotlib.

![](https://github.com/alanjones2/12Visuals/raw/main/images/lineplotmean.png)

And creating mulitple plots in the same figure is just a matter of creating new axes for those plots.

```` Python
ax = weather.plot.line(x='Month', y = 'Tmax', color = 'lightgrey', ax=ax)
ax = weather.plot.line(x='Month', y = 'Tmin',  color = 'lightgrey', ax=ax)

st.pyplot(fig)
````

The code above adds two more axes for the minimum and maximum temperatures - which I've coloured differently to the _mean_ plot - and then replots the figure.

![](https://github.com/alanjones2/12Visuals/raw/main/images/lineplotmeanminmax.png)

You can see that this gives us a range that could be more visually appealing if it were shaded.

We do this using the Matplotlib function ``fill_between()`` as follows:

```` Python
plt.fill_between(weather['Month'], 
                 weather['Tmax'],
                 weather['Tmin'], color='lightgrey', alpha=0.5)

ax.get_legend().set_visible(False)
ax.set_ylabel('Temperature Range °C')
````

The fill colour is set to ``lightgrey`` so it blends in the the upper and lower plots. I've also hidded the legend and given the y axis a label to show what we are attempting to represent.

![](https://github.com/alanjones2/12Visuals/raw/main/images/lineplotshaded.png)

As you can see this would be a very suitable representation of a confidence levels. You could, for example, create the upper and lower plots using a fixed percentage of the original one. So, for example, the upper plot line could take the value of the centre value plus 5%, and the lower one the centre value minus 5%.

## 6. Slopegraph

A Slopegraph is simply a line graph that conforms a particular style but that only compares two sets of values.

According to CNK, "slopegraphs can be useful when you have two time periods or points of comparison and want to quickly show relative increases
and decreases".

Unfortunately, the slopegraph is not often found in standard visualization libraries, so you could simply use a line graph instead and it should convey the same meaning.

I'll carry on with our weather theme, I'm going to create a couple of graphs that display the change in temperature that we saw in the text figure, above, but this time we compare London to Wick, in Scotland:

![](https://github.com/alanjones2/12Visuals/raw/main/images/slopetable.png)

This data represents the maximum temperature is two cities in two seperate years. In the following code we draw two plots in the same figure. The first is a simple line graph of the data, then we superimpose a scatter chart with only four points to give us the archetypal blobs at the end of the slopegraph lines.

```` Python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.header("Slope graph")

st.subheader("Here is the data")
df = pd.DataFrame()
df['year']=[2012,2022]
df['London']=(24.2,27.2)
df['Wick']=(14.8,17.3)

st.table(df)

st.subheader("A Slopegraph as a line graph")
fig, ax = plt.subplots()

ax = df.plot(x='year', color = ('red', 'blue'), ax=ax)
ax = df.plot.scatter(x='year',y='London', color= 'red', ax=ax)
df.plot.scatter(x='year',y='Wick', color = 'blue', ax=ax)

plt.xlim(2010,2024)
plt.xticks(df['year'])
ax.set_ylabel('')
st.pyplot(fig)
````
It looks reasonably ok but is not the typical form of a slopechart, certainly not the way they are represented in the CNK's book.

![](https://github.com/alanjones2/12Visuals/raw/main/images/slopeline.png)


To make a more conventional slopegraph we need to do a bit of manipulation on the matplotlib graph.

Here's the type of rendering that CNK has in her book:

![](https://github.com/alanjones2/12Visuals/raw/main/images/slope.png)

It's quite different in that the y values, and the legend text, are written at the ends of the lines and the conventional axes are removed.

Running this code will display the graph above.

```` Python
ax.text(df.year[0] -5, df.London[0], df.columns[1])
ax.text(df.year[0] -2.5,df.London[0], f'{df.London[0]}°C')
ax.text(df.year[1] +1, df.London[1],f'{df.London[1]}°C')
ax.text(df.year[0] -5, df.Wick[0], df.columns[2])
ax.text(df.year[0] -2.5, df.Wick[0],f'{df.Wick[0]}°C')
ax.text(df.year[1] +1, df.Wick[1],f'{df.Wick[1]}°C')

ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.xaxis.grid(visible=True, color = 'black')
ax.get_yaxis().set_visible(False)

ax.get_legend().set_visible(False)

st.pyplot(fig)
````
The first six lines add the text and values to the endo of the lines, then we remove the splines (the frame of the chart) and finally we add an x-axis grid (which only consists of two lines) and hide the legend.

Is that too much effort for a not much different result? I'll let you decide.

## Vertical bar

## Horizontal bar

## Stacked vertical bar

## Stacked horizontal bar

## 11. Waterfall


## Square area































### Notes

1. [_Storytelling with Data, a data visualization guide for business professionals_](https://amzn.to/3dJlMaS), Cole Nussbaumer Knaflic, Wiley, 2015 (affiliate link*)

2. The global temperature data is included in the downloadable code and is derived from HadCRUT dataset which tracks the changes in temperature since the late 19th century. You can download versions of it from the UK Meteorological Office, Hadley Centre, [download](https://www.metoffice.gov.uk/hadobs/hadcrut5/data/current/download.html) page without charge under the [Open Government License v3](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) (also see note 3, below).

3. [_Quantifying uncertainties in global and regional temperature change
using an ensemble of observational estimates: the HadCRUT4 data set_](https://www.metoffice.gov.uk/hadobs/hadcrut4/HadCRUT4_accepted.pdf), Colin P. Morice, John J. Kennedy, Nick A. Rayner and Phil D. Jones

4. The weather data is derived from the Met Office text data found [here](
https://www.metoffice.gov.uk/research/climate/maps-and-data/historic-station-data). This data is distributed in accordance with  [Open Government License v3](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) and may be used under the same conditions.



*_If you purchase something via an affiliate link then I may get a commission. It will not affect the price you pay._


