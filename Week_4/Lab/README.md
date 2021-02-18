# Lab 4 – String Manipulation
To complete this lab you will need to edit the scripts provided (be sure it is well commented!) and this README file.

You can write your script using whatever tools you like, but it must include a comment block at the top with the following information:
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
This week there are three short scripts: one to capitalize portions of a string, one to parse and manipulate a multiline string, and one to extract a portion of a string and return in a way that is more understandable. This week there are three starter scripts included with this repo: edit them as needed to do the following:

**Part 1**
Edit `exercise1.py` to write a function that capitalizes the first and fourth letters of a name. In this example, the function is called “old_macdonald” and takes a string for an argument.

For example, running the function as `old_macdonald('macdonald')` would produce `MacDonald` as its output.

Add your code to exercise1.py

Note: there is a method called "capitalize." The syntax for it is `'macdonald'.capitalize()` and, in this example, it returns 'Macdonald'

**Part 2**
`exercise2.py` scrapes the National Weather Service website to produce a multiline string (seen below) using string manipulation techniques.

> Tonight: Clear, Low: 55 F
>
> Thursday: Sunny then Chance Showers, High: 77 F
> 
> Friday: Sunny, High: 73 F
> 
> Saturday: Mostly Sunny, High: 77 F
> 
> Sunday: Mostly Sunny, High: 71 F

**Part 3**
Write code to extract the latitude and longitude from the URL in `exercise3.py`. Output should be text that reads:
Latitude: 42.2509428
Longitude: -71.8249939

Remember to update the existing header in the Python files. Be sure to include comments and documentation in your script to tell me what it’s doing!
