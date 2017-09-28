import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop

import json
import pprint
import websocket
# from websocket import create_connection

# websocket.enableTrace(True)
# ws = create_connection("ws://localhost:8080/websocket")

# result = ws.recv()
# print(‘Result: {}‘.format(result))
#
# result = ws.recv()
# print(‘Result: {}‘.format(result))
#
# ws.send(json.dumps([json.dumps({‘msg’: ‘connect’, ‘version’: ‘1’, ‘support’: [‘1’, ‘pre2’, ‘pre1’]})]))
# result = ws.recv()
# print(‘Result: {}‘.format(result))


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    # def __init__(self):
    #     with open('data.json') as json_data:
    #         d = json.loads(json_data)
    #         json_data.close()
    #         pprint(d)

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

    # def on_close(self):
    #     print("websocket is closed")
    #     pass


class IndexPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header('Cache-Control','no-store, no-cache, must-revalidate, max-age=0')
        self.render("index.html")

        #     d = json.loads(json_data)
        #     print('works')
        #     json_data.close()
            # pprint(d)


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
    server.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
