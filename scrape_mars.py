{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 2 - MongoDB and Flask Application\n",
    "\n",
    "\n",
    "Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.\n",
    "\n",
    "Start by converting your Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.\n",
    "\n",
    "Next, create a route called /scrape that will import your scrape_mars.py script and call your scrape function.\n",
    "\n",
    "Store the return value in Mongo as a Python dictionary. Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.\n",
    "\n",
    "Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
