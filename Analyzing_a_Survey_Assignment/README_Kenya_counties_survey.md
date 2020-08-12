# **Part 1: Analyzing a Survey**
**How this assignment works:** read through this document and follow along. You will download data, then write a series of programs to process the code in different ways. I _strongly_ encourage you to type, not copy, the example code. This will help you understand what it is doing better. At two different points, there is a "challenge" that requires you to take the code you have built up through the examples and modify it.

You will submit a new Colab notebook that contains code that fulfills the challenges. Your code should be well commented and you should use text blocks and Markdown to introduce your solutions and talk a little bit about your code: was there anything that was particularly challenging about writing it, did you run into any problems, how did you solve them, did you find other examples online that were helpful, what were they?
___
**Context:** You work in a very large humanitarian organizations with a large number of programs spread throughout [Kenya's counties](https://en.wikipedia.org/wiki/Counties_of_Kenya#:~:text=As%20of%202013%20general%20elections,legally%20recognised%20Districts%20of%20Kenya.). Due to the a significant drop in funding from donors who have decided that funding humanitarian work is no longer a priority, the head of your organization has decided to start closing down programs and shift resources to the counties where:
1. Ongoing programs are deemed critical and
2. there remain significant resources in terms of local funding, volunteer support, etc.

In an effort to be completely transparent, the head of your organization has asked each staff member working on programs to consider these paramaters and vote for the *one* county in which operations should continue. Each person gets one vote.

As the GIS analyst for this organiztaion, you're tasked with developing some different ways to explore and communicate the results.

This doesn't sound like a very complicated job, but you go to a few planning meetings anyways and are *assured* that the survey is being structred well and that it will be very easy for you to manipulate. Everyone seems very confident that they understand "data structure", "file format", and "transcription errors" (if you don't know the [last one](https://en.wikipedia.org/wiki/Transcription_error), you should look it up).

Of course, none of this happens as planned and when you do receive the final survey it is in the form of a `.txt` file that is formatted as a name, a hyphen, and a prefered county to work in. Example: `Shadrock Roberts - Nairobi County`.

When asked how the survey was collected, the response is, "somebody wrote it up in Word. Jeez, can't you work with that? I thought you were supposed to be "technical."" Oh well. Looks like you're going to need some Python.

**Note**: this is based on not just one, but hundreds of true stories where something just like this happened.

## Upload the Survey
Access the data for the survey in the [data folder accompanying this Github repo](https://github.com/Shadrock/online-python-course/tree/master/Analyzing_a_Survey_Assignment/Data). It may be important to right-click on the link for the file and select "save as." Previously, I've tried opening the data, copying it on screen, then pasting it into a new file... which kept throwing [Unicode errors](http://python-notes.curiousefficiency.org/en/latest/python3/text_file_processing.html#unicode-error-handlers).

To start, create a new Colab notebook (or Python script, if you prefer) and import the data. In Colab the code looks like this:

```python
from google.colab import files
uploaded = files.upload()
```
Running this code block will generate a button that you can use to select a file from your computer. For more examples of ways to upload surveys to Colab see [this blogpost](https://towardsdatascience.com/3-ways-to-load-csv-files-into-colab-7c14fcbdcb92). If you are working locally, it's important to make sure that you are working in the right directory. For more information on opening and reading files locally see [this web page from Stanford University](http://www.compciv.org/guides/python/fileio/open-and-read-text-files/#how-to-fix-a-filenotfounderror). [Google's documentation for Colab](https://colab.research.google.com/notebooks/io.ipynb) also has a lot of good information about working with files, including how to use Google drive or Google sheets.

## Reading the Survey
This next section of code opens the file, processes the file, and outputs the different parts of the string into a sentence for each line in the `.txt` file. This code uses the [`split()` method](https://docs.python.org/3.3/library/stdtypes.html#str.split) to split each line in the file on the hyphen. Before running the whole code block, experiment with the split method.

For example, what do you think will happen if you run `"1,2,3,4,5".split(",")` Or what about `"Jin Li - Nairobi County".split("-")` Try it and see!

After you've experimented, you can use `split()` to help process your code.
```python
with open("KEcounty_votes.txt") as file:
  for line in file:
    line = line.strip()                 # strips the newline from the end
    parts = line.split(" - ")           # Splits the string on the hyphen and outputs a list. E.g. ['field1', 'field2']
    name = parts[0]                     # These two lines store each field in a named variable. Since name and vote were the files in the file. The 0 and 1 values are the indexes!
    vote = parts[1]
    print(name + " voted for " + vote)  # This concatenates the strings to form a sentence.
```

In the code above, note that we've created a variable called `parts` to store the output of the split. After this line runs, parts has the value `['Jin Li', 'Nairobi County']`. In other words, the output is a list called `parts` that contains two elements. We store the name in a variable called `name` that pulls the first element (at the `0`) index. Then we store the second element (at the `1` index) using the variable name `vote`.

# **Inspecting Votes**
Let's write code that prints only the names of people who voted for Nairobi County. You may find `if vote  == "Nairobi County"` helpful.

Here's one possible solution:
```Python
with open("KEcounty_votes.txt") as file:
  for line in file:
    line = line.strip()                 # strips the newline from the end
    parts = line.split(" - ")           # Splits the string on the hyphen and outputs a list. E.g. ['field1', 'field2']
    name, vote = parts                  #  “multiple assignment” assigns each variable to the corresponding item in the list.
    if vote  == "Nairobi County":
      print(name + " prefers Nairobi County!")  # This concatenates the strings to form a sentence.
```

## Using Multiple Assignment in your code.
In the example given above to introduce split, we assigned each element of parts separately (e.g. `name = parts[0]`) but you can also assign them together using a technique called “multiple assignment”. In our solution, the line `name, vote = parts` means to assign each variable to the corresponding item in the list. Also, note that we use the "equal", or `==` to only print the results containing `Nairobi County`.

Multiple assignment only works when the number of elements being assigned on the left hand side of the “ = “ matches the number on the right. Try running the following code:
```python
a, b, c = [1, 2, 3]
print(b)
print(a)
```
or
```python
Nairobi, Boston, London = "NBO,BOS,LON".split(",")
print(Boston)
```
What happens when you run the following?
```python
Nairobi, Boston, London = "NBO,BOS,LON,LAX".split(",")
print(Boston)
```
# **Counting Votes**
Now, let's write a program that counts the total number of votes for Nairobi County. Use your previous code as a base. You’ll need a variable to hold the number of votes recorded for Nairobi County, which you increment (i.e add one to) as part of the loop.

Here's one possible solution:
```python
print("Counting votes for Nairobi County...")
count = 0
with open("KEcounty_votes.txt") as file:
  for line in file:
    line = line.strip()
    name, vote = line.split(" - ")
    if vote == "Nairobi County":
      count = count + 1
print(count)
```

# **Challenge 1: Write a general function**
Rewrite the code above as a function where you specify an argument with the name of the county you want to count votes for, and the function returns the number of votes for that particular county. Your code should be well commented to explain what the different parts of the code are doing.

# **Counting All the Votes**
Counting votes for each county is a bit time consuming, you have to know all the names in advance and you have to loop through the file multiple times. How about if you could automatically find all the counties that were voted for, and count them all in one pass?

You’ll need a data structure where you can associate a county name with the number of votes counted for it. A dictionary would be perfect!

Imagine a program that can count votes to create a dictionary with contents like this:

`
{
    'Nairobi County': 65,
    'Uasin Gishu': 63,
    'Turkana': 76,
    'Mombasa County': 58,
    'Nyeri': 63,
    'Kisumu': 72,
    'Marsabit': 72,
    'West Pokot': 57,
    'Elgeyo Marakwet': 56,
    'Taita Taveta': 56,
    'Homa Bay': 72
}
`

Meaning the key ‘Nairobi County’ is associated with the value of 65 votes, the key ‘Uasin Gishu’ is associated with the value of 63 votes, ‘Turkana’ has 76 votes, etc, etc.

Can you create such a program? Start with one of your previous vote-counting programs and try to modify it to count all varieties.

Here are two snippets of code you might find useful: create an empty dictionary for associating county names with vote counts using `counts = {}`, then find a place in your code for the following:
```python
if vote not in counts:
    # First vote for this variety
    counts[vote] = 1
else:
    # Increment the vote count
    counts[vote] = counts[vote] + 1
```
Remember that for dictionaries `counts[vote]` means "the value in `counts` which is associated with the key `vote`”. In this case, the key is a string (camp name) and the value is a number (vote count.)

If you need some help, here's one possible solution:
```python
# Create an empty dictionary for associating county names with vote counts
counts = {}

# Open and process file
with open("KEcounty_votes.txt") as file:
  for line in file:
    line = line.strip()
    name, vote = line.split(" - ")
    if vote not in counts:
      # First vote for this county
      counts[vote] = 1
    else:
      # Increment the vote count
      counts[vote] = counts[vote] + 1
print(counts)
```

### Formatting More Readable Output
When you run this program the output is pretty hard for a person to read, even though it’s all there. What we want is to print the data in a way which is easy for people to read.

Instead of `print(counts)` we could try:
```python
for name in counts:
  count = counts[name]
  print(name + ": " + str(count))
```
So, how does the output look? It might look a little odd. First, let's understand what the code is doing.

The code above prints each vote on its own line. Iterating through a dictionary (ie `for name in counts`) means iterating through the _keys_ (county names), so we still need to look up each _value_ (the vote count) with `count = counts[name]`

Why do we use `str(count)` here? Try removing the `str()` call and see what Python tells you! `str()` returns the string equivalent of the number, ie `str(12)` returns `"12"`.

Python needs to distinguish between strings and numbers for lots of reasons. For example, using numbers `12+1` is 13. Using strings, `"12" + "1"` concatenates the strings to give you `"121"`.

# **Data "Munging"**
Inspect the output and you'll notice some funny things. There appear to be a lot of duplicates! This is a result of unclean data. To a computer, `"Nairobi County"` and `"nairobi county"` look different because of the different capitalization. So do `"Taita Taveta"` and `" Taita Taveta"` because of the leading space. We need to clean up our data, which is sometimes referred to as "data munging."

We already know one munging function, `strip()`. Try applying `strip()` to each voting choice, to remove distinctions like `" Taita Taveta"` and `"Taita Taveta"`.

How about `"Nairobi County"` and `"nairobi county"`? Take a look at the [Python string functions reference](https://docs.python.org/3/library/stdtypes.html#string-methods) and see if you can find a function that could transform these two so they look the same to the computer.

There are lots of functions which could remove the case distinction. `str.lower()` would convert all the names to all lower case, `str.upper()` would CONVERT THEM ALL TO UPPER CASE, or `str.capitalize()` would **C**apitalize the first letter only. Here’s one possible solution:

```python
# Create an empty dictionary for associating county names with vote counts
counts = {}

with open("KEcounty_votes.txt") as file:
  for line in file:
    line = line.strip()
    name, vote = line.split(" - ")
    # munge the vote string to clean it up
    vote = vote.strip().capitalize()
    if not vote in counts:
      # First vote for this variety
      counts[vote] = 1
    else:
      # Increment the vote count
      counts[vote] = counts[vote] + 1
print(counts)
```

Check the comment on the "munging" line we've added. This basically says, “take the variable called `vote`, and call the `strip()` function on it, and then call the `capitalize()` function on the result, and then assign that result back to the variable `vote`.

Now, there are still some funny votes counted in the output of this program! They all have something in common, a double space “ “ between the first and second words. BLAHRG! Stupid typos! The `strip()` only cleaned up additional whitespace at the start and end of the string. We can use the `replace` function can be used to replace all double spaces with a single space. Try plugging the following code into your program so those last few votes get counted correctly: `vote = vote.replace("  ", " ")` The first set of quotes has *two* spaces, while the second only has one!

# **Vote Checking**
So far we’ve counted votes without paying attention to the name of the person who voted. Can you modify your program so it also prints out a warning if anyone voted twice?

You will need to start making a list of the names of everyone who has voted so far. Each time you see a new name, check if it is already in the list of names. Starting with an empty list of names, you can use `voterlist.append(newentry)` to append a new entry to the end.

You’ll need to apply the same data munging techniques to clean up people’s names, so that “Joanne Smith” and “joanne smith” are counted as the same person.

Below is one possible solution.

```python
# Create an empty dictionary for associating radish names with vote counts
counts = {}

# Create an empty list with the names of everyone who voted
voted = []

with open("KEcounty_votes.txt") as file:
  for line in file:
    line = line.strip()
    name, vote = line.split(" - ")
    # clean up the person’s name
    name = name.strip().capitalize().replace(" "," ")
    # check if this person already voted
    if name in voted:
      print(name + " has already voted! Fraud!")
      continue
    voted.append(name)
    # munge the vote string to clean it up
    vote = vote.strip().capitalize().replace("  "," ")
    if not vote in counts:
      # First vote for this variety
      counts[vote] = 1
    else:
      # Increment the vote count
      counts[vote] += 1

print("Results:")
print()
for name in counts:
  print(name + ": " + str(counts[name]))
```

There are two new concepts in the code above:

`continue` means "stop whatever you were doing and go to the next iteration of the loop". In this case, if the person has already voted then we don’t want to count their invalid vote - instead we `continue` and start the next iteration, with the next vote on the next line of the file.

`counts[vote] += 1` is a shorthand for `counts[vote] = counts[vote] + 1`.

# **Challenge 2: Write a complete script using functions**

At this point, you're code has gone through a _lot_ of iterations and you have all the raw material you need to split your code into functions to make it easier to read. Write a complete script to process the `KEcounty_votes.txt` file with separate functions to:
* clean up (munge) a string to make it easy to
match against (because we do the exact same thing to clean up names as we do to clean up the vote choice.),
* check if someone has voted before, and
* count a vote.

The script should print the number of votes cast for each county. And, as usual, it should be well commented to explain what the different sections of code do.

Bonus points if you update the script so it goes through the votes counted and finds the one with the most votes. If you decide to do this you may want to add this as a totally separate cell, after the previous cells, rather than modifying your existing loops.
