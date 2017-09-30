import tornado.ioloop
import tornado.web
import motor

class ContactHandler(tornado.web.RequestHandler):

    def get(self):
        """Show the basic contact form"""

        self.write('''
        User Contact Form

        -----------------</pre>
<form method="post">user Name: <input type="text" name="username" />

 Phone: <input type="text" name="phone" />

 Email: <input type="text" name="email" />

 <input type="submit" /></form>
<pre>
''')

    # Method exits before the HTTP request completes, thus "asynchronous"
    @tornado.web.asynchronous
    def post(self):
        """Insert user contact details"""
        username = self.get_argument('username')
        phone = self.get_argument('phone')
        email = self.get_argument('email')

        # Async insert; callback is executed when insert completes
        self.settings['db'].users.insert({
                'username': username,
                'phone': phone,
                'email': email
            },
        callback=self._on_response)

    def _on_response(self, result, error):
        if error:
            raise tornado.web.HTTPError(500, error)
        else:
            self.redirect('/')

class ContactDisplayHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        """Display all contacts"""

        self.write('<a href="/contact">Add contact</a>

')
        self.write('User contact list
')
        self.write('')
        db = self.settings['db']
        db.users.find().sort([('_id', -1)]).each(self._got_data)

    def _got_data(self, data, error):
        if error:
            raise tornado.web.HTTPError(500, error)
        elif data:
            self.write(
                '' % (
                    data['username'],
                    data['phone'],
                    data['email']
                )
            )
        else:
            # Iteration complete
            self.write('</pre>
<table>
<tbody>
<tr>
<td>%s</td>
<td>%s</td>
<td>%s</td>
</tr>
</tbody>
</table>
<pre>
')
            self.finish()
 
#connecting to the asynchronously using motor.
#Database name "example"
db = motor.MotorClient().open_sync().example

application = tornado.web.Application([
        (r'/contacts', ContactDisplayHandler),
        (r'/add-contact', ContactHandler),
    ], db=db
)

print 'Listening on http://localhost:8888'
application.listen(8888)
tornado.ioloop.IOLoop.instance().start()
