# ValidationGuide

## Table of Contents


- [ValidationGuide](#validationguide)
  - [Table of Contents](#table-of-contents)
- [HTML W3C validator](#html-w3c-validator)
  - [Home](#home)
  - [Base](#base)
  - [Register](#register)
  - [Login](#login)
  - [Add article](#add-article)
  - [Update article](#update-article)
  - [Add topic](#add-topic)
  - [Article](#article)
  - [404](#404)
- [CSS Jigsaw](#css-jigsaw)
- [JavaScript JSHint](#javascript-jshint)
- [Python CI Python Linter](#python-ci-python-linter)
  - [Article](#article-1)
    - [views](#views)
    - [forms](#forms)
    - [models](#models)
  - [Account](#account)
    - [views](#views-1)
- [Accessibility axe DevTools Chrome Extension](#accessibility-axe-devtools-chrome-extension)
- [Performance, Accessibility, SEO, Best Practices (Lighthouse Chrome DevTools)](#performance-accessibility-seo-best-practices-lighthouse-chrome-devtools)
- [Browser Testing](#browser-testing)
 




# HTML [W3C validator](https://validator.w3.org/)
  ## Home
  ## Base
  ## Register
  ## Login
  ## Add article
  ## Update article
  ## Add topic
  ## Article
  ## 404

# CSS [Jigsaw](https://jigsaw.w3.org/css-validator/)
The validation result for the style.css comes with no errors. 
![jigsaw result](https://res.cloudinary.com/nazek/image/upload/v1690722405/readme/style-result.png).

# JavaScript [JSHint](https://jshint.com/)
1 undefined variable: bootstrap.
Referring to line 16 in base.html ``let alert = new bootstrap.Alert(messages);``

![jshint result](https://res.cloudinary.com/nazek/image/upload/v1690722422/readme/js-script-result.png)

# Python [CI Python Linter](https://pep8ci.herokuapp.com/)
## Article
  ### views
  ### forms
  ### models
## Account
  ### views

# Accessibility [axe DevTools Chrome Extension](https://chrome.google.com/webstore/detail/axe-devtools-web-accessib/lhdoppojpmngadmnindnejefpokejbdd)

# Performance, Accessibility, SEO, Best Practices (Lighthouse Chrome DevTools)

# Browser Testing

**Layout:** Testing layout and appearance of site for consistency throughout browsers.

**Functionality:**

- Testing complete functionality of the site. This includes:
  - Register
  - Login
  - logout
  - Navigation
  - Add Article / Update Article / Delete Article
  - Add Topic / Delete Topic
  - Comment
  - Bookmark
  - like

- Ensuring all links, navigation and form submit functions as expected throughout browsers.

| Browser     | Layout      | Functionality |
| :---------: | :----------:| :-----------: |
| Chrome      | ✔          | ✔             |
| Edge        | ✔          | ✔             |
