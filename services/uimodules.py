import tornado.web


class Menu(tornado.web.UIModule):
    def render(self):
        return '<div>THE MODULE HAS ARRIVED</div>'
