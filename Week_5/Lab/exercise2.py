#The multi-line string was scraped from the National Weather Service Website.
#Edit this exercise to produce the output below using string manipulation techniques:

#Tonight: Clear, Low: 55 F
#Thursday: Sunny then Chance Showers, High: 77 F
#Friday: Sunny, High: 73 F
#Saturday: Mostly Sunny, High: 77 F
#Sunday: Mostly Sunny, High: 71 F

#Note: Copy the below code in the edit mode to retain the multi-line string formatting. There should be 39 lines of code when pasted in Python IDLE.

# -*- coding: utf-8 -*-
# Keep the line above when running script
# Tells python what encoding the string is stored in

# Scraped multi-line String
forecast = '''

Tonight
ClearLow: 55 F

Thursday
Sunny thenChanceShowersHigh: 77 F

Friday
SunnyHigh: 73 F

Saturday
Mostly SunnyHigh: 77 F

Sunday
Mostly SunnyHigh: 71 F
'''

# Split string into a list
# Use two blank lines (\n\n) as the separator
# Creates a list item at every instance of separator
forecast_list = forecast.split('\n\n')

# Loop through list to make string replacements to each item
# Remove extra whitespaces or lines for a cleaner format
for day in forecast_list:
    day = day.replace('\n',': ')
    # add your code here
    print(day)
