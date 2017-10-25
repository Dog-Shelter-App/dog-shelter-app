#GET MY PUP
## A ready-made operations tool for Animal shelters to store animals, query, and update.

[DigitalCrafts](http://www.DigitalCrafts.com)' group project week
###[Juliana Mei](http://github.com/julianapeace)
###[Kevin Meinhardt](https://github.com/KevinMind)
###[Gustavo Martinez](https://github.com/gmartinez31)
---------

### Summary
Houston's animal rescue organizations are overwhelmed by a large number of incoming lost/stray animals. All shelters triage their incoming animals into their own proprietary internal database.

This project aims to unify Houston's animal database into one powerful tool that is easily accommodate high incoming rates and high kill rates. It answers the current cities fragmented query options so no owner would have to dedicate hours to comb through multiple outdated websites, call and be placed on hold, and spend hours walking through kennels.

---------

### MVP (Minimum Viable Product)
- [x] User can add an animal
- [x] User can view an animal
- [x] User can query animal database

---------

### Stretch Goals
- [x] Users have full CRUD functionality
- [x] Users can followup when they CLAIM a dog
- [x] Users can QUERY animals

## KEY FEATURES
-Three User Types: 'Not Set', 'Owner', 'Shelter'
-A record of delete animals can be exported into a CSV

--------
## Developer Notes
### Group Project Week: October 16-25

## What your project does?
Our project is the solution to answer Houston's currently fragmented animal databases.

## The technology you used?
We used MongoDB, PyMongo, Python, Javascript, JQuery, SCSS, HTML

## Problems you encountered and how you solved them.

Git Git Git!!! On day one, we kept encountering merge conflicts. Whether it was *friggin* pycache files or we accidentally worked on the same file together, we learned a lot. Working as a group took a good amount of soft skills.

## Anything else cool?

We're really impressed with how incredibly filled out their idea became. We started the project with a super simple MVP. We achieved MVP status by day two. We spent the rest of the project week fleshing out features we "wished" it would do. Like the ability to mass delete animals. if this product is going to market, it needed to fit into Houstons' current high-kill workflow.

And we created a pretty expansive user level system! Users need to have certain credentials to be able to delete dogs or access admin pages (like export to csv/ view all users/ add a shelter)

------

Tornado_Starter Template by
Kevin Meinhardt

twitter: https://twitter.com/kevinmeinhardt2
github: https://www.github.com/kevinmind

##clone repo

$ git clone https://github.com/Dog-Shelter-App/dog-shelter-app.git

$ cd dog-shelter-app

$ virtualenv -a `pwd` -p `which python3`

##pip install requirements: tornado jinja2 and pymongo

$ pip install -r requirements.txt

##install frontend framework and file manager (if you need a front end)

$npm install

$gulp

##run app

$ python app.py

##

## go to http://localhost:8080

##add your services to the services folder and import them to your app.py file with

import services.<your service>
<your service name> = service.<your service>

call a function from your service

<your service name>.<your service's function>()

#prints out "hello world... or something."

URL FOR GOOGLE CONSOLE
https://console.cloud.google.com/home
