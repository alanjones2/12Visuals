
# 12 Essential Visualizations and How to Implement Them, part 2

## We look at how to create the 12 most useful graphs and charts in Python and Streamlit.

![Image by author](https://github.com/alanjones2/12Visuals/raw/main/images/6viz.png)

> ### "When I look back over the 150+ visuals that I created for workshops and consulting projects in the past year, there were only a dozen different types of visuals that I used", _Cole Nussbaumer Knaflic in Storytelling with Data_

TK re-write introduction for part 2

In [Part 1](https://towardsdatascience.com/12-essential-visualizations-and-how-to-implement-them-part-1-41e40400a740) we looked at the first 6 of the 12 visuals that Cole Nussbaumer Knaflic (CNK) identified in her book, _Storytelling with Data_ (see note 1). In this article we will deal with the implementation of the second 6. These are various Bar Charts, the Waterfall Chart and the Square Area Chart.

All of the code and data used in this article are available to freely download from my Github page. The downloadable code may include additional examples not included below.

![](https://github.com/alanjones2/12Visuals/raw/main/images/2nd6.png)
_Variations on the second 6 visuals - image by author_

## Bar charts

CNK suggests that bar charts are often avoided because they are common. But because they are common, they are easily understood by your audience, meaning that they spend less brain power interpreting your graphics and more on reading the data. So, we should embrace bar charts as a visualiztion when appropriate not avoid them.

They are also simple to create as they are included in most visualization libraries.

CNK divides bar charts into 4 categories, vertical, horizontal, stacked vertical amd stacked horizontal, and we will look at them in turn.

But first a word about ...

![](https://github.com/alanjones2/12Visuals/raw/main/images/zerobaselinebad.png)

![](https://github.com/alanjones2/12Visuals/raw/main/images/zerobaselinegood.png)

We are going to use a medals table for the 2022 Winter Olypics as our data for the various bar charts that we will look at. So here is the preliminary code that we will need.

```` Python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

medals =  pd.read_csv('data/2022WinterOlympics.csv')
````

![](https://github.com/alanjones2/12Visuals/raw/main/images/medalstable.png)

_Medals table for the top 4 countries at the 2022 Winter Olympics - data source, [Wikipedia](https://en.wikipedia.org/wiki/2022_Winter_Olympics), image by author_






## 7. Vertical bar



```` Python
fig, ax = plt.subplots()
medals.plot.bar(x='Country', y='Total', ax=ax)
st.pyplot(fig)
````

![](https://github.com/alanjones2/12Visuals/raw/main/images/totalbarvert.png)

```` Python
fig, ax = plt.subplots()
medals.plot.bar(x='Country', ax=ax)
st.pyplot(fig)
````
![](https://github.com/alanjones2/12Visuals/raw/main/images/top5barvert.png)

```Python
fig, ax = plt.subplots()
medals.plot.bar(x='Country', y = ['Gold','Silver','Bronze'],ax=ax)
st.pyplot(fig)
````
![](https://github.com/alanjones2/12Visuals/raw/main/images/7gsbvertbar.png)
## 8. Horizontal bar

```` Python
fig, ax = plt.subplots()
medals.plot.barh(x='Country', ax=ax)
st.pyplot(fig)
````
![](https://github.com/alanjones2/12Visuals/raw/main/images/top5barhoriz.png)

## 9. Stacked vertical bar

```` Python
fig, ax = plt.subplots()
medals.plot.bar(x='Country', 
                y = ['Gold','Silver','Bronze'],
                stacked = True, ax=ax)
st.pyplot(fig)
````

![](https://github.com/alanjones2/12Visuals/raw/main/images/top5barvertstack.png)

## 10. Stacked horizontal bar

```` Python
fig, ax = plt.subplots()
medals.plot.barh(x='Country', 
                 y = ['Gold','Silver','Bronze'], 
                 stacked = True, ax=ax)
st.pyplot(fig)
````

![](https://github.com/alanjones2/12Visuals/raw/main/images/top5barhorizstack.png)

## 11. Waterfall

```` Python
a = ['Beginning HC','Hires','Transfers In','Transfers Out','Exits']
b = [100,30,8,-12,-10]
````

```` Python
my_plot = waterfall_chart.plot(a, b, net_label = "Ending HC")
st.pyplot(my_plot)
````
![](https://github.com/alanjones2/12Visuals/raw/main/images/waterfall1.png)

```` Python
my_plot = waterfall_chart.plot(a, b, net_label = "Ending HC", blue_color='blue',red_color='blue', green_color='blue')
st.pyplot(my_plot)
````
![](https://github.com/alanjones2/12Visuals/raw/main/images/waterfall2.png)

## 12. Square area

total population: 100

cancer sufferers: 6

cancer sufferers who eat bacon in excess: 1

First a vertical bar chart

![](https://github.com/alanjones2/12Visuals/raw/main/images/12cancerbar.png)

```` Python
fig, ax = plt.subplots(figsize=(8,5))

plt.bar(['Cancer-free','Contracted cancer by chance','Contracted cancer and is a Bacon Eater'],[94,6,1])
plt.xticks(rotation = 45)

ax.set_ylabel('Percentage')
ax.set_title('Occurance of Bowel Cancer in a Population')

st.pyplot(fig)
````

Second, a stacked bar that serves as an area chart

![](https://github.com/alanjones2/12Visuals/raw/main/images/12cancerstackarea.png)

```` Python
fig, ax = plt.subplots()
ax.bar('Instances of Cancer', 94,label='Cancer-Free')
ax.bar('Instances of Cancer', 6, label='Contracted cancer by chance')
ax.bar('Instances of Cancer', 1, label='Contracted cancer and is a Bacon Eater')
st.pyplot(fig)
````

Last, a square area chart

![](https://github.com/alanjones2/12Visuals/raw/main/images/12cancersquarearea.png)

```` Python
# construct a 2D array of 0s - total pop
a = [0]*100
b = np.array(a).reshape((10,10))

# add a 2 by 3 rectangle of 1s representing csncer sufferers
for i in range(8,10):
    for j in range(7,10):
        b[i,j] = 1

# add a single cell with value 2
# representing the number of cancer sufferers 
# who eat too much bacon
b[9,9] = 2

# Plot the grid as a heat map in Seaborn
fig, ax = plt.subplots(figsize=(8,5))
sns.heatmap(b, 
            linewidths=0.5, 
            yticklabels=False,
            xticklabels=False, 
            cmap=['lightblue','royalblue','midnightblue'],
            ax=ax)

# Customize legend
colorbar = ax.collections[0].colorbar 
colorbar.set_ticks([0.5,1,1.5])
colorbar.set_ticklabels(['Cancer-free','Contracted cancer by chance','Contracted cancer and is a Bacon Eater'])

ax.set_title('Occurance of Bowel Cancer in a Population')
st.pyplot(fig)
````



### Notes

1. [_Storytelling with Data, a data visualization guide for business professionals_](https://amzn.to/3dJlMaS), Cole Nussbaumer Knaflic, Wiley, 2015 (affiliate link*)

2. The global temperature data is included in the downloadable code and is derived from HadCRUT dataset which tracks the changes in temperature since the late 19th century. You can download versions of it from the UK Meteorological Office, Hadley Centre, [download](https://www.metoffice.gov.uk/hadobs/hadcrut5/data/current/download.html) page without charge under the [Open Government License v3](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) (also see note 3, below).

3. [_Quantifying uncertainties in global and regional temperature change
using an ensemble of observational estimates: the HadCRUT4 data set_](https://www.metoffice.gov.uk/hadobs/hadcrut4/HadCRUT4_accepted.pdf), Colin P. Morice, John J. Kennedy, Nick A. Rayner and Phil D. Jones

4. The weather data is derived from the Met Office text data found [here](
https://www.metoffice.gov.uk/research/climate/maps-and-data/historic-station-data). This data is distributed in accordance with  [Open Government License v3](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) and may be used under the same conditions.



*_If you purchase something via an affiliate link then I may get a commission. It will not affect the price you pay._


