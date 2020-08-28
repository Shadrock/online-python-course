# Lab 1 – Calculations with Python
To complete this lab you will need to add a script that contains your code (be sure it is well commented!) and edit this README file. You can save your Colab directly as an `.ipynb` file or, if you're using a different code editor, save it as a `.py` file.

You can write your script using whatever tolls you like, but it must include a comment block at the top with the following information:
- Name:
- Date created:
- Version of Python you are using
- Very brief description of the assignment or the assignment name. Include inputs and outputs.

You should edit your README file to provide the following information:
- Summarize what your script does or the problem you were trying to solve.
- Summarize any major errors you encountered and what sources they used to resolve the errors
- How you fixed the errors, or where the error is if you couldn't figure something out.

Remember that you are encouraged to look for answers online! Stackoverflow, other Github repositories, or Python documentation are all good places to start. If you need a reminder about *why* we create README files and how to structure them well, [see this online guide](https://www.makeareadme.com/). Github's documentation on README files [can be found here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/about-readmes).

## The Code
You will write code to calculate agricultural land and rain runoff in Kenya.
Tip - Concepts here come from Chapter 2: Variables, expressions, and statements

When agricultural land is paved over, rainwater cannot be absorbed as easily, resulting in the runoff of rainwater. In some cases, this runoff can lead to increases in flooding or landslides. The runoff also presents an opportunity to capture and/or recycle it. We’re going to write a short script to calculate the amount of rain run off of a single plot of land (50 feet by 20 feet) in Kenya during a very small rainstorm. You may be as astonished as we were to learn how much it is. Take a guess: what is the volume of water that runs off a 1,000 square foot plot of paved land during a 1-inch rainstorm? 20 gallons? 50 gallons? 100 gallons? 1000 gallons?

To calculate the runoff from any given rainfall:

Start by writing your script to include variables and values for the length, width, and area of the plot of land. You may want to put a comment tag to show what this section of the script is for. Take the dimensions of the footprint of the land and convert them to inches, because the rainwater is measured in inches and we will need to convert to gallons. Then create descriptive variables with these values and use them to calculate the area. Note: you only need to calculate to the second decimal place or hundredths. Next create include variables and values for the amount of rainfall, which equals: length times width times the number of inches of rainfall to get the cubic inches of water. Once you’ve done that, you’ll need to convert the number of cubic inches to gallons.

Finally, make sure that the script will print out the following text, along with the values you used. It should look something like this:

> plot_length is: (insert whatever values you used)
>
> plot_width is:  (insert whatever values you used)
>
> rainfall_inches is:  (insert whatever values you used)
>
> runoff_gallons is:  (insert whatever values you used)

