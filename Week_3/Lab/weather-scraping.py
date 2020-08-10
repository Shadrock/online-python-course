'''
Assignment title: Lab 3- Web-scraping Current Weather Conditions
Date: 02/06/2020
Description: The script web-scrapes the weather.gov website to extract current weather conditions for a selected location in the U.S.
Inputs: Latitude & Longitude in Decimal Degrees
Outputs: Current Weather Conditions
'''

# Import required libraries
import requests
from bs4 import BeautifulSoup

# Provide the latitude and longitude for the location you would like to check the weather for
# Lat/lon in decimal degrees provided for Worcester, MA
lat = '42.2634'
lon = '-71.8022'

# Create url for the requested location through string concatenation
url = 'https://forecast.weather.gov/MapClick.php?lat='+lat+"&lon="+lon
# Check if the URL exists
# print url

# Send request to retrieve the web-page using the get() function from the requests library
# The page variable stores the response from the web-page
page = requests.get(url)

# Create a BeautifulSoup object with the response from the URL
# Access contents of the web-page using .content
# html_parser is used since our page is in HTML format
soup=BeautifulSoup(page.content,"html.parser")

# Locate element on page to be scraped
# This element is located within an id tag called current_conditions-summary
# find() locates the element in the BeautifulSoup object
cur_weather_conditions = soup.find(id="current_conditions-summary")

# Extract text from the selected BeautifulSoup object using .text
cur_weather_conditions = cur_weather_conditions.text

# Final Output
# Return scraped information
print('The Current Weather Conditions at '+ lat +  ", " + lon + " is:" + cur_weather_conditions)
