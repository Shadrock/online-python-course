# **Creating Charts in Python**
**How this assignment works:** read through this document and follow along. This builds on our previous exercise processing Kenya Counties data. I _strongly_ encourage you to type, not copy, the example code. This will help you understand what it is doing better. There is one "challenge" that requires you to take the code you have built up through the examples and modify it.

You will submit a new Colab notebook that contains code that fulfills the challenge. Your code should be well commented and you should use text blocks and Markdown to introduce your solutions and talk a little bit about your code: was there anything that was particularly challenging about writing it, did you run into any problems, how did you solve them, did you find other examples online that were helpful, what were they?
___
**Context:** In our previous work, we did some processing on our survey of counties in Kenya, but we can take things further and explore some more features using a Jupyter notbook. We’re going to use a Python library called [Matplotlib](https://matplotlib.org/) to create some graphical charts based on our data.

Open a new notebook and try the code below; you’ll see that the output is a line chart plotted in the notebook, under the code cell.

```python
import matplotlib.pyplot as plt
vals = [3,2,5,0,1]
plt.plot(vals)
```
Matplotlib can also output charts in other formats like image files, but being able to edit the code and regenerate the chart inline is one of the nice features of Jupyter notebooks.

If you want to use Matplotlib directly in Python instead of via a Notebook, you just need to add one final line to each of your programs: `plt.show()` will display a window with the chart you created, and pause the script until you close it. All the examples here assume you’re using matplotlib with a Colab Notebook, so remember this additional line if you're not.

## Load Your Data
The `.txt` file that contains our survey is in the [data folder accompanying this Github repo](https://github.com/Shadrock/online-python-course/tree/master/Analyzing_a_Survey_Assignment/Data). We can load it using the same code we did previously. In Colab the code looks like this:

```python
from google.colab import files
uploaded = files.upload()
```
# **The Challenge: make 2 graphics**
We'll use matplotlib to generate a bar chart to display the vote counts from the Kenya Counties program we wrote. The example below will walk you through matplotlib using _my_ solution to the challenges in our previous work: your solution may or may not resemble mine. Once you've gone through the example below, you'll need to figure out how to create a bar chart that works with _your_ code. **Additionally**, you'll need to create one more type of chart. Your final submission will be a new Colab Notebook that contains code to generate the two charts. It doesn't matter if you have one piece of code to generate both charts, or separate code to generate each chart.

## Bar Charts in Python
For this example, we'll run my code here to generate some of the variables I created including `counts`, which holds a dictionary mapping each county name to the vote count. We'll use that to plot the vote counts. Remember, this may or may not be similar to your code: the goal here is to work through an example and get an idea of how you can write your code. Run this code I created to "munge" the data and create different functions to process the votes.

```python
# Create an empty dictionary for associating county names with vote counts
counts = {}

# Create an empty list with the names of everyone who voted
voted = []

# Clean up (munge) a string so it's easy to match against other strings
def clean_string(s):
  return s.strip().capitalize().replace("  "," ")

# Check if someone has voted already and return True or False
def has_already_voted(name):
  if name in voted:
    print(name + " has already voted! Fraud!")
    return True
  return False

# Count a vote for the county variety named 'county'
def count_vote(county):
  if not county in counts:
    # First vote for this county
    counts[county] = 1
  else:
    # Increment the county count
    counts[county] = counts[county] + 1

with open("KEcounty_votes.txt") as file:
  for line in file:
    line = line.strip()
    name, vote = line.split(" - ")
    name = clean_string(name)
    vote = clean_string(vote)

    if not has_already_voted(name):
      count_vote(vote)
    voted.append(name)

print("Results:")
print()
for name in counts:
    print(name + ": " + str(counts[name]))
```

## On with the graphing...
Start by importing two modules - [pyplot](https://matplotlib.org/tutorials/introductory/pyplot.html) is one way to plot graph data with Matplotlib. It’s modelled on the way charting works in another popular commercial program, MATLab. [NumPy](https://numpy.org/) is a module providing lots of numeric functions for Python.
```python
# Imports matplotlib and numpy and assigns them variable names
import matplotlib.pyplot as plt
import numpy as np
```
The code below is a loop that processes the dictionary into a format that’s easy to send to matplotlib - a list of county names (for the labels on the bars) and a list of vote counts (for the actual graph.)
```python
names = []
votes = []
# Split the dictionary of names->votes into two lists, one holding names and the other holding vote counts
for county in counts:
    names.append(county)
    votes.append(counts[county])
```
Now we'll create a range of indexes for the X values in the graph, one entry for each entry in the “counts” dictionary (ie `len(counts)`), numbered 0,1,2,3,etc. This will spread out the graph bars evenly across the X axis on the plot.

`np.arange` is a NumPy function like the `range()` function in Python, only the result it produces is a “NumPy array”. We’ll see why this is useful in a second.

```python
# The X axis can just be numbered 0,1,2,3...
x = np.arange(len(counts))
```
`plt.bar()` creates a bar graph, using the "x" values as the X axis positions and the values in the votes array (ie the vote counts) as the height of each bar.

`plt.xticks()` specifies a range of values to use as labels ("ticks") for the X axis.

Finally, `rotation=90` ensures that the labels are drawn sideways (90 degree angle) not straight. You can experiment with different rotations to create different effects.
```python
plt.bar(x, votes)
plt.xticks(x + 0, names, rotation=90)
```

After running this code you should see something that looks like this:
--- IMAGE HERE ---

## A Few Things to Consider
In this example, there’s no label on the Y axis showing that it represents the vote count. Can you update your bar graph code so it does this? Take a look at the [ylabel() function in the pyplot documentation](https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.ylabel).

For your second chart, you can view the [matplotlib gallery](https://matplotlib.org/3.1.1/gallery/index.html) for ideas. Two good places to start would be the [Horizontal Bar Chart](https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/barh.html#sphx-glr-gallery-lines-bars-and-markers-barh-py) or the [Bar Charts with Gradients](https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/gradient_bar.html#sphx-glr-gallery-lines-bars-and-markers-gradient-bar-py), either of which would be a great second chart. Feel free to try others, but these should both be fairly straight forward.

Happy coding!
