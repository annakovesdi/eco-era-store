Testing
Validation
I put the code through various validators. The HTML in W3C. I fixed all the red ones, but let the yellow warnings for sections without heading in these particular cases exist.

Html Validation

Html Validation

Html Validation

Html Validation

Html Validation

Html Validation

Html Validation

Html Validation

Html Validation

Html Validation

Html Validation

The CSS validator of w3c CSS validator found 2 errors that I did not fix since they are relevant. They give the buttons on the profile of a user shadow when hovered over.

CSS Validation

Visitor stories testing
As a new visitor, I want to easily find my way to a recipe.
When arriving on the site, immediately 3 recipes are displayed. they are aggregated from the database, which means they keep changing after a refresh. When clicking on the plus button of a recipe, you can see this recipe entirely.

As a new visitor, I want to be able to search in the recipe for a dish, a country, or an ingredient.
By clicking on the button recipes, the user can find the search field. The search field is an index of most words in the database in the keys recipe name, description, country, and ingredients. Under the search field, all recipes are displayed on default. When a search query has been made and the search has results, the results are displayed under the search box. If a search has no results a flashed message appears, explaining that the search has no results, and all recipes are displayed under the search field.

As a new visitor, I want to sign up.
By clicking the sign-up button, a form appears requesting first name, username, email address, and password. If all fields are validated green the user is signed up and logged in. They get redirected to their profile page, see a flash message welcoming them, and can use this username and password combination to log in next time they visit the site.

As a returning visitor, I would like to log in.
When a user is signed up and still can remember their username and password they can log in by filling in the form under the log-in button. They get redirected to their profile page and see a flash message that they have been logged in.

As a user, I would like to see my profile and my added recipes.
On the profile page, the user can see their first name, three editing buttons concerning their profile and all their added redipes.

As a user, i would like to edit my profile information and/or my password.
On the profile page the user can edit their email address or first name, edit their password or delete their profile. If the profile is deleted also all recipes of this user are deleted.

As a user, I would like to add a recipe.
After signing up, or logging in a button add-recipe is visible. By clicking the button the user is taken to a form. If all fields that are required are filled in the recipe is added to the database. A flash message announces the succesful edition of the recipe, the user is redirected to all recipes.

As a user, i would like to edit or delete my recipe.
If a recipe is created by a user, this user can see on this recipe's individual page an edit and delete button. If the user clicks edit, the add recipe form is displayed with all the content displayed so the user can edit where necessary. It is possible to cancel the edit, if the recipe was edited a flash message confirms the edit. The user gets redirected to the edited recipe. When clicking delete a modal pops up, asking if you are sure to delete the recipe? If so, a flash message is displayed confirming the recipe was deleted. The user gets redirected to all recipes.

As a user, I would like to delete my profile and all my recipes.
If the user clicks on the delete button on the profile a modal pops up, asking if you are sure to delete your profile? If so, all recipes of the user will be deleted as well. When clicked yes, a flash message is displayed confirming the profile was deleted. The user gets logged out en redirected to the sign-up page.

As a true enthausiast, I would like the site to create a country-themed week menu for me.
By clicking the week menu shuffle, the user sees a form with all countries of the world in a dropdown. If a country is selected, seven aggregated recipes of that country display on the screen for the user.

As a user, I want to log out
When a user is logged in, a log-out button is always visible. If clicked, a user logs out.

Manual (logical) testing of all elements, functionality
Step by step, I will guide you through the pages, and describe bugs that I fixed and the functionality of the finished site.

Index
with three aggregated recipes from the database and a link to the week-menu-shuffle feature

Index

The index page shows three recipes that should change after every refresh. By hitting the refresh button on the browser, this functionality is visible. I learned the method for this from tutor Tim, it was easy to implement, and started functioning right away.

Week Menu Shuffle
where a dropdown with flags of all countries of the world lets the user select a country of choice, and then aggregates seven recipes from that country from the database (if that many recipes are available- for the moment only Italy has seven recipes in the db)

week menu shuffle week menu

If you select a country, the site will display 7 recipes from that country. this was a hard one to wrap my head around. It was difficult to see which part of the function should go in the "Week_menu" app route, and which part in the "week_menu_suffle". It created extra chaos that I did not explain myself clear enough to a tutor and we arrived at a miscommunication avalanche about how this should be possible. My first instinct, that the week menu should take a parameter (country), was right in the end. I needed to match the country to the country in recipes, and then take a sample from these recipes. The issue was that that does not work if you do it one after the other (what beginners like me often try to do) It only works out if it's all done at the same time, because you cannot use aggregate on a list, or cursor object, or dictionary, created with a variable. Because to select a country, a dropdown is used, it is quite foolproof: the flag that is selected is dominant. It is impossible not to select a flag - so even if one types nothing, or something nonsensical, the country of the flag is displaying on the next page.

Recipes
with all recipes displayed of the db, and a search field where the user can search in the database in recipe name, ingredients, description, and country

Recipes

The recipes page simply displays all recipes from the database. The search function consists of an Index of the recipe name, ingredients, description, and country. A little difficulty was to get the search field to give a flash message if no recipes were found - I wanted to solve this in the app.py. I did find a way to do this, but I am repeating myself: I know this is NOT right:

Search

I asked my mentor during our last session, but his advice to just get rid of the else: statement completely (only displaying the if: statement) left the search empty if there were matches. I really did not have time to contact a tutor or deep dive in Stack Overflow about this. I did already do a search and various versions of this code, but for now, this was the only way it was working. I realize this is not the way it is supposed to be, so I recognize this as a bug that needs to be fixed at a later point. If the search field is left empty or something nonsensical is typed, the search just returns without results: a flash message is displayed that the search had no results and all recipes are visible.

Recipe
where a recipe is readable in its entirety. If the user is the creator of the recipe, it is also possible to edit or delete it

Recipe

The singular recipe page displays all the information on all the recipes. To get the ingredients displayed as a list, I made all individual recipe fields on the add-recipe form. All fields had the same name attribute "ingredients" so I could use the getlist() method and create an array in the database. This array is then displayed if you click on ingredients: all ingredients are listed under each other, neatly. The edit and delete button are only visible the user who created the recipe (and is stored in the key "created_by"). If Edit recipe is clicked, the add recipe form is displayed with all database information of this recipe filled out in the fields. The user can edit this, and click Edit Recipe or Cancel. The fields have validation in the form of a pattern value in the html. Not all fields are required. As long as the pattern value is kept and the field can validate good, it is possible to fill in nonsensical stuff and even only spaces. This is something I come back to under defensive strategies.

Sign Up and Log In
where the user can sign up providing a first name, username, password, and email address and log in

Sign Up

To sign up the user needs to provide four fields worth of information. Here spaces are not allowed, and the input is validated through a pattern attribute. The email address needs to contain an @ symbol and a dot. The information is stored in a collection of users in the database. The safety of the password is protected by werkzeug, which lets python generate a password hash so the actual password is not visible in the database. When logging in, the password hash gets checked against the provided password by the user by werkzeug. Like this the password of the user is secure. The log-in page checks the username and password provided by the user against the users in the database. If a username does not exist or the password does not match, a flash message displays informing the user the username and/or password are incorrect. No additional information is given for security reasons. If the log-in details are correct, the user is logged in by a session cookie and redirected to their profile page.

Log Out
when clicked a logged in user logs out

Log Out

The session cookie is removed and the user is thus logged out. A flash message communicates this with the user while redirecting them to the log-in page. When the user is logged out, some pages are not accessible. They just don't display on the screen (for example in the navigation). It is not possible to view a profile page, add a recipe or log out while logged out. It is not possible to log in or sign up while logged in. If a user is logged out and tries to access a page where a user is supposed to be logged in (add recipe, edit recipe for example) the user is redirected to log in.

Profile
where the logged in user can see their recipes and edit their name, password, email address or delete the profile and all their recipes

Profile

The profile page of the user displays their recipes from the database and has editing functionality.

editing the profile allows the user to edit their first name and email address. The username can not be changed for consistency. It is possible to cancel the edit.
editing the password generates a new password hash in the database. It is possible to cancel the edit.
deleting the profile not only deletes the user, but also all the recipes created by this user. This is pretty and just for the privacy of a user. A modal warns the user of the consequences of deleting, and yes has to be chosen to continue. It is possible to cancel the delete in the modal. Here I ran into a funny little bug, when I did not remove the session cookie after deleting the user. This meant that the user was still logged in, with all functionality, without a username or profile. This got fixed by removing the session cookie. Another bug I ran into is that if I wanted to update some fields, but not all, in the db I had to use a different method. So if the fields that i didn't provide information to should not be overwritten I had to use a different notation as explained here https://stackoverflow.com/questions/10290621/how-do-i-partially-update-an-object-in-mongodb-so-the-new-object-will-overlay.
Add recipe
where the user can add a recipe to the database

Add Recipe

The picture is of the edit recipe page, this is the same form as the add recipe page just filled in with data from the database. It is only possible to add a recipe if the user is logged in. The add recipe functionality lets the user add a recipe to the database providing all the details. To be able to leave the user free in their way to add a recipe, this is the least secure feature of the site. Spaces are allowed, and thus only spaces are also possible as a recipe name or an ingredient. The fields are being validated, but quite weakly. See defensive strategies, the next heading. the image for the recipe, for now, is a url, provided by the user: this is quite user unfriendly. Adding images was out of the scope for this Milestone Project. To create a link for the recipe to display the singular page i used the term "url" in the db - my mentor pointed out that this was quite unclear and the industry uses "slug" instead. Changing this created quite alot of reviewing because it needed to be changed everywhere of course for proper functionality. I called this one endearingly The Slug Bug.

Defensive strategies
Starting to dive into defensive strategies makes me realize how weak this site is. Unwanted data (for example empty data) can be added to the database in the add or edit recipe functionality, and even when the validation is turned on in the front end, like on the sign-up form, my mentor demonstrated how easily this can be deleted on the users end en thus it is almost as if it does not exist. The most basic users will not notice this, but the first person with some basic knowledge can go around this type of basic protection. The forms and the functionality need to be protected from the back end, in the python file. This way it is less easy to post unwanted data to the database. I started to look up how this can be done, but in the time frame provided this was not possible for me to accomplish - it is a learning goal for the near future though. I can imagine also the profile of the user, and their email address could be protected more thoroughly. I feel all information is just "out there" for a tech-savvy person to grab. If I would like to make a social recipe site like mentioned in functionality to be added, it would be quite impossible to protect the private data of users this way. Defensive strategies and security are themes that are touched upon in the most basic of ways, but completely insufficient for the real protection of privacy-sensitive data on this site.

Testing across browsers and devices
I did simulator tests throughout devices with chrome dev tools. I made sure the site looks okay on mobile devices, laptops and ipads. I asked (facebook)friends and family to check out the site and let me know what browser and device they used, and if they ran into any bugs. No bugs were reported, and lots of different devices were used.

iphone, samsung, huawei, xiaomi windows pc, macbook, imac, asus laptop safari, firefox, chrome, edge I ran the site through lambdatest to check it across browsers. Besides the large gap visible on all pages in Firefox that i did not have time to fix yet, there were no other discrepancies. I think the gap has to do with the space the flash messages take up, but i could not find out how to fix this and the deadline was breathing down my neck. I would like to come back to this later. The lambda tests look like this (for exaple, there were too many boring same looking screenshots to display here. On the one I chose, the blank field on Firefox browsers is visible)