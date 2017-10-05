import os

# Needed to run server, event loop and basic server logging
import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.log
import tornado.websocket

# needed to run templating engine
from jinja2 import \
    Environment, PackageLoader, select_autoescape

# needed for database queries
import pymongo
from pymongo import MongoClient

#############################################################################################

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


def print_step(input):
    print("="*100)
    print("{}".format(input))
    print("="*100)


 # request URL
def make_soup(url):
    print_step("Step 1. Request a url.")
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

############################################################################################

# Environment variable. Defines location of template files, declares what MUL are interpreted
# IMPORTANT: must include __init__.py file in top directory. in this case '/myapp'
ENV = Environment(
    loader = PackageLoader('myapp','templates'),
    autoescape = select_autoescape(['html', 'xml'])
)

# set default port for server env
PORT = int(os.environ.get('PORT', '8902'))

DATABASE_URL = os.environ.get(
  'DATABASE_URL',
  'postgres://postgres:e6aef3b4b5685d1ad42a72f5c641853f@dokku-postgres-crmdb:5432/crmdb'
)



# open client to db that runs infinitely during the app runtime.
client = pymongo.MongoClient("mongodb://kevin:Bettyb00p!@cluster0-shard-00-00-fqbin.mongodb.net:27017,cluster0-shard-00-01-fqbin.mongodb.net:27017,cluster0-shard-00-02-fqbin.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin")
db = client.test

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("websocket is open")
        # db.inventory.find({
        #     "message" : (.*)
        # })

    def on_message(self, message):
        # list.extend(message)
        db.messages.insert_one({"message": message})
        messages_list = db.messages.find({})

# handler defines how a page handler will get template files and context information
class TemplateHandler(tornado.web.RequestHandler):
  def render_template (self, tpl, context):
    template = ENV.get_template(tpl)
    self.write(template.render(**context))

# main handler, passes in template handler for finding template files
class MainHandler(TemplateHandler):
    def get(self):
        messages = db.messages.find({})
        self.set_header(
          'Cache-Control',
          'no-store, no-cache, must-revalidate, max-age=0')
        self.render_template("pages/index.html", {'messages': messages})

class MessagingHandler(TemplateHandler):
    def get(self):
        messages = db.messages.find({})
        self.set_header(
          'Cache-Control',
          'no-store, no-cache, must-revalidate, max-age=0')
        self.render_template("messaging.html", {'messages': messages})

class PyScraperHandler(TemplateHandler):
    def get(self):
        url = self.get_argument("url")

        if not url:
            url = "https://en.wikipedia.org/wiki/Chuck_Norris"
        soup = make_soup(url)

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
        print(words)

        self.set_header(
          'Cache-Control',
          'no-store, no-cache, must-revalidate, max-age=0')
        self.render_template("py-scraper.html", {'words': words, 'url': url})

class DeleteMessageHandler(TemplateHandler):
    def get(self):
        db.messages.delete_many({})
        messages = db.messages.find({})
        self.set_header(
            'Cache-Control',
            'no-store, no-cache, must-revalidate, max-age=0'
        )
        self.render_template("pages/index.html", {'messages': messages})

settings = {
    "debug": True,
    "static_path": os.path.join(os.path.dirname(__file__), "static")
}


class make_app(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/messaging", MessagingHandler),
            (r"/websocket", WebSocketHandler),
            (r"/delete", WebSocketHandler),
            # (r"/(styles\.css)", tornado.web.StaticFileHandler,
            #  dict(path=settings['static_path'])),
            (r"/py-scraper", PyScraperHandler),
        ]
        tornado.web.Application.__init__(self, handlers, autoreload=True, **settings)


if __name__ == "__main__":
    tornado.log.enable_pretty_logging()
    ws_app = make_app()
    server = tornado.httpserver.HTTPServer(ws_app)
    # enables logging of updated files.
    server.listen(PORT)
    tornado.ioloop.IOLoop.current().start()
