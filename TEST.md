# TestGuide

## Table of Contents

- [TestGuide](#testguide)
  - [Table of Contents](#table-of-contents)
  - [Navigation](#navigation)
  - [CRUD](#crud)
    - [Create](#create)
    - [Read](#read)
    - [Update](#update)
    - [Delete](#delete)
  - [Filter](#filter)
  - [Register](#register)
  - [Login](#login)
  - [Logout](#logout)
  - [Like](#like)
  - [Comment](#comment)
  - [Bookmark](#bookmark)
  - [Social links](#social-links)


## Navigation
Navigation links are found either in the navbar for the big screen sizes or in a drop-down icon for the medium small screen sizes.

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **‘Home’ icon** | Click on icon. | User is redirected to Home page  |
| **‘Register’ link** | Click on Register link  | User is redirected to Register form page  |
| **‘Login’ link** | While not authenticated, Click on "Login". | User is directed to Login form. |
| **‘Logout’ link** | While authenticated, click on "Logout". | User is directed to Home page. |
| **‘Add article’ link** | While authenticated, click on "Add article" link. | User is redirected to Add article form |
| **‘Add topic’ link** | While authenticated, click "Add topic". | User is redirected to Add topic form. |
| **‘Topics’ drop-down list** | While authenticated, click "Topics" drop-down list. | All topics are listed. |


## CRUD
CRUD functionalities can only be granted by authenticated users in two different levels of access, meaning only the Moderator can create,
update and delete articles, and the login users can comment and like articles. 

### Create
The Moderator can create and submit an article 

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Title field** | Select field ‘title’ and start typing . | Title is displayed. Typing is disabled after 100 characters. |
| **Topic drop-down** | Click on field, select a topic name from the drop-down list . | Selected topic is displayed . |
| **Body field** | Click on ‘body’ field, and start typing, use the rich-text feature while typing. | Body is displayed. |
| **Submit** | Click on submit. | User is redirected to the ‘Home’ page, and the article is displayed there. |
| **Incomplete form** | Fields left empty. | Submit button will not function. |

### Read 
Authentication is not required to be able to read an article. 

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Article title** | Click on title. | Article will be displayed in a separate page. |

### Update 
The Moderator can edit and update articles. 

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Edit button** | Click on edit button. | Article body will be displayed in edit mode.  |
| **submit** | After altering form fields. Click on submit button. | New changes are saved to article table. |
| **Incomplete form** | Click on submit where a field at least is empty. | Warning msg will be displayed, and the form will not be submitted. |


### Delete 
The Moderator can select and delete articles. 

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Delete button** | Click on the delete button of a specific article. | Alert message will be displayed to confirm deletion.  |
| **confirm** | Click on confirm button on delete dialog box. |  Article will be deleted and removed from database table. |
| **cancel** | Click on cancel button on delete dialog box. | Deletion will not be executed and alert message dialog box will be closed. |


## Filter
Articles will be displayed according to the selected topic. 
| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Topic dropdown button** | Click on Topic drop-down, then select a topic. | page render all articles under the same topic.  |

## Search

Articles will be displayed according to the search criteria (Author, title, topic).
| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Search button** | Type in the search area author name or article title/topic, then click on search button. | page render all articles relate to the search criteria.  |

## Register 
User creates an account

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Register form ** | On navbar, click on the register button. | Register Form will be displayed, all fields should be filled.  |
| **Incomplete form** | Click on submit where a field at least is not filled properly. |  Alert messages will be displayed beside each incomplete field. |
| **submit** | Click on the submit button after filling in the form properly. | A new account is created a user is redirected to the login page. |


## Login
A user who has already an account will no longer see ‘Register’ link on the navbar, but ‘Login’ instead 

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Login form** | On navbar, click on login link. | login Form will be displayed, all fields should be filled.  |
| **Incomplete form / wrong inputs** | Click on submit where a field at least is not filled properly. |  Alert messages will be displayed beside each incomplete field or wrong input. |
| **submit** | Click on the submit button after filling in the form properly. | user is redirected to the home page with authenticated privileges. |



## Logout 
Only authenticated user can logout 

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Logout link** | On navbar, click on logout link. | User is redirect to the home page. |


## Like  
Authenticated users only can leave comments articles.

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Like icon** | Below the article, click on like.  | the number of likes is increased 1, and the icon turns to filled thumb-up.  |
| **Unlike** | Click on the submit button after filling in the form properly. | the number of likes is decreased 1, and the icon turns to empty thumb-up  |


## Comment 
Authenticated users only can like articles 

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Comment icon** | Below the article, click on comment icon, a dialog box is displayed to write a comment inside.  | Alert messages will be displayed beside each incomplete field or wrong input.  |
| **Unlike** | After filling in the comment, click on submit. | Comment is displayed below the article. |


## Bookmark 
Authenticated users can bookmark articles, so it’s saved for next visits. 
| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Bookmark icon** | Below the article, click on save icon.  | article will be listed in your profile, and the icon turns to filled bookmark.  |
| **disable icon** | click on filled-save icon | and the icon turns to empty bookmark  |

