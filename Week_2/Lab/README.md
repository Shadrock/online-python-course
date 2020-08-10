# Lab 2 – Data Classification
To complete this lab you will need to add a `.py` script that contains your code (be sure it is well commented!) and edit this README file.

You can write your script using whatever tolls you like, but it must include a comment block at the top with the following information:
- Name:
- Date created:
- Version of Python you are using
- Very brief description of the assignment or the assignment name. Include inputs and outputs.

You should edit your README file to provide the following information:
- Summarize what your script does or the problem you were trying to solve.
- Summarize any major errors you encountered and what sources they used to resolve the errors
- How you fixed the errors, or where the error is if you couldn't figure something out.

Remember that you are encouraged to look for answers online! Stackoverflow, other Github repositories, or Python documentation are all good places to start.

## The Code
You will a function, called “feelTemp”, that converts a given temperature (in Fahrenheit) into four categorical levels, hot, warm, cool, and cold using the following criteria:

- If the temperature is 100 or above, the functions return “It is hot.”;
- If the temperature is between 70 and 100, the function returns “It is warm.”;
- If the temperature is between 32 and 70, the functions return “It is cool.”;
- If the temperature is below 32, it returns “It is cold.”

The function feelTemp will take one value for the temperature, and then returns a category as a string. When running the program, the user is prompted to input a temperature, then the program prints one of the four categorical levels (hot, warm, cool, and cold) that the given temperature falls into.

Use `if/elif/else` structure to classify the input numerical values into one of the four categories; use the input to get input from the keyboard. Be sure to include comments and documentation in your script to tell me what it’s doing!
