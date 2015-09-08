#djangocon-web
[![Build Status](https://travis-ci.org/vpatel85/djangocon-web.svg?branch=master)](https://travis-ci.org/vpatel85/djangocon-web)

clustering people at djangocon 2015. Check out the project's [documentation](http://vpatel85.github.io/djangocon-web/).

# Prerequisites 
- [virtualenv](https://virtualenv.pypa.io/en/latest/)
- [postgresql](http://www.postgresql.org/)
- [redis](http://redis.io/)
- [travis cli](http://blog.travis-ci.com/2013-01-14-new-client/)
- [heroku toolbelt](https://toolbelt.heroku.com/)

# Initialize the project
Create and activate a virtualenv:

```bash
virtualenv env
source env/bin/activate
```
Install dependencies:

```bash
pip install -r requirements/local.txt
```
Create the database:

```bash
createdb cluster
```
Initialize the git repository

```
git init
git remote add origin git@github.com:vpatel85/djangocon-web.git
```

Migrate, create a superuser, and run the server:
```bash
python cluster/manage.py migrate
python cluster/manage.py createsuperuser
python cluster/manage.py runserver
```

# Create Servers
By default the included fabfile will setup three environments:

- dev -- The bleeding edge of development
- qa -- For quality assurance testing
- prod -- For the live application

Create these servers on Heroku with:

```bash
fab init
```

# Automated Deployment
Deployment is handled via Travis. When builds pass Travis will automatically deploy that branch to Heroku. Enable this with:
```bash
travis encrypt $(heroku auth:token) --add deploy.api_key
```
