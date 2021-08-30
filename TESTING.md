<h1>Testing</h1>

<h2>Validation</h2>

I put the code through various validators, namely:
HTML W3 https://validator.w3.org/
CSS W3 https://jigsaw.w3.org/css-validator/
JS Beautifytools https://beautifytools.com/javascript-validator.php
Python ExtendsClass https://extendsclass.com/python-tester.html
I only describe errors here (because of the extensive nature of the project), when I fixed them and if not, why not. 
The validations are categorized by app.

<h3>Checkout App</h3>

*Html Validation*
pass

*CSS Validation*
pass

*JS Validation*
2 missing semicolons

*Python validator*
forms.py syntax error:
    label = f'{labels[field]}*'
I tied to find the proper syntax but was unsuccessful. Also the boutique ado project has this syntax.
I found more fstring errors in this validator, maybe the validator does not like fstrings.

<h3>Eco Era Store App</h3>

*Python validator*
pass

<h3>Home App</h3>

*Html Validation*
1. Error: Bad value button for attribute type on element a: Subtype missing l.18
Remove type=button from an element. 
1. Error: Element a is missing required attribute href. l.18
add href="#" to a element
1. Error: Attribute ?muted/?controls/?loop not allowed on element iframe at this point. l.65
Leaving these, because the element muted allows iframe to autoplay and controls/loop
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

1. I want to easily find the product I am looking for

On the home page, an extensive menu is visible, easily navigatable to the category of products a user is searching for. There is also an all products button in case the user has no idea which category to search. 

2. I want to put products I like as fast as possible in my bag

On The products page, there is a fast add button for every product

3. I want to delete items from my bag

The shopping bag items are deletable with the delete button

3. I want to update the number of products in my bag

The shopping bag is updatable with the update button

3. I want to have a clear menu to browse through the store

A clean menu is provided with various dropdowns on category items that are connected, for example, my account. The menu is fully responsive and visible on every page

4. I can find information about the products

All products have a page with a clear description, pictures and price

5. I can find how to use the products

There is a separate how to use the products page on the site, but often the way to use washable products is also described in the description

6. I want to sign up

Under the my account heading a user can easily sign up

7. I want to check out without signing up

It's possible to check out without registering to the site. The checkout form needs to be filled in completely.

8. I want to pay with a creditcard or ideal or bancontact

For now, only payments with a creditcard are integrated, with ideal and bancontact implemented in the future

9. I want to find information on the return policy and contact information

There is an information heading in the menu providing users with the privacy policy, information, contact possibilities, etc. 

*As a returning visitor*

8. I would like to see my saved basket from the last time I visited

The basket of a visitor is saved as a cookie and thus will reappear on the next visit

8. I would like to log in.

If a user signs up they can easily log in to the account menu

9. I would like to see/change my address and my order history

This is possible when a user creates a profile, on their profile page

10. I would like to edit my profile information and/or my password

It's already possible to edit basic profile information and your password.

11. I would like to delete my profile and order history

This is not possible yet, and not legal for the dutch AVG rules. This needs to be implemented in the near future. Also automatically deleting all order history after a set amount of time is important to implement. 

12. I would like to log out

This is possible from the main navigation on every page

*As a superuser*

13. I would like to add a product and add a category to it

In the Product Management form, a superuser can add products

13. I would like to edit or delete products

In the Product Management form, a superuser can edit/delete products

14. I would like to update the descriptions of products and categories 

In the Product Management form, a superuser can edit/delete descriptions of products and categories

15. I only want superusers to access this functionality

The product management page is protected in various ways through the back end, see defensive strategies.

16. I would like to put a product on Sold Out, so it stays in the shop but is not addable to the basket

This is possible for now, but this functionality is not yet fortified in the backend

<h2>Manual (logical) testing of all elements, functionality</h2>

Step by step, I will guide you through the pages, and describe bugs that I fixed and the functionality of the finished site.

<h3>Home</h3>

The home page displays the navigation menu, a hero video (an ad of Eco Era Store), and the Instagram feed of the shop. Instagram is very important for this shop, so displaying the feed on the home page will make people feel right at home, or get newbies to maybe follow the page after seeing a preview. The controls of Vimeo and the ads of Juicy will disappear for a paying customer.

![Home page screenshot](https://eco-era-store.s3.eu-central-1.amazonaws.com/media/home.png "Home Page Screenshot")

<h3>Products</h3>

The products are displayed in cards and are searchable under their category names in the nav-bar. They display their price and name at all times. On desktop, there are see more/add to bag buttons, for fast adding the product. On the mobile site, the picture is clickable to see more. 
There is an all products link in the navbar that shows all products on one page. The products all have a picture, name, price, category, and short+long descriptions. The page for a single item shows all this information. The model for the products already has more images, but they are not yet integrated into the html - so uploading more then one image does not make sense yet. There was just no time left to finish this, but the visibility of more than one image will come asap. 

![Category Wipes products screenshot](https://eco-era-store.s3.eu-central-1.amazonaws.com/media/category-wipes.png "Category Wipes products screenshot")

<h3>Sign Up, Log In and Log Out</h3>

All this is handled by Allauth - 
- Signup 
- E-mail address management (multiple e-mail addresses, setting a primary)
- Password forgotten flow
- E-mail address verification flow
Real email is working but is not reviewed yet for content, it's just functionality that's in place.
In the future, it is important to also integrate the social account functionality of Allauth for this project since most customers will come to the site from Instagram. But again, in the time frame provided I did not get the chance to tackle that. 

![Sign Up page screenshot](https://eco-era-store.s3.eu-central-1.amazonaws.com/media/sign-in.png "Sign Up page screenshot")

<h3>Profile</h3>

In the profile app it's possible to log in, view past orders, edit the delivery address and have the checkout form pre-filled when you want to buy something. 
bug - not all data is saved, full name does not show up on checkout form. Found it, no time to fix it. 

![Profile screenshot](https://eco-era-store.s3.eu-central-1.amazonaws.com/media/profile.png "Profile screenshot")

<h3>Product Management</h3>

If a user is a registered superuser, they have access to the product management page where they can edit category description and all products and their details. They can also delete products, or add new ones.
It is also possible to mark a product as sold out, so it's still visible in the shop but it is not possible to place the item in the bag.

![Product management screenshot](https://eco-era-store.s3.eu-central-1.amazonaws.com/media/product-management.png "Product management screenshot")

<h3>Defensive strategies</h3>

Login and password safety is handled by allauth. 
Payment safety is handled by Stripe.
When writing the code, it was always made sure to use the possibilities in Django to make sure a form is always validated and where login is required, the authentication decorators were used and before anything is edited, the view checks if a user is authenticated. 
The secret keys were never pushed to github and kept secret throughout production. Every defensive strategy learned was used. 

<h3>Testing across browsers and devices</h3>

I did simulator tests throughout devices with chrome dev tools. I made sure the site looks okay on mobile devices, laptops and ipads. I asked (facebook)friends and family to check out the site and let me know what browser and device they used, and if they ran into any bugs. Some minor css bugs were reported and fixed (like outlines that overlap etc), and lots of different devices were used.

I ran the site through lambdatest to check it across browsers. As well the virtual view in another browser as the screenshots of different pages in different browsers/devices, for example: iphone, samsung, huawei, xiaomi, windows pc, macbook, imac, asus laptop safari, firefox, chrome, edge.

Below an example of lambdatest screenshots:

![lambdatest screenshots](https://eco-era-store.s3.eu-central-1.amazonaws.com/media/Lambda.png "lambdatest screenshots")