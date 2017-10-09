
###############################################################################
import os
# Needed to run server, event loop and basic server logging
import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.log
import tornado.websocket
import tornado.auth

# needed to run templating engine
from jinja2 import \
    Environment, PackageLoader, select_autoescape

# needed for database queries
import pymongo
from pymongo import MongoClient

###############################################################################

# Localized Services

import services.py_scraper
py_scraper = services.py_scraper

import services.messanger_pygeon
messanger_pygeon = services.messanger_pygeon

client = pymongo.MongoClient("mongodb://kevin:Bettyb00p!@cluster0-shard-00-00-fqbin.mongodb.net:27017,cluster0-shard-00-01-fqbin.mongodb.net:27017,cluster0-shard-00-02-fqbin.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin")
db = client.test

###############################################################################

# Environment variable. Defines location of template files, declares what MUL are interpreted
# IMPORTANT: must include __init__.py file in top directory. in this case '/myapp'
ENV = Environment(
    loader = PackageLoader('myapp','templates'),
    autoescape = select_autoescape(['html', 'xml'])
)

# set default port for server env
PORT = int(os.environ.get('PORT', '8902'))

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

# handler defines how a page handler will get template files and context information
class TemplateHandler(BaseHandler):
  def render_template (self, tpl, context):
    template = ENV.get_template(tpl)
    self.write(template.render(**context))

# main handler, passes in template handler for finding template files
class MainHandler(TemplateHandler):
    @tornado.web.authenticated
    def get(self):
        user = tornado.escape.xhtml_escape(self.current_user)
        self.set_header(
          'Cache-Control',
          'no-store, no-cache, must-revalidate, max-age=0')
        self.render_template("pages/index.html", {'user': user})

class LoginHandler(BaseHandler):
    def get(self):
        self.write('<html><body><form action="/login" method="post">'
                   'Name: <input type="text" name="name">'
                   '<input type="submit" value="Sign in">'
                   '</form></body></html>')

    def post(self):
        self.set_secure_cookie("user", self.get_argument("name"))

        self.redirect("/")

class LogOutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("user")
        self.redirect(self.get_argument("next", "/"))

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

class MessagingHandler(TemplateHandler):
    def get(self):
        messages = db.messages.find({})
        self.set_header(
          'Cache-Control',
          'no-store, no-cache, must-revalidate, max-age=0')
        self.render_template("messaging.html", {'messages': messages})

class PyScraperHandler(TemplateHandler):
    def get(self):
        # get url parameter
        url = "https://www.vice.com/en_us/article/a3kpv4/i-waited-for-mcdonalds-szechuan-sauce-and-it-was-fine"
        url = self.get_argument("url")
        # scrape url and pass to template
        words = py_scraper.py_scrape(url)

        self.set_header(
          'Cache-Control',
          'no-store, no-cache, must-revalidate, max-age=0')
        self.render_template("py-scraper.html", {'words': words, 'url': url})

settings = {
    "debug": True,
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": "sdflk2j3f23f2lk2jf30ijsdflkjff0j998h98h",
    "login_url": "/login"
}


class make_app(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/login", LoginHandler),
            (r"/logout", LogOutHandler),
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
