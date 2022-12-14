#!/usr/bin/env python
# coding: utf-8

# ## Deliverable 3. Create a Travel Itinerary Map.

# In[2]:


# Dependencies and Setup
import pandas as pd
import requests
import gmaps

# Import API key
from config import g_key

# Configure gmaps
gmaps.configure(api_key=g_key)


# In[ ]:


# 1. Read the WeatherPy_vacation.csv into a DataFrame.
vacation_df = pd.read_csv("Vacation_Search/WeatherPy_vacation.csv")
vacation_df.head()


# In[3]:


# 2. Using the template add the city name, the country code, the weather description and maximum temperature for the city.
info_box_template = """
<dl>
<dt>Hotel Name</dt><dd>{Hotel Name}</dd>
<dt>City</dt><dd>{City}</dd>
<dt>Country</dt><dd>{Country}</dd>
<dt>Current Weather</dt><dd>{Current Description} and {Max Temp} °F</dd>
</dl>
"""

# 3a. Get the data from each row and add it to the formatting template and store the data in a list.
hotel_info = [info_box_template.format(**row) for index, row in clean_hotel_df.iterrows()]

# 3b. Get the latitude and longitude from each row and store in a new DataFrame.
locations = clean_hotel_df[["Lat", "Lng"]]


# In[4]:


# 4a. Add a marker layer for each city to the map.
fig = gmaps.figure(center=(30.0, 31.0), zoom_level=1.5)
marker_layer = gmaps.marker_layer(locations,info_box_content=hotel_info)
fig.add_layer(marker_layer)
# 4b. Display the figure
fig


# In[5]:


# From the map above pick 4 cities and create a vacation itinerary route to travel between the four cities. 
# 5. Create DataFrames for each city by filtering the 'vacation_df' using the loc method. 
# Hint: The starting and ending city should be the same city.

vacation_start = vacation_df.loc[vacation_df['City']=="Kununurra"]
vacation_end = vacation_df.loc[vacation_df['City']=="Kununurra"]
vacation_stop1 = vacation_df.loc[vacation_df['City']=="Karratha"]
vacation_stop2 = vacation_df.loc[vacation_df['City']=="Carnarvon"] 
vacation_stop3 = vacation_df.loc[vacation_df["City"]=='Geraldton'] 


# In[6]:


# 6. Get the latitude-longitude pairs as tuples from each city DataFrame using the to_numpy function and list indexing.
start = vacation_start['Lat'].to_numpy()[0],vacation_start['Lng'].to_numpy()[0]
end = vacation_end['Lat'].to_numpy()[0],vacation_end['Lng'].to_numpy()[0]
stop1 = vacation_stop1['Lat'].to_numpy()[0],vacation_stop1['Lng'].to_numpy()[0]
stop2 = vacation_stop2['Lat'].to_numpy()[0],vacation_stop2['Lng'].to_numpy()[0]
stop3 = vacation_stop3['Lat'].to_numpy()[0],vacation_stop3['Lng'].to_numpy()[0]


# In[7]:


# 7. Create a direction layer map using the start and end latitude-longitude pairs,
# and stop1, stop2, and stop3 as the waypoints. The travel_mode should be "DRIVING", "BICYCLING", or "WALKING".
fig = gmaps.figure()
vacation_itinerary = gmaps.directions_layer(
        start, end, waypoints=[stop1, stop2, stop3], travel_mode='DRIVING')

fig.add_layer(vacation_itinerary)
fig


# In[8]:


# 8. To create a marker layer map between the four cities.
#  Combine the four city DataFrames into one DataFrame using the concat() function.
itinerary_df = pd.concat([],ignore_index=True)
itinerary_df


# In[9]:


# 9 Using the template add city name, the country code, the weather description and maximum temperature for the city. 
info_box_template = """
<dl>
<dt>Hotel Name</dt><dd>{Hotel Name}</dd>
<dt>City</dt><dd>{City}</dd>
<dt>Country</dt><dd>{Country}</dd>
<dt>Current Weather</dt><dd>{Current Description} and {Max Temp} °F</dd>
</dl>
"""

# 10a Get the data from each row and add it to the formatting template and store the data in a list.
hotel_info = [info_box_template.format(**row) for index, row in itinerary_df.iterrows()]

# 10b. Get the latitude and longitude from each row and store in a new DataFrame.
locations = itinerary_df[["Lat", "Lng"]]


# In[3]:


# 11a. Add a marker layer for each city to the map.
figure_layout = {
    'width': '800px',
    'height': '700px'}
fig = gmaps.figure(center=(-20.0, 125.0), zoom_level=5
                ,layout=figure_layout)



marker_layer = gmaps.marker_layer(locations,info_box_content=hotel_info)

fig.add_layer(marker_layer)
# 11b. Display the figure
fig


# In[ ]:




