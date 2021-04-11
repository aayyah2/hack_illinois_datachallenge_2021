#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from sklearn import linear_model

#Preprocessing/Subsetting 

happiness_data = pd.read_csv('world-happiness-report-2021.csv') 
#print(happiness_data.columns)

print(happiness_data.mean())
happiness_data["Generosity"]=(happiness_data["Generosity"]-happiness_data["Generosity"].min())/(happiness_data["Generosity"].max()-happiness_data["Generosity"].min())

happiness_data["Ladder score"]=(happiness_data["Ladder score"]-happiness_data["Ladder score"].min())/(happiness_data["Ladder score"].max()-happiness_data["Ladder score"].min())

happiness_data["Healthy life expectancy"]=(happiness_data["Healthy life expectancy"]-happiness_data["Healthy life expectancy"].min())/(happiness_data["Healthy life expectancy"].max()-happiness_data["Healthy life expectancy"].min())

happiness_data["Social support"]=(happiness_data["Social support"]-happiness_data["Social support"].min())/(happiness_data["Social support"].max()-happiness_data["Social support"].min())

happiness_data["Freedom to make life choices"]=(happiness_data["Freedom to make life choices"]-happiness_data["Freedom to make life choices"].min())/(happiness_data["Freedom to make life choices"].max()-happiness_data["Freedom to make life choices"].min())

happiness_data["Logged GDP per capita"]=(happiness_data["Logged GDP per capita"]-happiness_data["Logged GDP per capita"].min())/(happiness_data["Logged GDP per capita"].max()-happiness_data["Logged GDP per capita"].min())

#factors to look at: Generosity, Healthy Life Expectency, Social Support, Freedom to make life choices, 'Logged GDP per capita'
unique_regions = pd.unique(happiness_data[["Regional indicator"]].values.ravel())

western_europe = happiness_data.loc[happiness_data["Regional indicator"] == 'Western Europe']
middle_east = happiness_data.loc[happiness_data["Regional indicator"] == 'Middle East and North Africa']
latin_america = happiness_data.loc[happiness_data["Regional indicator"] == 'Latin America and Caribbean']
north_america = happiness_data.loc[happiness_data["Regional indicator"] == 'North America and ANZ']
subsaharan_africa = happiness_data.loc[happiness_data["Regional indicator"] == 'Sub-Saharan Africa']
south_asia = happiness_data.loc[happiness_data["Regional indicator"] == 'South Asia']


# In[5]:


print((happiness_data["Regional indicator"]).unique())


# In[6]:


#Part I
categories = ['Ladder Score','Generosity',"Healthy life expectancy","Social support",
              "Freedom to make life choices", "Logged GDP per capita"]

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r = [subsaharan_africa["Ladder score"].mean(), subsaharan_africa["Generosity"].mean(), (subsaharan_africa["Healthy life expectancy"].mean()), (subsaharan_africa["Social support"].mean()), subsaharan_africa["Freedom to make life choices"].mean(), (subsaharan_africa["Logged GDP per capita"].mean())],
      theta=categories,
      fill='toself',
      name='Subsaharan Africa'
))

fig.add_trace(go.Scatterpolar(
      r = [western_europe["Ladder score"].mean(), western_europe["Generosity"].mean(), (western_europe["Healthy life expectancy"].mean()), (western_europe["Social support"].mean()), western_europe["Freedom to make life choices"].mean(), (western_europe["Logged GDP per capita"].mean())/15],
      theta=categories,
      fill='toself',
      name='Western Europe'
))

fig.add_trace(go.Scatterpolar(
      r = [middle_east["Ladder score"].mean(), middle_east["Generosity"].mean(), (middle_east["Healthy life expectancy"].mean()), (middle_east["Social support"].mean()), middle_east["Freedom to make life choices"].mean(), (middle_east["Logged GDP per capita"].mean())],
      theta=categories,
      fill='toself',
      name='Middle East'
))

fig.add_trace(go.Scatterpolar(
      r = [latin_america["Ladder score"].mean(), latin_america["Generosity"].mean(), (latin_america["Healthy life expectancy"].mean()), (latin_america["Social support"].mean()), latin_america["Freedom to make life choices"].mean(), (latin_america["Logged GDP per capita"].mean())],
      theta=categories,
      fill='toself',
      name='Latin America'
))

fig.add_trace(go.Scatterpolar(
      r = [north_america["Ladder score"].mean(), north_america["Generosity"].mean(), (north_america["Healthy life expectancy"].mean()), (north_america["Social support"].mean()), north_america["Freedom to make life choices"].mean(), (north_america["Logged GDP per capita"].mean())],
      theta=categories,
      fill='toself',
      name='North America'
))

fig.add_trace(go.Scatterpolar(
      r = [south_asia["Ladder score"].mean(), south_asia["Generosity"].mean(), (south_asia["Healthy life expectancy"].mean()), (south_asia["Social support"].mean()), south_asia["Freedom to make life choices"].mean(), (south_asia["Logged GDP per capita"].mean())],
      theta=categories,
      fill='toself',
      name='South Asia'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 1]
    )),
  showlegend=True
)

fig.show()


# In[7]:


#Part II
happiness_data = pd.read_csv('world-happiness-report-2021.csv') 

df = happiness_data

#life expect vs generosity, ladder score, gdp, freedom, social support
fig = px.scatter(df, x="Social support", y="Healthy life expectancy", color="Logged GDP per capita",
                 title="Life Expectancy vs Social Support", trendline='ols', trendline_color_override='darkblue')
fig.show()

fig = px.scatter(df, x="Generosity", y="Healthy life expectancy", color="Logged GDP per capita",
                 title="Life Expectancy vs Generosity", trendline='ols', trendline_color_override='darkblue')
fig.show()

fig = px.scatter(df, x="Logged GDP per capita", y="Healthy life expectancy", color="Logged GDP per capita",
                 title="Life Expectancy vs GDP Per Capita", trendline='ols', trendline_color_override='darkblue')
fig.show()


fig = px.scatter(df, x="Freedom to make life choices", y="Healthy life expectancy", color="Logged GDP per capita",
                 title="Life Expectancy vs Freedom to Make Choices", trendline='ols', trendline_color_override='darkblue')
fig.show()


fig = px.scatter(df, x="Ladder score", y="Healthy life expectancy", color="Logged GDP per capita",
                 title="Life Expectancy vs Ladder score", trendline='ols', trendline_color_override='darkblue')
fig.show()


# In[8]:


#Part III
fig = go.Figure(data=go.Scatter(
    y = happiness_data["Generosity"],
    x=happiness_data["Logged GDP per capita"],
    mode='markers',
    marker=dict(
        size=15,
        color=happiness_data["Healthy life expectancy"], #set color equal to a variable
        colorscale='Viridis', # one of plotly colorscales
        showscale=True
    )
))

fig.update_layout(
    title="Generosity vs GDP per capita (colored by life expectancy)",
    xaxis_title="GDP per capita",
    yaxis_title="Generosity",
    showlegend=False
)

fig.show()


# In[9]:


#Part IV
X = happiness_data[["Logged GDP per capita", "Social support", "Freedom to make life choices", "Ladder score"]]
y = happiness_data["Healthy life expectancy"]

regr = linear_model.LinearRegression()
regr.fit(X, y)
print(regr.score(X, y))


# In[ ]:

