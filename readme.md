# GET MY PUP
## A full operations tool for animal rescue shelters to keep animal inventory up-to-date with extreme ease.

### [DigitalCrafts](https://www.DigitalCrafts.com)' group project week

### [Juliana Mei](https://github.com/julianapeace)

### [Kevin Meinhardt](https://github.com/KevinMind)

### [Gustavo Martinez](https://github.com/gmartinez31)

---------

### Summary
Houston's animal rescue organizations are overwhelmed by a large number of incoming lost/stray animals. All shelters triage their incoming animals into their own proprietary internal database.

This project aims to unify Houston's animal database into one powerful tool that easily accommodates shelters with high incoming and high kill rates. It answers the currently fragmented options. Now owner don't have to dedicate hours combing through multiple outdated websites, call and be placed on hold, or spend hours walking through kennels.

---------

### MVP (Minimum Viable Product)
- [x] User can add an animal
- [x] User can view an animal
- [x] User can query animal database

---------

### Stretch Goals
- [x] Users have full CRUD (Create, Read, Update, Delete) functionality
- [x] Users can followup when they CLAIM a dog
- [x] Users can filter animals
- [ ] AWS S3 Boto3 Image storage



## KEY FEATURES
- [x] Three User Types: 'Not Set', 'Owner', 'Shelter'
Shelters have admin privileges like Add/Delete/Edit/Mass-delete dogs. Owners can only query. 'Not Set' can only view dog database.
- [x] A record of deleted animals can be exported into a CSV
- [x] A function to add 100 dogs to the database including AI sentence generation
- [x] Notifications when dogs are found
- [x] Secure authentication
- [x] Multi-part form entry for simple usability

--------
## Developer Notes
### Group Project Week: October 16-25

## What your project does?
Our project is the solution to answer Houston's currently fragmented animal databases.

## The technology you used?
We used MongoDB, PyMongo, Python, Javascript, JQuery, CSS, HTML, Jinja, Tornado, AWS Lightsail

## Problems you encountered and how you solved them.

Git Git Git!!! On day one, we kept encountering merge conflicts. Whether it was *friggin* pycache files or we accidentally worked on the same file together, we learned a lot. Working as a group took a good amount of soft skills.

## Anything else cool?

We're really impressed with how incredibly filled out their idea became. We started the project with a super simple MVP. We achieved MVP status by day two. We spent the rest of the project week fleshing out features we "wished" it would do. Like the ability to mass delete animals. if this product is going to market, it needed to fit into Houstons' current high-kill workflow.

And we created a pretty expansive user level system! Users need to have certain credentials to be able to delete dogs or access admin pages (like export to csv/ view all users/ add a shelter)

We can pre-populate the entire database with auto-generators. With one command, we can load hundreds of dogs with pseudo-profiles and AI generated sentences!
------
