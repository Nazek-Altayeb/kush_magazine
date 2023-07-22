# Goal

Develop an online magazine where moderators could write articles of different topics,
login users could write comments and like articles, where also guests would have the ability to read and search articles.

# Target audience

- Readers who are interested in online magazines.

# User Experience

## User Stories

1. As a website owner I want to:
   - Manage access priviliges.
2. As a Moderator I want to:
   - Write, update and delete my own articles.
3. As a user I want to:
   - comment on articles, and like.
   - I can search for an article.
   - I can filter articles according to topics.
   - Bookmark articles.
4. As a guest I want to:
   - Read articles.

## Design

## Colors

## Typography

# System analysis / Use case diagram

![Use case duagram](/static/images/usecase-diagram.png)

# Database Design / ERD

![ERD](/static/images/ERD-diagram.png)

# UX Plane

## Scope

## Logic Path

# Agile workflow

With the use of GitHub's kanban board, issues have been listed with labels for each, prioritising them in a manner that meets the project objective.

1. Adding essential features first
   - Backend functionalities have been added as a first iteration (install required libraries, create database with related tables, CRUD functionalities).
   - As a next step, templates and views that relate to CRUD have been done as a second iteration.
   - authentication with allauth take a place as a third step after testing the CRUD.
2. GitHub Features / Issues
   - The user stories have been given a Github issue, each is prioritized and is a given one of three labels (Must have , Should have, Could have).
     ![Issues](/static/images/issues.png).

# Implementation Plan

1.  Data layer
    1. Create the following database tables as models in models.py (Article, User, Comment, Topic, Like)
    2. Migrate to database
2.  Back-end
3.  Presentation layer

# Existing Features

1. CRUD articles
2. Comment on article
3. like an article
4. filter articles
5. search for article
6. Bookmark an article
7. Manage access piviliges

# Testing

# Fixed Bugs

# Planned features

# Deployment

# Technologies

## Environments and Hosting

- [Figma](https://www.figma.com/) (Wireframes)
- [Lucid](https://lucid.app/) (ERD diagrams)
- [GitHub](https://github.com/) (Version control)
- [Codeanywhere](https://codeanywhere.com) (IDE)
- [Heroku](https://heroku.com/) (Site hosting)
- [Cloudinary](https://cloudinary.com/) (Serving static media files)

## Libraries

- [Gunicorn](https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/gunicorn/) (Python HTTP server for WSGI applications)
- [pyscopg2](https://pypi.org/project/psycopg2/) (PostgreSQL Database adapter)
- [django-allauth](https://django-allauth.readthedocs.io/en/latest/) (User authentication)
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) (Control rendering behaviour of Django forms)

### Database

- [ElephantSQL](https://www.elephantsql.com/) (PostgreSQL database hosting)

# Deployment

#### Install libraries

Below are the libraries needed for deployment on Heroku.  For full explanation on how to install these libraries, refer to the links provided in [Technologies](#technologies).

- Install **Gunicorn** (server used to run Django on Heroku): ``pip3 install django gunicorn``
- Install **pyscopg2** (connects to PostgreSQL): ``pip 3 install dj_database_url pyscopg2``
- Install **Cloudinary** (host static files and images): ``pip3 install dj3-cloudinary-storage``

#### Create the Heroku App

- Log into Heroku and go to the Dashboard
- Click **New** and select **Create new app** from the drop-down
- Name app appropriately and choose relevant region, then click **Create App**

#### Create PostgreSQL database using ElephantSQL

This is necessary to create a database that can be accessed by Heroku. as it's not possible to access the database provided by Django by the deployed Heroku app.

- Log into ElephantSQL and go to Dashboard
- Click **Create New Instance**
- Set up a plan by providing a Name (project name) and select a Plan (for this project the free plan "Tiny Turtle" was chosen). Tags are optional.
- Click **Select Region** and choose appropriate Data center
- Click **Review**, check all details and click **Create Instance**
- Return to Dashboard on click on the name of the newly created instance
- Copy the database URL from the details section

#### Hide sensitive data

- Create ``env.py`` file and ensure it is included in the ``.gitignore`` file
- Add ``import os`` to env.py file and set environment variable **DATABASE_URL** to the URL copied from ElephantSQL (``os.environ["DATABASE_URL"]="<copiedURL>"``)
- Below, set **SECRET_KEY** variable (``os.environ["SECRET_KEY"]="mysecretkey"``, but be more inventive about the key string!)

#### Update Settings

- Add the following code at the top of ``settings.py`` to connect Django project to env.py:

    ````
      import os
      import dj_database_url
      if os.path.isfile('env.py'):
          import env
    ````

- Remove insecure secret key provide by Django in settings.py and refer to variable in env.py instead (``SECRET_KEY = os.environ.get('SECRET_KEY')``)

- To connect to new database, replace provided **DATABASE** variable with

    ````
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
    ````

- Save and migrate all changes made

#### Connect Heroku to Database

- In Heroku dashboard, go to **Settings** tab
- Add three new config vars **DATABASE_URL** (value is database URL), **SECRET_KEY** (value is secret key string) and **PORT** (value "8000")

#### Connect to Cloudinary

- In Cloudinary dashboard, copy **API Environment variable**
- In ``env.py`` file, add new variable ``os.environ["CLOUDINARY_URL"] = "<copied_variable"`` and remove ``CLOUDINARY_URL=`` from the variable string
- Add same variable value as new Heroku config var named **CLOUDINARY_URL**
- In ``settings.py``, in ``INSTALLED_APPS`` list, above ``django.contrib.staticfiles`` add ``cloudinary_storage``, below add ``cloudinary``
- To define Cloudinary as static file storage add the following to settings.py

    ````
    STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'

    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    ````

#### Set hosts

- In ``settings.py`` add

    ````
    ALLOWED_HOSTS = ['app-name.herokuapp.com', 'localhost']
    ````

# Credits

# Aknowledgement
