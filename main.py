import streamlit as st
import pandas as pd
import numpy as np
st.title('Uber pickups in NYC')

import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
url = "https://kafka.pk/collections/all-tapestry"
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the "span" tags with class "title"
title_spans = soup.find_all("span", class_="title")

# Extract the text inside each "span" tag
for span in title_spans:
    title_text = span.get_text()
    st.text(title_text)
