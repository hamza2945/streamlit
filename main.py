# import streamlit as st
# import requests
# from bs4 import BeautifulSoup
# st.title('Website Title Scraper')
# # Send a GET request to the URL
# url = "https://kafka.pk/collections/all-tapestry"
# response = requests.get(url)
# # Parse the HTML content using Beautiful Soup
# soup = BeautifulSoup(response.content, "html.parser")
# # Find all the "span" tags with class "title"
# title_spans = soup.find_all("span", class_="title")
# reviews=soup.find_all("span",class_="jdgm-prev-badge__text")
# i=0
# # Extract the text inside each "span" tag
# for span in title_spans:
#     title_text = span.get_text()
    
#     st.text(title_text)
#     st.text(reviews[i].get_text())
#     i=i+1

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the AQI data from a CSV file
df = pd.read_csv('aqi_data.csv')

# Convert year values to integers
df['Year'] = df['Year'].astype(int)

# Sidebar slider for selecting the range of years
year_range = st.slider('Select Year Range', int(df['Year'].min()), int(df['Year'].max()), value=(int(df['Year'].min()), int(df['Year'].max())))

# Filter the data based on the selected year range
filtered_data = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]

# Group the data by city and calculate the average AQI
avg_aqi_by_city = filtered_data.groupby('City')['AQI'].mean().reset_index()
# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(avg_aqi_by_city['City'], avg_aqi_by_city['AQI'])
plt.xlabel('City')
plt.ylabel('Average AQI')
plt.title('Average AQI by City using dummy data')
plt.xticks(rotation=45)
plt.tight_layout()
# Display the bar chart using Streamlit
st.pyplot(plt)

