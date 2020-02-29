# Web scraping/crawling is the act of removing all html tags from a website leaving us with the information we need. Below is how to scrap the list of latest questions in stackoverflow with Python

# in terminal run pipenv install beautifulsoup4
#  also run pipenv install requests
# change the virtual env to PyCrawler or edit the extension if runningas a sub file print("hello") to preview
# import requests
# use the get method on requests, input the url as parameter eg "https://stackoverflow.com/questions" asign it to a response var
# import BeautifulSoup from bs4
# create an instance of BeautifulSoup object parse in 2 params response.text & "html.parser" save it in a var called soup
# Go to the first question on the site, click inspect to see the class of element of the data you want to scrap
# use the select method on soup which is a css selector input ".<name of the class>" eg ".question-summary" store it in questions var (you can print(question.select_one(".question-hyperlink"*the class name of the element to scrap*).getText()); to see the attributes)
# Then iterate the list of questions before the above print statement and run
# Lastly you can print(question.select_one(".vote-count-post"*the class name of the element to scrap*).getText()
#  Now run code  


import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".question-summary")
for question in questions:
    print(question.select_one(".question-hyperlink").getText())
    print(question.select_one(".vote-count-post").getText())