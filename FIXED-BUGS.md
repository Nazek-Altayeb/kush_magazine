* Bug: search feature fail to retrieve articles according to author name.
  * fix: add 'username' in query.
* Bug : Empty page displayed when no articles found
  * fix: add condition in search template to display 'no articles found' if no articles exist.
* Bug : layout of the home page break in mobile devices
  * fix : add media queries for smaller screen width.
* Bug :  push failed in heruko
  * fix: update the  backports.zoneinfo in requirement.txt.
* Bug: comment is not saved
  * Fix: add condition to check if comment form is valid.
* Bug: Get wrong number of likes
  * Fix : move the likes accumulator statement outside the if clause in get_context_data method.
* Bugs: errors accours because of typo in views methods and some templates.
  * Fix: correct variables/fields names.
* Bugs: Get errors and warnings in templates.
  * fix: remove duplicated Ids used in multiple elements, remove un-used tags.
*  