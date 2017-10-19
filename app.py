
###############################################################################
import os
import datetime
import json
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

import requests


###############################################################################

# Localized Services Imported Here

from services.uimodules import Menu
import services.db_opperations as db_opp

# pull creds
from settings import mongo_url
# import driver
import pymongo
# import client function
from pymongo import MongoClient
# create client
client = pymongo.MongoClient(mongo_url)
# define database
db = client.test_database
# define collections
collection = db.test_collection
users = db.user_collection
dogs = db.dogs_collection

##########################
#### cluster
######## database
############ collection
################ document



###############################################################################

# Environment variable. Defines location of template files, declares what MUL are interpreted
# IMPORTANT: must include __init__.py file in top directory. in this case '/myapp'
ENV = Environment(
    loader = PackageLoader('myapp','templates'),
    autoescape = select_autoescape(['html', 'xml'])
)

# set default port for server env
PORT = int(os.environ.get('PORT', '8080'))

# main handler, passes in template handler for finding template files
class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        user_cookie = self.get_secure_cookie("user")
        return user_cookie

# handler defines how a page handler will get template files and context information
class TemplateHandler(BaseHandler):
  def render_template (self, tpl, context):
    template = ENV.get_template(tpl)
    self.write(template.render(**context))

class MainHandler(TemplateHandler):
    def get(self):
        login = self.get_argument('login', None)
        user = self.get_current_user
        messages = collection.find({})
        users = db.user_collection.find({})
        self.set_header(
          'Cache-Control',
          'no-store, no-cache, must-revalidate, max-age=0')
        self.render_template("/pages/index.html", {"login": login, "users": users, "messages": messages})

    def post(self):
        text = self.get_body_argument('text')
        result = collection.insert_one(
            {"text": text}
        )
        self.redirect('/')

class SignupHandler(TemplateHandler):
    def get(self):
        self.set_header(
          'Cache-Control',
          'no-store, no-cache, must-revalidate, max-age=0')
        self.render_template("pages/signup.html", {"user": "Kevin"})
    def post(self):
        given_name = self.get_body_argument('given_name')
        family_name = self.get_body_argument('family_name')
        email = self.get_body_argument('email')
        password = self.get_body_argument('password')
        zip_code = self.get_body_argument("zip")
        if User.select().where(User.email == email).count() == 0:
            User.create(
                first_name = given_name,
                last_name = family_name,
                email = email,
                password = password,
                zip = zip_code,
                auth = "tornado"
                )
            self.redirect("/login")
        else:
            raise tornado.web.HTTPError(500,  "user already exists.")
            self.redirect('/login?status=signup')

class DogFormHandler(TemplateHandler):
    def get(self):
        self.set_header(
          'Cache-Control',
          'no-store, no-cache, must-revalidate, max-age=0')
        self.render_template("/pages/dog-form.html", {"user": "kevin"})
    def post(self):
        # call add dog function from db opperations
        dogs.insert_one(
            {
            "dog_name": self.get_body_argument('dog_name'),
            "my_File": self.get_body_argument('my_File'),
            "breed": self.get_body_argument('breed'),
            "id_chip": self.get_body_argument('id_chip'),
            "location_found": self.get_body_argument('location_found'),
            "prim_color": self.get_body_argument('prim_color'),
            "sec_color": self.get_body_argument('sec_color'),
            "height": self.get_body_argument('height'),
            "weight": self.get_body_argument('weight'),
            "gender": self.get_body_argument('gender', None),
            "fix": self.get_body_argument('fix', None),
            "collar": self.get_body_argument('collar', None),
            "collar_color": self.get_body_argument('collar_color'),
            "ears": self.get_body_argument('ears'),
            "eyes": self.get_body_argument('eyes'),
            "notes": self.get_body_argument('notes')
            }
        )
        entry = dogs.find(
        {
        "dog_name": "Dog"
        }
        )
        print(entry)
        self.redirect('/dog-list')
        # ADD DOG

class DogListHandler(TemplateHandler):
    def get(self):
        dogs_list = dogs.find({})
        self.set_header(
          'Cache-Control',
          'no-store, no-cache, must-revalidate, max-age=0')
        self.render_template("/pages/dog-list.html", {"dogs_list": dogs_list})





class LoginHandler(TemplateHandler):
    def get(self):
        status = self.get_argument('status', None)
        reason = "Log In"
        if status == "fail":
            reason = "Incorrect Username or Password"
        if self.get_secure_cookie('user'):
            self.redirect('/profile?status=good')
        else:
            path = self.request
            destination = self.get_argument('next', None)
            # print("next is {}".format(request_path))
            data = 4
            self.set_header(
              'Cache-Control',
              'no-store, no-cache, must-revalidate, max-age=0')
            self.render_template("/pages/login.html", {"data": data, "reason": reason})

    def post(self):
        email = self.get_argument('email')
        password = self.get_argument('password')
        if User.select().where(User.email == email).count() == 0:
            print("no user found")
            # raise tornado.web.HTTPError(404, 'No Account with that email address.')
            self.redirect("/signup?user=null")
        else:
            user = User.select().where(User.email == email).get()
        if user.password != password:
            self.redirect('/login?status=fail')
            raise tornado.web.HTTPError(403, "Incorrect username or password.")
        else:
            self.set_secure_cookie("user", email)
        self.redirect('/profile')

class LogOutHandler(BaseHandler, tornado.auth.GoogleOAuth2Mixin):
    def get(self):
        self.clear_cookie("user")
        self.redirect("/?login=false")

class GAuthLoginHandler(BaseHandler, tornado.auth.GoogleOAuth2Mixin):
    @tornado.gen.coroutine
    def get(self):
        # TRY: REMEMBER WHERE USER WANTED TO GO
        # request = self.request.headers.get("Referer")
        # question = request.find('=')
        # next_path = request[question+1:]

        # Set host: used for compatibility with localhost and external servers.
        host = self.request.host

        # if there is a code in the url
        if self.get_argument('code', False):
            # check if user is already authenticated
            user = yield self.get_authenticated_user(redirect_uri="http://{}/login-google".format(host),
                code= self.get_argument('code'))
            # if not, then there should not be a code and we throw error.
            if not user:
                self.clear_all_cookies()
                print("ERROR 500")
                raise tornado.web.HTTPError(500, 'Google authentication failed')

            # send the user back to google auth to reverify their token
            # take whatever access token is set in the browser
            access_token = str(user['access_token'])
            # send user to google authentication server
            http_client = self.get_auth_http_client()
            # load response
            response =  yield http_client.fetch('https://www.googleapis.com/oauth2/v1/userinfo?access_token='+access_token)
            # if there is no response... something went wrong
            if not response:
                self.clear_all_cookies()
                raise tornado.web.HTTPError(500, 'Google authentication failed')
            # If you are here, then google responded, continue reading the response
            user = json.loads(response.body)

            # unpack the info google sent

            name = user['name']
            given_name = user['given_name']
            family_name = user['family_name']
            email = user['email']
            avatar = user['picture']
            user_id = user["id"]


            # google says they are cool, and we believe them
            # save user here, save to cookie or database
            self.set_secure_cookie('user', user['email'])

            ###################################################################
            #   WRITE NEW USER TO DB                                          #
            ###################################################################
            #        WRITE USER WITH POSTGRES                                 #
            ###################################################################

            # If user does not exists by id in DB, create a user for them..
            # redirect to complete profile
            users.insert_one(
                {
                "given_name": given_name,
                "family_name": family_name,
                "email": email,
                "avatar": avatar,
                "user_id": user_id
                }
            )
            ###################################################################
            #        WRITE USER WITH MONGODB                                  #
            ###################################################################
            # CODE GOES HERE
            ###################################################################

            # user exists, redirect to profile page.
            self.redirect('/profile')


            return
        # cookie exists, forward user to site
        elif self.get_secure_cookie('user'):
            self.redirect('/profile')
            return
        # no code, no cookie, try to log them in... via google oauth
        else:
            yield self.authorize_redirect(
                redirect_uri="http://{}/login-google".format(host),
                client_id= self.settings['google_oauth']['key'],
                scope=['email'],
                response_type='code',
                extra_params={'approval_prompt': 'auto'})


##############################################################################
class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        pass
        # db.inventory.find({
        #     "message" : (.*)
        # })

    def on_message(self, message):
        # list.extend(message)
        db.messages.insert_one({"message": message})
        messages_list = db.messages.find({})

class MessagingHandler(TemplateHandler):
    # Add this decorator to restrict access to logged in users.
    @tornado.web.authenticated
    def get(self):
        messages = "db.messages.find({})"
        self.set_header(
          'Cache-Control',
          'no-store, no-cache, must-revalidate, max-age=0')
        self.render_template("messaging.html", {'messages': messages})

class ProfileHandler(TemplateHandler):
    # Add this decorator to restrict access to logged in users.
    @tornado.web.authenticated
    def get(self):
        user_list = users.find({})
        status = self.get_argument('status', None)
        header = "Your Profile"
        if status == "update":
            header = "Profile Updated"
        elif status == "good":
            header = "Already Logged In"
        cookie = self.current_user
        self.set_header(
          'Cache-Control',
          'no-store, no-cache, must-revalidate, max-age=0')
        self.render_template("pages/profile.html", {"users": user_list})
    def post(self):
        # Get ID
        email = self.get_body_argument('email')
        # Write data to user
        user.first_name = self.get_body_argument('first_name')
        user.last_name = self.get_body_argument('last_name')
        user.phone = self.get_body_argument('phone')
        user.save()
        self.redirect('/profile?status=update')

class MenuModule(tornado.web.UIModule):
    def render(self):
        return self.render_string("menu.html")



# see settings.py for instructions on setting this up
from settings import client_id, project_id, auth_uri, token_uri, auth_provider_x509_cert_url, client_secret, cookie_secret

print(client_id)

settings = {
    "debug": True,
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": cookie_secret,
    'google_oauth':{"key":client_id, "secret":client_secret},
    "login_url": "/login",
    "google_redirect_url": "/login-google",
    "ui_modules": {"Menu": Menu}
    }


class make_app(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/login", LoginHandler),
            (r"/logout", LogOutHandler),
            (r"/login-google", GAuthLoginHandler),
            (r"/profile", ProfileHandler),
            (r"/messaging", MessagingHandler),
            (r"/dog", DogFormHandler),
            (r"/dog-list", DogListHandler),
            (r"/websocket", WebSocketHandler)
        ]
        # ui_modules = {'Menu': uimodule.Terminal}
        tornado.web.Application.__init__(self, handlers, autoreload=True, **settings)


if __name__ == "__main__":
    tornado.log.enable_pretty_logging()
    ws_app = make_app()
    server = tornado.httpserver.HTTPServer(ws_app)
    # enables logging of updated files.
    server.listen(PORT)
    tornado.ioloop.IOLoop.current().start()
