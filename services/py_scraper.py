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
def make_soup(url):
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

def py_scrape(url):
    # make soup
    soup = make_soup(url)
    # trim fat
    p_body = soup.body
    # word store
    words = []
    # word check
    check_list = []
    # unique words
    for string in p_body.strings:
        string_list = string.split(" ")
        for word in string_list:
            # print("{} => {} ==> {}".format(len(word),type(word),word))
            if word in check_list:
                pass
            else:
                words.append(word.strip())
                check_list.append(word.strip())
    return words
