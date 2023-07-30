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
    - [urls](#urls)
  - [Account](#account)
    - [views](#views-1)
  - [Magazine](#magazine)
    - [settings](#settings)
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
Referring to line 16 in article.js ``let alert = new bootstrap.Alert(messages);``

![jshint result](https://res.cloudinary.com/nazek/image/upload/v1690722422/readme/js-script-result.png)

# Python [CI Python Linter](https://pep8ci.herokuapp.com/)
python files have been verified with the above validator, below are some results for the three apps (Article, Account, Magazine). The rest of python files have similar results.
## Article
Below are the yielded  results given when validating the files (views.py, forms.py, models.py, urls.py).
  ### views
  ![python linter result](https://res.cloudinary.com/nazek/image/upload/v1690728469/readme/CI-Python-result-article-views.png)
  ### forms
  ![python linter result](https://res.cloudinary.com/nazek/image/upload/v1690728469/readme/CI-Python-result-article-forms.png)
  ### models
  ![python linter result](https://res.cloudinary.com/nazek/image/upload/v1690728469/readme/CI-Python-result-article-models.png)
  ### urls
  ![python linter result](https://res.cloudinary.com/nazek/image/upload/v1690728469/readme/CI-Python-result-article-urls.png)
## Account
Below is the yielded  results given when validating the file views.py.
  ### views
  ![python linter result](https://res.cloudinary.com/nazek/image/upload/v1690728469/readme/CI-Python-result-account-views.png)
## Magazine
Below is the yielded  result given when validating setting.py.
Notice: the same error (line too long) occurs at lines (111 , 142).
  ### settings
  ![python linter result](https://res.cloudinary.com/nazek/image/upload/v1690728469/readme/CI-Python-result-setting.png)

# Accessibility [axe DevTools Chrome Extension](https://chrome.google.com/webstore/detail/axe-devtools-web-accessib/lhdoppojpmngadmnindnejefpokejbdd)
8 issues found.
![Accessibility](https://res.cloudinary.com/nazek/image/upload/v1690741405/readme/Accessibility-test-result.png)
- Element must meet minimum color contrast ratio thresholds
- <html> element must have lang attribute.
    - Fix: added to 'html' element in the base.html, after applying this fix, the number of issues has dropped to 5 issues, all issues point to the same problem 
    (Element must meet minimum 
         color contrast ratio thresholds)
![Accessibility](https://res.cloudinary.com/nazek/image/upload/v1690742194/readme/Accessibility-second-test-result.png)

# Performance, Accessibility, SEO, Best Practices (Lighthouse Chrome DevTools)

- Desktop 

![Accessibility](https://res.cloudinary.com/nazek/image/upload/v1690742650/readme/performance.png)
- Mobile

![Accessibility](https://res.cloudinary.com/nazek/image/upload/v1690742787/readme/performance-mobile.png)

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

