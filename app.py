
###############################################################################
import os
from datetime import datetime
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

import db_opp as db_opp

client = db_opp.create_client()

db = client.test_database
# define collections
users = db.users_collection
dogs = db.dogs_collection
shelters = db.shelters_collection
breeds = db.breeds_collection


# AWS S3
from settings import aws_s3_access_key, aws_s3_secret_access_key

# import boto3
#
# s3 = boto3.client('s3')
#
# response = s3.list_buckets()
#
# buckets = [bucket['Name'] for bucket in response['Buckets']]
# print(buckets)


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
        if self.get_secure_cookie('user'):
            # do this
            logged_in = True
        else:
            logged_in = False
        self.set_header(
          'Cache-Control',
          'no-store, no-cache, must-revalidate, max-age=0')
        self.render_template("/pages/index.html", {"logged_in": logged_in})


class DogFormHandler(TemplateHandler):
    @tornado.web.authenticated
    def get(self):

        user = db_opp.find_user_by_email(self.current_user.decode('utf-8'))

        if user['type'] == "shelter":
            self.set_header(
              'Cache-Control',
              'no-store, no-cache, must-revalidate, max-age=0')
            self.render_template("/pages/dog-form.html", {})
        else:
            self.redirect('/dogs')
    def post(self):
        # import io
        # from PIL import Image

        file_all = self.request.files['my_File'][0]
        file_name = file_all['filename']
        file_body = file_all['body']

        import os

        file_path = os.path.join('static/img/dogs/', file_name)
        if not os.path.exists('static/img/dogs/'):
            os.makedirs('static/img/dogs/')
        print(file_path)
        with open(file_path, 'wb') as f:
            f.write(file_body)
        f.closed

        # # File_Name = File_All.name
        #
        # print(File_Body)
        # # print("+" * 10)
        # # print(File_Name)
        #
        # img = Image.open(io.StringIO(File_Body))
        # import boto3
        # s3 = boto3.resource('s3')
        # bucket = s3.Bucket('images.findmypup.com')
        # obj = bucket.Object('mykey')
        #
        # with open(img, 'rb') as data:
        #     obj.upload_fileobj(data)
        # file_name = self.request.files['my_File'][0]['filename']

        # import boto3
        # s3 = boto3.client('s3')
        # bucket_name = 'images.findmypup.com'
        # s3.upload_file(file_path, bucket_name, file_name)

        # import base64
        # import json
        # image_64_encode = base64.encodestring(file_body)
        # print(image_64_encode)
        #
        user = db_opp.find_user_by_email(self.current_user.decode('utf-8'))

        data = {
            "_id": db_opp.create_uuid(),
            "dog_name": self.get_body_argument('dog_name'),
            "thumbnail": file_path,
            "breed": self.get_body_argument('breed').lower(),
            "id_chip": self.get_body_argument('id_chip'),
            "age": self.get_body_argument('age'),
            "date_found":datetimeconverter( self.get_body_argument('date_found')),
            "location_found": self.get_body_argument('location_found'),
            "prim_color": self.get_body_argument('prim_color').lower(),
            "sec_color": self.get_body_argument('sec_color').lower(),
            "height": self.get_body_argument('height'),
            "weight": self.get_body_argument('weight'),
            "gender": self.get_body_argument('gender', None),
            "fix": self.get_body_argument('fix', None),
            "collar": self.get_body_argument('collar', None),
            "collar_color": self.get_body_argument('collar_color').lower(),
            "ears": self.get_body_argument('ears').lower(),
            "eyes": self.get_body_argument('eyes').lower(),
            "notes": self.get_body_argument('notes'),
            "delete": False,
            "user": user['email'],
            "shelter": user['shelter']
        }
        db_opp.add_new_dog(data)
        self.redirect('/dogs')

        # ADD DOG

class DogListHandler(TemplateHandler):
    @tornado.web.authenticated
    def get(self):
        data = []
        if self.get_argument("gender", None):
            query = {}
            query['gender'] = self.get_argument("gender", None)
            data.append(query)
        if self.get_argument("breed", None):
            query = {}
            query['breed'] = self.get_argument("breed", None)
            data.append(query)
        if self.get_argument("color", None):
            query = {}
            query['color'] = self.get_argument("color", None)
            print(query['color'])
            data.append(query)
        if self.get_argument("age", None):
            query = {}
            query['age'] = int(self.get_argument("age", None))
            data.append(query)
        if self.get_argument("name", None):
            query = {}
            query['name'] = self.get_argument("name", None)
            data.append(query)




        if len(data) < 1:
            dogs_list = db_opp.find_all_public_dogs()
        else:
            dogs_list = db_opp.find_many_dogs(data)
            print("Dogs in Database: {}".format(db_opp.find_all_public_dogs().count()))
            print("Dogs queried: {}".format(db_opp.find_many_dogs(data).count()))
        self.set_header(
          'Cache-Control',
          'no-store, no-cache, must-revalidate, max-age=0')
        self.render_template("/pages/dog-list.html", {"dogs_list": dogs_list})
    # def post(self):
    #     gender = self.get_body_argument("gender", None)
    #     breed = self.get_body_argument("breed", None)
    #     color = self.get_body_argument("color", None).lower()
    #     age = self.get_body_argument("age", None)
    #     name = self.get_body_argument("name", None)
    #
    #     pay
    #
    #     r = requests.post(url, data=json.dumps(payload))


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
class UserProfileHandler(TemplateHandler):
    @tornado.web.authenticated
    def get(self):
        user_data = db_opp.find_user_by_email(self.current_user.decode('utf-8'))
        if user_data['type'] == "owner":
            shelter = False
        else:
            shelter = True
        shelters_list = db_opp.find_all_shelters()

        self.set_header(
          'Cache-Control',
          'no-store, no-cache, must-revalidate, max-age=0')
        self.render_template("/pages/profile.html", {"user": user_data, "shelter": shelter, "shelters_list": shelters_list})

    def post(self):
        _id = self.get_body_argument("id")
        given_name= self.get_body_argument("given_name", None)
        family_name= self.get_body_argument("family_name", None)
        email= self.get_body_argument("email")
        phone= self.get_body_argument("phone", None)
        type = self.get_body_argument("type")
        shelter = self.get_body_argument('shelter', None)
        print(shelter)

        data = {
        "given_name": given_name,
        "family_name": family_name,
        "email": email,
        "phone": phone,
        "type": type,
        "shelter": shelter
        }

        db_opp.update_user_by_id(_id, data)

        self.redirect('/profile')

class SheltersHandler(TemplateHandler):
    @tornado.web.authenticated
    def get(self):
        user = db_opp.find_user_by_email(self.current_user.decode('utf-8'))

        shelters_list = db_opp.find_all_shelters()

        self.set_header(
          'Cache-Control',
          'no-store, no-cache, must-revalidate, max-age=0')
        self.render_template("/pages/shelters.html", {"user": user, "shelters_list": shelters_list})

    def post(self):
        name = self.get_body_argument('name', None)
        email = self.get_body_argument('email', None)
        phone = self.get_body_argument('phone', None)
        address = self.get_body_argument('address', None)
        print("adding shelter")

        if db_opp.find_shelter_by_name(name):
            pass
        else:
            data = {
                "_id": db_opp.create_uuid(),
                "name": name,
                "email": email,
                "phone": phone,
                "address": address
            }
            db_opp.add_new_shelter(data)

        self.redirect("/profile")

class CompleteProfileHandler(TemplateHandler):
    @tornado.web.authenticated
    def get(self):
        user = db_opp.find_user_by_email(self.current_user.decode('utf-8'))

        self.set_header(
          'Cache-Control',
          'no-store, no-cache, must-revalidate, max-age=0')
        self.render_template("/pages/complete-profile.html", {"user": user})

    def post(self):
        data = { "type": self.get_body_argument("type")}
        db_opp.update_user_by_email(self.current_user.decode('utf-8'), data)

        self.redirect("/profile")

class UsersHandler(TemplateHandler):
    def get(self):
        users_list = db_opp.find_all_users()
        self.set_header(
          'Cache-Control',
          'no-store, no-cache, must-revalidate, max-age=0')
        self.render_template("/pages/admin.html", {"users": users_list})


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
            ###################################################################
            #   WRITE NEW USER TO DB                                          #
            ###################################################################
            #        WRITE USER WITH POSTGRES                                 #
            ###################################################################
            # If user does not exists by id in DB, create a user for them..
            # redirect to complete profile

            if db_opp.find_user_by_email(email):
                current_user = db_opp.find_user_by_email(email)
                print(current_user['email'])
                self.set_secure_cookie('user', current_user['email'])
                if current_user['type'] == "not_set":
                    self.redirect('/complete-profile')
                else:
                    self.redirect('/profile')
            else:
                data = {
                "_id": db_opp.create_uuid(),
                "given_name": given_name,
                "family_name": family_name,
                "email": email,
                "avatar": avatar,
                "type": "not_set",
                "shelter": "not_set"
                }
                db_opp.add_new_user(data)

                self.set_secure_cookie('user', email)
                self.redirect("/complete-profile")
                print("added user to db")

            return
        # cookie exists, forward user to site
        elif self.get_secure_cookie('user'):
            self.redirect('/complete-profile')
            return
        # no code, no cookie, try to log them in... via google oauth
        else:
            yield self.authorize_redirect(
                redirect_uri="http://{}/login-google".format(host),
                client_id= self.settings['google_oauth']['key'],
                scope=['email'],
                response_type='code',
                extra_params={'approval_prompt': 'auto'})


# see settings.py for instructions on setting this up
from settings import client_id, project_id, auth_uri, token_uri, auth_provider_x509_cert_url, client_secret, cookie_secret


settings = {
    "debug": True,
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": cookie_secret,
    'google_oauth':{"key":client_id, "secret":client_secret},
    "login_url": "/login",
    "google_redirect_url": "/login-google"
    }


class DogProfileHandler(TemplateHandler):
    def get(self, _id):
        dog = db_opp.find_dog_by_id(_id)
        shelter_name = dog["shelter"]
        shelter = db_opp.find_shelter_by_name(shelter_name)
        print(shelter)
        self.set_header(
          'Cache-Control',
          'no-store, no-cache, must-revalidate, max-age=0')
        self.render_template("/pages/dog-profile.html", {'dog': dog, "shelter": shelter})

class QueryHandler(TemplateHandler):
    def post(self):
        gender = self.get_body_argument("gender", None)
        breed = self.get_body_argument("breed", None)
        color = self.get_body_argument("color", None).lower()
        age = self.get_body_argument("age", None)
        name = self.get_body_argument("name", None)

        # dogs_list = dogs.find({"gender": gender, "breed": breed, "prim_color": color, "age": age, "dog_name": name}).count()
        data = [
        {"gender": gender},
        {"breed": breed},
        {"prim_color": color},
        {"age": age},
        {"dog_name": name}
        ]

        dogs_list = db_opp.find_many_dogs(data)

        self.set_header(
          'Cache-Control',
          'no-store, no-cache, must-revalidate, max-age=0')
        self.render_template("/pages/dog-list-results.html", {'dogs_list': dogs_list, 'breed':breed, 'gender': gender, "color": color, "age": age, "name": name})

class EditDogHandler(TemplateHandler):
    def get(self, _id):
        dog = db_opp.find_dog_by_id(_id)
        self.render_template("pages/dog-profile-edit.html", {"dog":dog})

class UpdateDogHandler(TemplateHandler):
    def post(self):
        _id = self.get_body_argument('_id')
        dog_name = self.get_body_argument('dog_name')
        # "thumbnail": file_path
        breed= self.get_body_argument('breed').lower()
        id_chip= self.get_body_argument('id_chip')
        age= self.get_body_argument('age')
        location_found= self.get_body_argument('location_found')
        prim_color= self.get_body_argument('prim_color').lower()
        sec_color= self.get_body_argument('sec_color').lower()
        height= self.get_body_argument('height')
        weight= self.get_body_argument('weight')
        gender= self.get_body_argument('gender', None)
        fix= self.get_body_argument('fix', None)
        collar= self.get_body_argument('collar', None)
        collar_color= self.get_body_argument('collar_color').lower()
        ears= self.get_body_argument('ears').lower()
        eyes= self.get_body_argument('eyes').lower()
        notes= self.get_body_argument('notes')
        dogs.update_one({"_id":_id}, {'$set': {'dog_name':dog_name, 'age':age, 'breed':breed, 'id_chip':id_chip, 'location_found':location_found, 'collar':collar, 'collar_color':collar_color, 'height':height, 'weight':weight,'prim_color':prim_color, 'sec_color':sec_color, 'eyes':eyes, 'ears':ears, 'notes':notes }})

        self.redirect('/dogs/' + _id)
def datetimeconverter(n):
    #front end date input(n) is always formated {%Y}-{%m}-{%d}
    #converts to datetime object
        return datetime.strptime(n, '%Y-%m-%d')

class DeleteDogHandler(TemplateHandler):
    def post(self):
        # singledelete = self.get_body_argument('singledelete')
        # print(singledelete)

        date_found = self.get_body_argument('date_found')
        end_date = self.get_body_argument('end_date')
        #convert to timeobject
        date_found_obj = datetimeconverter(date_found)
        end_date_obj = datetimeconverter(end_date)
        requests = [UpdateMany({'date_found':{'$gte': date_found_obj, '$lt': end_date_obj}}, {'$set':{'delete':datetime.today()}})]

        dogs_list = dogs.find({'date_found':{'$gte': date_found_obj, '$lt': end_date_obj}})
        dogs.bulk_write(requests)

        self.render_template('pages/deleted.html', {"dogs_list":dogs_list, "date_found":date_found, "end_date":end_date})

class ExportHandler(TemplateHandler):
    def get(self):
        import csv

        myquery = db_opp.find_deleted_dogs()

        with open('some.csv', 'w') as outfile:
            fields = ['_id','dog_name', 'age', 'breed', 'date_found', 'location_found', 'ears', 'eyes', 'gender','fix', 'notes', 'thumbnail', 'sec_color', 'prim_color', 'weight', 'height', 'id_chip', 'collar', 'collar_color', 'delete' ,'user']
            writer = csv.DictWriter(outfile, fieldnames = fields)
            writer.writeheader()
            for x in myquery:
                writer.writerow(x)
        outfile.close()

class make_app(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/login", LoginHandler),
            (r"/logout", LogOutHandler),
            (r"/login-google", GAuthLoginHandler),
            (r"/complete-profile", CompleteProfileHandler),
            (r"/profile", UserProfileHandler),
            (r"/admin", UsersHandler),
            (r"/dogs/new-dog", DogFormHandler),
            (r"/dogs", DogListHandler),
            (r"/edit/(.*)",EditDogHandler),
            (r"/update", UpdateDogHandler),
            (r"/delete", DeleteDogHandler),
            (r"/querybar", QueryHandler),
            (r"/export", ExportHandler),
            (r"/shelters", SheltersHandler),
            (r"/dogs/(.*)",DogProfileHandler),
            (
                r"/static/(.*)",
                tornado.web.StaticFileHandler,
                {'path': 'static'}
                )
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
