import os
import urllib.request
from bs4 import BeautifulSoup

#html cleaner
import lxml
from lxml.html.clean import Cleaner

# natural language processing
import nltk

cleaner = Cleaner()
cleaner.javascript = True # This is True because we want to activate the javascript filter
cleaner.style = True      # This is True because we want to activate the styles & stylesheet filter

# CLI interface
def print_step(input):
    print("="*100)
    print("{}".format(input))
    print("="*100)


 # request URL
def make_soup():
    print_step("Step 1. Request a url.")
    url = input("feed me a link.")
    # url = "https://en.wikipedia.org/wiki/Python"
    # go get your html page
    html_obj = get_ingredients(url)
    # clean up the html page
    html_string = (html_obj.read().decode('utf-8'))
    # soupify
    clean_html = cleaner.clean_html(html_string)
    soup = BeautifulSoup(clean_html, 'lxml')
    return soup


def validate_url(url):
    if "www" in url:
        print_step("Fantastic. URL received.")
        return True
    else:
        url = input("Silly human. Your URL needs a www. at the beginning...")

# remove javascript and css styling from the page.
def clean_ingredients(html):
    p_clean = lxml.html.tostring(cleaner.clean_html(lxml.html.parse(html)))
    # p_clean = lxml.html.parse(html)
    # print(p_clean)
    return p_clean

# make http request
def get_ingredients(url):
    # create request
    request = urllib.request.Request(url)
    # return the response
    response = urllib.request.urlopen(request)
    return response




# p_head = soup.head
# p_body = soup.body
# p_footer = soup.footer

# print("=====\n",p_head,"=====\n",p_body,"=====\n",p_footer)

# links for page
# for link in soup.find_all('a'):
#     print(link.get('href'))
# for h1 in soup.find_all('h1'):
#     print(h1.get(h1))

# soup.title
# <title>The Dormouse's story</title>

# soup.title.name
# u'title'



# page_title_container = soup.title.parent.name
# u'head'

# soup.p
# <p class="title"><b>The Dormouse's story</b></p>

# soup.p['class']
# u'title'

# soup.a
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

# soup.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# soup.find(id="link3")
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
# tags = p_body.find_all('meta')
#


# for tag in tags:
#     i = 1
#     print("{}===>\n{}===>\n\n\n".format(i, tag['content']))


soup = make_soup()

p_body = soup.body

words = []
check_list = []

for string in p_body.strings:
    string_list = string.split(" ")
    for word in string_list:
        # print("{} => {} ==> {}".format(len(word),type(word),word))
        if word in check_list:
            pass
        else:
            words.append(word.strip())
            check_list.append(word.strip())
print(text)
