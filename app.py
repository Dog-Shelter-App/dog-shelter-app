import os

# Needed to run server, event loop and basic server logging
import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.log
import tornado.websocket
# import tornado.asyncio
from jinja2 import \
    Environment, PackageLoader, select_autoescape


# Environment variable. Defines location of template files, declares what MUL are interpreted
# IMPORTANT: must include __init__.py file in top directory. in this case '/myapp'
ENV = Environment(
    loader = PackageLoader('myapp','templates'),
    autoescape = select_autoescape(['html', 'xml'])
)

PORT = int(os.environ.get('PORT', '8080'))

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("websocket is open")
        list = []
        list.append(3)
        print(list)
        x = 'hello'
        # with open('data.json', 'r') as fh:
        #   data = json.load(fh)

    def on_message(self, message):
        # list.extend(message)
        print(list)
        # data = open()
        self.write_message(u"<li>" + message + "</li>")

# handler defines how a page handler will get template files and context information
class TemplateHandler(tornado.web.RequestHandler):
  def render_template (self, tpl, context):
    template = ENV.get_template(tpl)
    self.write(template.render(**context))

# main handler, passes in template handler for finding template files
class MainHandler(TemplateHandler):
  def get(self):
    self.set_header(
      'Cache-Control',
      'no-store, no-cache, must-revalidate, max-age=0')
    self.render_template("index.html", {'name': 'World'})


settings = {
    "debug": True,
    "static_path": os.path.join(os.path.dirname(__file__), "static")
}


class make_app(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/websocket", WebSocketHandler),
            (r"/(styles\.css)", tornado.web.StaticFileHandler,
             dict(path=settings['static_path'])),
        ]
        tornado.web.Application.__init__(self, handlers, autoreload=True, **settings)


if __name__ == "__main__":
    tornado.log.enable_pretty_logging()
    ws_app = make_app()
    server = tornado.httpserver.HTTPServer(ws_app)
    # enables logging of updated files.
    server.listen(PORT)
    tornado.ioloop.IOLoop.current().start()
