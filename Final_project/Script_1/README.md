# Final Project: Web-scraping Weather Forecast with Python (Script 1)

In this lab, you will work with a script that scrapes the 5-day weather forecast from the National Weather Service website. The script extracts information from multiple elements listed under the same class name using the BeautifulSoup library.

- Copy the `NWS_WeatherForecast.py` file and paste the code it contains into your code editor or Colab.

- Read the description and comments in the script to understand the purpose of the script

- Run the script. You may see some packages being installed when you run it for the first time.

- The script returns the 5-day forecast for Worcester, MA (Lat: 42.2634, Lon: -71.8022) with the latitude and longitude information provided. Using the latitude and longitude values, it generates the following URL through string concatenation: https://forecast.weather.gov/MapClick.php?lat=42.2634&lon=-71.8022

- Open this URL in a Firefox or Chrome browser. Locate the information that is being outputted in our script. Right click on this and select the Inspect Element option. This will launch the Inspector window that helps locate different elements on the page.

- Notice that all forecast containers in this section are located in the _`forecast-tombstone`_ class inside the _`li`_ tag. In order to scrape multiple elements listed under the same class name, we utilize the `findAll()` function from BeautifulSoup. The tag and class names are required arguments for this function.

### Editing the Script1
Edit the `NWS_WeatherForecast.py` script to add the following functionality:
1. Take latitude and longitude values as inputs in decimal degrees from a user.

2.	Convert the latitude and longitude values to strings to generate the URL for the selected location. Pass this URL as an argument in the `get()` request.

3.	The returned forecast information in the existing script did not preserve its spacing during the scraping process. Using the `replace()` function, fix any spacing issues with the output

4.	Convert the final output to uppercase.

Remember to update the `NWS_WeatherForecast.py` file to include comments and documentation in your script to tell me what it’s doing!
