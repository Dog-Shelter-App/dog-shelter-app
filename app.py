import os

# Needed to run server, event loop and basic server logging
import tornado.ioloop
import tornado.web
import tornado.log
from jinja2 import \
    Environment, PackageLoader, select_autoescape


# Environment variable. Defines location of template files, declares what MUL are interpreted
# IMPORTANT: must include __init__.py file in top directory. in this case '/myapp'
ENV = Environment(
    loader = PackageLoader('myapp','templates'),
    autoescape = select_autoescape(['html', 'xml'])
)

PORT = int(os.environ.get('PORT', '8080'))

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



def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/(styles\.css)", tornado.web.StaticFileHandler,
         dict(path=settings['static_path'])),
    ], **settings, autoreload=True)
if __name__ == "__main__":
    # enables logging of updated files.
    tornado.log.enable_pretty_logging()
    app = make_app()
    app.listen(PORT)
    tornado.ioloop.IOLoop.current().start()
