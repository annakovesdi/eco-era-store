<h1>Testing</h1>

<h2>Validation</h2>

I put the code through various validators, namely:
HTML W3 https://validator.w3.org/
CSS W3 https://jigsaw.w3.org/css-validator/
JS Beautifytools https://beautifytools.com/javascript-validator.php
Python ExtendsClass https://extendsclass.com/python-tester.html
I only describe errors here (because of the extensive nature of the project), if i fixed them and if not, why not. 
The validations are categorised by app.

<h3>Checkout App</h3>

*Html Validation*
pass

*CSS Validation*
pass

*JS Validation*
2 missing semicolons

*Python validator*
forms.py synthax error:
    label = f'{labels[field]}*'
I tied to find the proper synthax but was unsuccesfull. Also the boutique ado project has this synthax.
I found more fstring errors in this validator, maybe the validator does not like fstrings.

<h3>Eco Era Store App</h3>

*Python validator*
pass

<h3>Home App</h3>

*Html Validation*
1. Error: Bad value button for attribute type on element a: Subtype missing l.18
Remove type=button from a element. 
1. Error: Element a is missing required attribute href. l.18
add href="#" to a element
1. Error: Attribute ?muted/?controls/?loop not allowed on element iframe at this point. l.65
Leaving these, because the element muted allows iframe to autoplay and controls/loop, controle
1. Error: The frameborder attribute on the iframe element is obsolete. Use CSS instead.
Removed
1. Error: Bad value 100% for attribute width on element iframe: Expected a digit but saw % instead/
Error: The frameborder attribute on the iframe element is obsolete. Use CSS instead
Left like this, code provided by Juicy.

*Python validator*
pass

<h3>Products App</h3>

*Html Validation*
pass

*CSS Validation*
pass

*Python validator*
pass

<h3>Profiles App</h3>

*Html Validation*
pass

*Python validator*
pass

<h3>Shoppingbag App</h3>

*Html Validation*
pass

*JS Validation*
2 missing semicolons

*Python validator*
pass

<h3>Static, templates</h3>

*Html Validation*
Error: stray div tag l.53

*CSS Validation*
Error: Title:hover transform from black to black not valid
Removed

<h2>User stories testing</h2>

*As a new visitor* 

1. I want to easily find the product i am looking for

On the home page an extensive menu is visible, easily navigatable to the category of products a user is searching. There is also an all products button in case the user has no idea which category to search. 

2. I want to put products i like as fast as possible in my bag

On The products page there is a fast add button for every product

3. I want to delete items from my bag

The shopping bag items are deleteble with the delete button

3. I want to update the amount of products in my bag

The shopping bag is updateble with the update button

3. I want to have a clear menu to browse through the store

A clean menu is provided with various dropdowns on category items that are connected, for example profile. The menu is fully responsive and visible on every page

4. I can find information about the products

All products have a page with a clear description, pictures and price

5. I can find how to use the products

There is a separate how to use the products page on the site, but often the way to use washable products is also described in the description

6. I want to sign up

Under the my account heading a user can easily sign up

7. I want to check out without signing up

Its possible to check out without registering to the site. The checkout form needs to be filled in completely.

8. I want to pay with creditcard or ideal or bancontact

For now only payments with creditcard are integrated, with ideal and bancontact implemented in the future

9. I want to find information on return policy and contact information

There is an information heading in the menu providing users with the privacy policy, information, contact possibilities etc. 

*As a returning visitor*

8. I would like to see my saved basket from the last time i visited

The basket of a visitor is saved as a cookie and thus wil reappear on the next visit

8. I would like to log in.

If a user signs up they can easily log in in the account menu

9. I would like to see / change my address and my order history

This is possible when a user creates a profile, on their profile page

10. I would like to edit my profile information and/or my password

It's already possible to edit basic profile information, password not yet. this is one of the things to add in upcoming features, when sending emails will be possible.

11. I would like to delete my profile and order history

This not possible yet, and not legal for the dutch AVG rules. This needs to be implemented in the near future. 

12. I would like to log out

This is possible from the main navigation on every page

*As a superuser*

13. I would like to add a product and add a category to it

In the Product Management form a superuser can add products

13. I would like to edit or delete products

In the Product Management form a superuser can edit/delete products

14. I would like to update the descriptions of products and categories 

In the Product Management form a superuser can edit/delete descriptions of products and catageories

15. I only want superusers to access this functionality

The product management page is protected on various ways through the back end

16. I would like to put a product on Sold Out, so it stays in the shop but is not addable to the basket

This is possible for now, but this functionality is not yet fortified in the backend

<h2>Manual (logical) testing of all elements, functionality</h2>

Step by step, I will guide you through the pages, and describe bugs that I fixed and the functionality of the finished site.

<h3>Home</h3>

The home page displays the navigation menu, a hero video (an ad of eco era store) and the instagram feed of the shop. Instagram is very important for this shop, so displaying the feed on the home page will make people feel right at home, or get newbies to maybe follow the page after seeing a preview. The controls of Vimeo and the ads of Juicy will disappear for a paying customer.

![Home page screenshot](https://eco-era-store.s3.eu-central-1.amazonaws.com/media/home.png "Home Page Screenshot")

<h3>Products</h3>

The products are displayed in cards and are searchable under their category names in the nav-bar. They display their price and name at all times. On desktop there are see more/add to bag buttons, for fast adding the product. On the mobile site the picture is clickable to see more. 
There is an all products link in the navbar that shows all products in one page. The products all have a picture, name, price, category and short+long descriptions. The page for a single item shows all this information. The model for the products already has more images, but they are not yet integrated in the html - so uploading more then one image does not make sense yet. There was just no time left to finish this, but visibility of more then one image wil come asap. 

![Category Wipes products screenshot](https://eco-era-store.s3.eu-central-1.amazonaws.com/media/category-wipes.png "Category Wipes products screenshot")

<h3>Sign Up, Log In an Log Out</h3>

All this is handled by Allauth - 
- Signup 
- E-mail address management (multiple e-mail addresses, setting a primary)
- Password forgotten flow
- E-mail address verification flow
To make everything work completely, sending mails through Django should be formatted. this is not yet the case because it should be done with the real email of eco era store.
In the future it is important to also integrate the social account functionality of Allauth for this project, since most customers will come to the site from instagram. But again, in the time frame provided i  did not get the chance to tackle that. 

![Sign Up page screenshot](https://eco-era-store.s3.eu-central-1.amazonaws.com/media/sign-in.png "Sign Up page screenshot")



Profile
bug - not all data is saved, full name does not show up on checkout form. 

Profile

The profile page of the user displays their recipes from the database and has editing functionality.


Product Management


Defensive strategies


Testing across browsers and devices
I did simulator tests throughout devices with chrome dev tools. I made sure the site looks okay on mobile devices, laptops and ipads. I asked (facebook)friends and family to check out the site and let me know what browser and device they used, and if they ran into any bugs. No bugs were reported, and lots of different devices were used.

iphone, samsung, huawei, xiaomi windows pc, macbook, imac, asus laptop safari, firefox, chrome, edge I ran the site through lambdatest to check it across browsers. Besides the large gap visible on all pages in Firefox that i did not have time to fix yet, there were no other discrepancies. I think the gap has to do with the space the flash messages take up, but i could not find out how to fix this and the deadline was breathing down my neck. I would like to come back to this later. The lambda tests look like this (for exaple, there were too many boring same looking screenshots to display here. On the one I chose, the blank field on Firefox browsers is visible)