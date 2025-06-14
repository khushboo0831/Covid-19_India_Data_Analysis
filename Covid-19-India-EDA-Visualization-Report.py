#!/usr/bin/env python
# coding: utf-8

# In[48]:


# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


# # <center> Latest Covid-19 India Statewise Data </center>

# **About Dataset**
# 
# This dataset contains latest Covid-19 India state-wise data. This dataset can be used to analyze covid condition in India.
# This dataset is great for Exploratory Data Analysis
# 
# 
# **Attribute Information**
# * State/UTs - Names of Indian States and Union Territories.
# * Total Cases - Total number of confirmed cases
# * Active - Total number of active cases
# * Discharged - Total number of discharged cases
# * Deaths - Total number of deaths
# * Active Ratio (%) - Ratio of number of active cases to total cases
# * Discharge Ratio (%) - Ratio of number of discharged cases to total cases
# * Death Ratio (%) - Ratio of number of deaths to total cases

# ### Importing Required Libraries for this Notebook.

# In[8]:


import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# * It is always considered as a good practice to make a copy of original dataset.

# In[9]:


main_df = pd.read_csv("LatestCovid-19.csv")
df = main_df.copy()
df


# * Above dataframe shows the list of all indian state with covid information.

# ### EDA

# In[49]:


# Shape of the dataset
df.shape


# In[50]:


# Getting list of all columns present in the dataframe
df.columns


# In[51]:


# Checking for the duplicated value

df.duplicated().sum()


# In[52]:


# Replacing long name by short name

df = df.replace('Dadra and Nagar Haveli and Daman and Diu', 'Daman and Diu')
df.head(8)


# In[53]:


# Information about dataset

df.info()


# In[54]:


# Statistical measurement of the dataset

df.describe()


# In[55]:


# Checking for any missing value
df.isnull().sum()


# In[ ]:





# In[57]:


df.corr(numeric_only=True)


# In[19]:


import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap of COVID-19 Data")
plt.show()


# ## Visualization

# #### Creating Report using Visualization

# In[20]:


# Barplot using seaborn

plt.figure(figsize=(8, 10))
sns.barplot(data = df, y="State/UTs", x="Total Cases")


# * In above plot we can see that Maharastra have maximum number of covid cases.

# In[21]:


px.bar(df, x="State/UTs", y="Total Cases", color="Death Ratio (%)", title="Total Cases as per each State : ")


# * Even after having the highest number of covid cases in maharastra its death ratio is 2.1% while other state like punjab have high death ratio i.e 2.72%
# * Similarly we can compare other states with one another to make a report on Death Ratio.

# In[22]:


px.scatter(df, x='Active Ratio (%)',y='Death Ratio (%)', color=df['State/UTs'])


# * Here we can see that have the highest Active Ratio i.e 24.95%.
# * we can again see that Punjab have highest Death Ratio of 2.72%, while its active ratio is 0.13%.
# * In similar way we can prepare a detailed report on the Active and Death Ratio.

# In[58]:


fig = px.choropleth(
    df,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='State/UTs',
    color='Total Cases',
    color_continuous_scale='Reds'
)

fig.update_geos(fitbounds="locations", visible=False)

fig.show()


# * Here according to color bar scale the state which have higher number of cases will be dark red in color.
# * Even though graph is missing few state, but even after that its giving good information via visualization.

# In[24]:


fig = px.choropleth(
    df,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='State/UTs',
    color='Deaths',
    color_continuous_scale='Blues'
)

fig.update_geos(fitbounds="locations", visible=False)

fig.show()


# * Higher the number of death in each state more darker will the state in color.

# In[25]:


sns.pairplot(df)


# In[26]:


px.density_heatmap(df, y="Total Cases", x="State/UTs", nbinsx=20, nbinsy=20)


# In[27]:


px.density_heatmap(df, y="Total Cases", x="State/UTs", marginal_x="histogram", marginal_y="histogram")


# In[28]:


sns.relplot(x = 'Total Cases', y ='Discharged', hue = 'State/UTs', data = df)


# In[29]:


import seaborn as sns
import matplotlib.pyplot as plt

sns.pairplot(df, vars=["Total Cases", "Active", "Discharged", "Deaths"], hue="State/UTs", diag_kind='kde')
plt.suptitle("Scatter Matrix of COVID Variables", y=1.02)
plt.show()


# * Above graph shows us the relationship between different variables of all states of India.

# In[30]:


fig = px.scatter(df, x="Total Cases", y="Active", size="Deaths", color=df['State/UTs'], log_x=True, size_max=50)
fig.show()


# * Above graph shows us that Maharastra have highest number of death.
# * While Daman and Diu have lowest number of death.

# In[31]:


px.scatter(df, x="Total Cases", y="Active",size="Active Ratio (%)", color="Active Ratio (%)",hover_name="State/UTs", log_x=True, size_max=60)


# * Above graph shows us that Mizoram have highest number of Active Ratio.

# In[32]:


fig = px.pie(df, values='Total Cases', names=df['State/UTs'], title='Covid cases (%) in all states of India')
fig.show()


# * Above graph shows us that **more than 50%** of covid cases in india are coming only from 4 to 5 states.

# In[33]:


df.nunique()


# In[34]:


fig = px.pie(df, values='Discharge Ratio (%)', names=df['State/UTs'], title='Covid cases (%) in all states of India')
fig.show()


# * Discharge ratio of each state is different as we can also see it from data.

# In[35]:


fig = px.pie(df, values='Death Ratio (%)', names=df['State/UTs'], title='Covid cases (%) in all states of India')
fig.show()


# In[36]:


fig = px.scatter (df, x = "Active", y = "Deaths", template = "plotly_dark",  trendline="ols")
fig.show ()


# ### Report

# #### Creating Report using Mathematical Calculations

# In[37]:


# State having highest number of covid cases in India.

highest_cases = df[df['Total Cases'] == max(df['Total Cases'])]
highest_cases


# In[38]:


# State having Lowest number of covid cases in India.

lowest_cases = df[df['Total Cases'] == min(df['Total Cases'])]
lowest_cases


# In[39]:


# State having highest number of Active cases in India.

highest_active = df[df['Active'] == max(df['Active'])]
highest_active


# In[40]:


# State having Lowest number of Active cases in India.

lowest_active = df[df['Active'] == min(df['Active'])]
lowest_active


# In[41]:


# State having highest number of death ratio in India.

highest_death_ratio = df[df['Death Ratio (%)'] == max(df['Death Ratio (%)'])]
highest_death_ratio


# In[42]:


# State having lowest number of death ratio in India.

lowest_death_ratio = df[df['Death Ratio (%)'] == min(df['Death Ratio (%)'])]
lowest_death_ratio


# In[43]:


# State having highest discharge ratio in India.

highest_discharge_ratio = df[df['Discharge Ratio (%)'] == max(df['Discharge Ratio (%)'])]
highest_discharge_ratio


# In[44]:


# State having lowest discharge ratio in India.

lowest_discharge_ratio = df[df['Discharge Ratio (%)'] == min(df['Discharge Ratio (%)'])]
lowest_discharge_ratio


# In[45]:


# Visualization of top 5 state having highest Death ratio in India.
df1 = df.sort_values(by='Death Ratio (%)', ascending=False).head()
states = df1['State/UTs']
ratio = df1['Death Ratio (%)']
plt.barh(states, ratio)
plt.xlabel('Death Ratio (%)')
plt.ylabel('State')
plt.title('State with  more death ratio in India')
plt.show()


# In[46]:


# DataFrame of top 5 state having highest Death ratio in India.
df1


# #### Conclusion :- By using EDA, Visualization and Reporting we draw different conclusion from the dataset at each step.
