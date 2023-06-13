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

- [Bootstrap 5](https://getbootstrap.com/) - Used inorder to make the website responsive.

# Deployment

# Credits

# Aknowledgement
