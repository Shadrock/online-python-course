# Web-scraping in Depth Part 2

This tutorial is designed to continue our deep dive into the practice of web scraping. In the exercise below we'll be scraping elements from multiple web pages.

## Working with Multiple Pages
So far, we've been grabbing elements from a single page in Wikipedia; text from the table of contents, an image, etc. But in general, we'll be wanting to grab multiple elements across multiple pages.

For this exercise, we'll be using a site specifically designed to practice web scraping: http://toscrape.com. This way we don't need to worry about asking for permission or looking through the terms of service. We'll practice on their imitation book store: http://books.toscrape.com/. This is basically set up like a regular online bookstore. For our goal, let's try to get the title of every book with a five-star rating. This would save us time if we were trying to pick out a highly rated book to read.

# Web Scraping Tutorial
The Python code below was created using Google Colab, so some of the code may differ slightly if you are working in a different environment.

## Importing our Libraries
We'll continue to use Beautiful Soup (`bs4`), `requests`, and `lmxl`. Google Colab comes with a wide range of libraries already installed. You can check to see if libraries are installed using the following code:

```Python
# This example checks to see if we have bs4 installed and will return a boolean.
import sys
'bs4' in sys.modules
```
If you need to install the libraries you can use:
```Python
# install libraries
!pip install requests
!pip install lxml
!pip install bs4
```
To get started, import your libraries!
```Python
# start by importing our libraries
import requests
import bs4
```

Now let's see what we're working with. The main page shows that there are 1000 books in the store. And that each page only shows 20 of those... there are 50 pages. So we'll probably need to loop through each of the pages since everything isn't on one page.

We'll start by understanding what happens to the URL as a user clickes from one page to the next. Let's copy/paste the URL from the first to pages to compare them:

The URL from the first page is: `http://books.toscrape.com/catalogue/page-1.html`
The URL from the second page is: `http://books.toscrape.com/catalogue/page-2.html`

Okay, it looks like the `page-` string changes with each new page. And we know there are 50 pages. If we didn't know how many pages there were, we'd need to think about how to use something like a `while` condition for our loop, but since we know how many pages we have we can get to work...

Start by creating a base URL that contains all the static parts of the URL. However, where the page number should be, let's swap out curly braces `{}`. This will allow us to the `.format` method to pass in whatever page numbers we like as strings.

```Python
base_url = "http://books.toscrape.com/catalogue/page-{}.html"
```
Then we'll test this by passing an argument and running one page. I'm using `20`, but you can try it with any page you like.
```Python
base_url.format('20')
```
When you run this, you should get a strong that shows the URL for the page you passed. In my case the output is `http://books.toscrape.com/catalogue/page-20.html`.

From here, there are a few ways we could proceed. One way would be to set up variables for each page number and pass those. The output of the code below should be similar to the above: a string value with the page you passed in the correct place in the URL.
```Python
page_num = 15
base_url.format(page_num)
```
This allows us to go to any particular page we like. So it can be used as part of our loop in order to go through the pages. But how do we scrape through each page to find the 5 star rating?

Let's inspect some star ratings using developer tools. Can you find `class = "icon star"`? What class exists above that? Is there a class for star ratings?

We're also looking for titles. It looks like there's a `class="product_pod"` that holds all the information for a book: price, title, whether it's in stock, and the rating! So if we grab that class, we can parse out all the information we need!

Now that we have a target to scrape, it's time to make a request, make our soup, and select that pod class.
```Python
# Make our request
res = requests.get(base_url.format(1))
```
```Python
# Create our soup
soup = bs4.BeautifulSoup(res.text, 'lxml')
```
```Python
# Check the soup: running this will return quite a bit of code from the html page.
soup
```
```Python
# Now let's select the product pod class: running this will also return quite a bit of code.
soup.select(".product_pod")
```
If you look at the output from the last step, you should a series of code HTML code blocks that all look similar and contain things like `<i class="icon-star"></i>` and other product information. As a quick check to make sure our code is running we can check the length of our soup selection. Since there are 20 books per page, and each one has a product pod class, the output from the following code should be `20`.

```Python
len(soup.select(".product_pod"))
```
Now we need to figure out what code will allow us to grab a title associated with a 5 star rating. Since the output of `(soup.select(".product_pod")` is basically a list of all the different things (star review, title, etc.) lets start by setting it up as a list called `products` then start by grabbing the first item in `products` to start creating our code.
```Python
products = soup.select(".product_pod")
```
We'll use an example to get our code going. If it works with one example - that we'll creatively call `example`, then we can expand our code.
```Python
example = products[0] # using a zero index to grab just the first one.
```
Now we'll run it to see what we're getting.
```Python
example
```
The output should look something like this:
```
<article class="product_pod">
<div class="image_container">
<a href="a-light-in-the-attic_1000/index.html"><img alt="A Light in the Attic" class="thumbnail" src="../media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg"/></a>
</div>
<p class="star-rating Three">
<i class="icon-star"></i>
<i class="icon-star"></i>
<i class="icon-star"></i>
<i class="icon-star"></i>
<i class="icon-star"></i>
</p>
<h3><a href="a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
<div class="product_price">
<p class="price_color">Â£51.77</p>
<p class="instock availability">
<i class="icon-ok"></i>

        In stock

</p>
<form>
<button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
</form>
</div>
</article>
```
There are two things in here that we want to look at:
- the class for the star rating, and
- the title.

Let's begin by trying to answer the question, is this a 5 star rating or not? We can do a quick and dirty check by converting our `example` variable to a string, then checking to see if the rating is in that.

```Python
'star-rating Five' in str(example)
```
Running this code will return a boolean value. For me, this was `False`.

This would be one way of building out code... but this method might not be the best. Instead, let's use the beautiful soup select method. If we manually inspect our output for `example`, we see that it contains a class for a three star rating. We could try and select this, replacing the space between the words `rating` and `Three` with a dot. This is just a a requirement of this method. We should see a class return.

```Python
example.select(".star-rating.Three")
```
Running the above code should result in an list similar to this:
```
[<p class="star-rating Three">
 <i class="icon-star"></i>
 <i class="icon-star"></i>
 <i class="icon-star"></i>
 <i class="icon-star"></i>
 <i class="icon-star"></i>
 </p>]
 ```
So it looks like we do have a three star rating! Taking this test further, we can check to see if there is a 5 star rating in our example. We know there isn't one, so we would expect to get an empty list.

```Python
example.select(".star-rating.Five")
```

So another way to check for 5 star ratings would be to use this method by checking if an empty list is the equivalent to the star rating. This will return a boolean.
```Python
[] == example.select(".star-rating.Five")
```

Now that we know how to check our rating. Let's figure out how to grab a title. Inspecting our example, we see a `title` tag which is held within a `<a href>` tag. Let's run the following code:
```Python
example.select('a')
```
The output should look something like:
```
[<a href="a-light-in-the-attic_1000/index.html"><img alt="A Light in the Attic" class="thumbnail" src="../media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg"/></a>,
 <a href="a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a>]
```
Looks like this returns two `a` tags. Looking at the first one, it looks like it contains an `img` while the second one contains the `title` we're looking for. So for each product, we want to the second `a` tag, which would be index space 1. Since we're using the `select` method in beautiful soup, we can also ask for the tag to get the associated value.

```Python
example.select('a')[1]['title']
```
The output is `A Light in the Attic`. That's great, our code is working! Not only that, but this is a fantastic book, which you should definitely check out if you haven't already.

So let's block in what we want our code to do by combining our ideas.
- We want to check if something is 5 star by doing a string call in, `example.select(rating))`.
- Then we can also grab the book title using `example.select('a')[1]['title']`.

Ok. I think we're ready to build our scraper.

```Python
# start by initiating an empty list that will hold our output.
five_star_titles = []

# Now iterate to get info from each page.
# We want to include page 50, so index should go up to, but not include 51,
for n in range (1,51):
  scrape_url = base_url.format(n)
  res = requests.get(scrape_url)
  soup = bs4.BeautifulSoup(res.text,'lxml')
  books = soup.select(".product_pod")
  # within our loop, we'll create another loop to parse the books and select star rating five.
  for book in books:
    if len(book.select('.star-rating.Five')) != 0: # if the list is not empty, then we do have a 5 star book. Could also use if 'star-rating Five' in str(book)
      book_title = book.select('a')[1]['title']
      five_star_titles.append(book_title)
```
Alright... here comes the moment of truth. Let's check our output.

```Python
# Running this should give us our list
five_star_titles
```
Congrats: you've looped through a whole web site to scrape all the five-star titles!

# What to Submit

In this tutorial we've written - step by step - instructions to create a script that will scrape the text we want across multiple pages of a website. Now I want you to alter the code a bit. We know what all the highest rated books are on this website, but what about the lowest rated ones? Let's say that most users don't scroll through all 50 pages of a site but, generally, only see the first few. We want a list of all of the books that only have one star rating, in the first 5 pages of the website. Adjust the script to give you this output.

When you are done, submit your notebook - the code should be in a single block or code cell so it can be run all at once - in a Github repository from your _personal account_. The`README` file in your repository should briefly explain what your code does and specify any inputs and outputs required. Feel free to add other explanation as necessary, such as any problems you encountered and how you debugged them, any interesting insights you gained from the tutorial, etc.
