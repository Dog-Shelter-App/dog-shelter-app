import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop

import json
import websocket

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def __init__(self):
        print(self)

    def open(self):
        print("websocket is open")

    def on_message(self, message):
        print(message)

    def on_close(self):
        print("websocket is closed")

class IndexPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header('Cache-Control','no-store, no-cache, must-revalidate, max-age=0')
        self.render("index.html")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndexPageHandler),
            (r'/websocket', WebSocketHandler)
        ]

        settings = {
            'template_path': 'templates'
        }
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    ws_app = Application()
    server = tornado.httpserver.HTTPServer(ws_app)
    server.listen(8888, print('now listening on port 8080'))
    tornado.ioloop.IOLoop.instance().start()
