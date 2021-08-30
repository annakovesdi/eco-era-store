<h1>Eco Era Store</h1>

**Webshop for handmade ecological baby/mama products. The website allows you to get to know the products, the philosophy, the policy on a simple and no-nonsense easily viewable site. Checkout for bought items is handled by stripe, static files storage by AWS, and deployment/Postgres database through Heroku.**

<h2>UX</h2>
The ideal visitor is a parent and/or menstruating person, is interested in zero-waste and ecological solutions for common day-to-day hygiene routines regarding these subjects, wants to support small businesses, loves handmade goods, and would like to shop online.

Visitors are likely coming from Instagram, are interested to see prices and 'taste the atmosphere'. 

<h3>Visitor stories</h3>

*As a new visitor* 

1. I want to easily find the product I am looking for
2. I want to put products I like as fast as possible in my bag
3. I want to delete items from my bag
4. I want to update the number of products in my bag
5. I want to have a clear menu to browse through the store
6. I can find information about the products
7. I can find how to use the products
8. I want to sign up
9. I want to check out without signing up
10. I want to pay with creditcard or ideal or bankcontact
11. I want to find information on the return policy and contact information

*As a returning visitor*

12. I would like to see my saved basket from the last time I visited
13. I would like to log in.
14. I would like to see my address and my order history
15. I would like to edit my profile information and/or my password
16. I would like to delete my profile and order history
17. I would like to log out

*As a superuser*

18. I would like to add a product and add a category to it
19. I would like to edit or delete products
20. I would like to update the descriptions of products and categories 
21. I only want superusers to access this functionality

The website represents the style, logo, typography, and colors of the Eco Era brand. Buyers are familiar with the imagery and style already through the Instagram page and see this when they arrive on the home page for familiarity and branding. 

<h2>Wireframes</h2>
Main colors of the site: 
lightgreen: #E2E8E3
darkblue: #829CB0

![wireframe1](https://eco-era-store.s3.eu-central-1.amazonaws.com/media/wireframe1.jpg "wireframe 1")
![wireframe2](https://eco-era-store.s3.eu-central-1.amazonaws.com/media/wireframeTWO.jpg "wireframe 2")

<h2>Features</h2>

*Header/Footer* 

The header is featured on every page, consisting of several links and dropdown menus for easy and fast navigation. The accounts dropdown allows the user to navigate login/profile page functionality while the various links take you to categories (and their products), all products, or information on the shop. There is a shopping cart (displaying the grand total) visible at all times in the header.
The footer has a copyright notice, contact information, and Instagram and Facebook links.  

*Index page* 

The home page features an advertisement video of Eco Era that auto plays and loops, muted. The logo is displayed, big and in the center, with a shop now button (taking you to an all  products page). Under the video you see a peekaboo announcing Eco Era on socials - when scrolled the Instagram entries of Eco Era Shop are displayed through Juicy. 
The home page has a navigation bar and footer. 

*Products*

All products displays all products (so all categories). Depending on screen size 1 up until 4 products are displayed in a row. They all have an add-to-bag button that adds one item to the shoppingbag. 
When the see more button is clicked, products all have an individual page where more information is displayed - their description, picture(s), category, price, and eventual combination discounts. Here the quantity is selectable before adding to the bag. 

*Categories*

Every category has a link in the nav-bar and its own page - with the description of the category as the first section. All products can be added to a category. There are 15 categories, all their descriptions are editable by a superuser.

*Profile*

Every user can create a profile, where data on the user is stored, like address and order history. The user can sign up, view their profile, edit their profile, and log in and out.

*Superuser*

A superuser can add, edit and delete all products in the webshop - They can change their names, categories, prices, images, and descriptions. 
They can edit the description of categories aswel. 

*Shopping bag*

The shopping bag features all products (if there are any) with a picture, name, price, changeable quantity, subtotal, and delete button. Also, the delivery costs and grand total are displayed, and the free delivery threshold - if it's not reached yet. 

*Checkout*

The checkout page features a form, with delivery and billing information to fill in. If a user is logged in and chose to save this information, it is automatically displayed. Checkout is handled by Stripe, after successful payment the completed order is displayed with an assigned order number. 

*Toasts*

All actions that a user takes are communicated through toasts. For example, if a user successfully creates a profile/adds a product to the bag etc, a success message is displayed. If a superuser starts editing a product, an information toast of the edit appears. If a user fails to pay due to a mistake in the form, an error message communicates this. 

Features to implement in the future:
Oh so many, so many. Some of these things I already started building, since this will be a real website one day, for this very real company Eco Era Store. The features were not yet finished though before my deadline and too buggy to leave on the site. If the site is looked at with careful eyes, they are still in past commits and will also come back after assessment, hopefully finding good solutions for the issues. 

tracking cookies alert
more images for a single product
discount if you buy certain items at the same time 
product ratings
product comments
ideal payment
bancontact payment
social accounts sign in

I would like to tweak the design for the mobile page a bit. It's fine for now but I feel it could look a little more appealing, the desktop site is somewhat better than the mobile one and most users will probably see the site first on their phone (because of the customers arriving through Instagram).

<h2>Technologies used</h2>
Gitpod to develop the website
GitHub for version control and code hosting
Heroku for deployment
AWS S3 Bucket as static files database
Heroku Postgres as database
Google fonts for the fonts

Html, Css, JavaScript and Python are the developing languages

Frameworks: Django as the main framework for the site, Bootstrap for CSS, JQery for JavaScript

Libraries and packages used: boto3, coverage, dj-database-url, django-allauth, django-countries, django-crispy-forms, django-storages, gunicorn, jmespath, oauthlib, Pillow, psycopg2-binary, stripe

Balsamiq for the wireframes
lambdatest.com for static testing
Chrome dev tools for manual testing

<h2>Testing</h2>
Testing information can be found in the TESTING.md file

<h2>Deployment</h2>
The site is deployed through Heroku, with staticfiles stored in Amazon Web Services and code version control and storage in GitHub.

Steps to setup deployment:

Create a new Heroku app. 

In the settings of the Heroku app in the browser Config vars are added. Here you add the SECRET_KEY, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, DATABASE_URL, STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY, STRIPE_WEBHOOK_SECRET and USE_AWS configuration variables. 

The SECRET_KEY is the Django secret key variable. 
AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY are provided in your Amazon Web Services dashboard, where the static files are stored for this site. 
DATABASE_URL is the Postgres url of your Heroku Postgres database. 
STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY and STRIPE_WEBHOOK_SECRET are provided in the Stripe for developers area in your Stripe profile. 
EMAIL_HOST_PASS and EMAIL_HOST_USER are set for the automatic email settings: the email address and passcode to let Django use it, set in the mail service. 
USE_AWS is set to true (USE_AWS=True) in the Heroku environment to make sure the deployed version uses AWS for static files. 

To set up your AWS S3 Bucket, you need to create one en configure it first. Read up about this process here, if you want to use AWS aswel: https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html

Before deploying to Heroku a Procfile is necessary, there is one in the project. Heroku apps include a Procfile that specifies the commands that are executed by the app on startup. You can use a Procfile to declare a variety of process types, including your app’s web server, multiple types of worker processes, a singleton process, such as a clock or tasks to run before a new release is deployed Each dyno in your app belongs to one of the declared process types, and it executes the startup command associated with that process type. The Procfile is always a simple text file that is named Procfile without a file extension. Also, a requirements.txt file is included. When forking the GitHub be sure to install everything from the requirements.txt file before deploying(just run $ pip3 install -r requirements.txt in your terminal). If you install new packages make sure to freeze them into the requirements.txt (pip3 freeze > requirements.txt)

Under the deploy tab of the Heroku app in the browser it is possible to connect a GitHub Repository to the Heroku app, and automatically deploy from the main branch. In this case, every push to main will deploy a new version of this app. Deploys happen automatically: be sure that this branch in GitHub is always in a deployable state and any tests have passed before you push.

Be sure to create a .gitignore file that hides sensitive information from deployment. Always check with $ git status that your sensitive files are not pushed to GitHub and Heroku. A gitignore file specifies intentionally untracked files that Git should ignore.

This site is now live at https://eco-era-store.herokuapp.com/

<h2>Credits</h2>
Most of the credits this learning season go to Code Institute. By reviewing the mini-projects and Boutique Ado Project I created a lot of this site. Without the tutorials and step-by-step guides, this project would be exactly nowhere. 

Of course, there were lots of other helpers too. They are listed here in no particular order.

- Read the book "A smarter way to learn Python" by Mark Myers
- Documentation Django
- Documentation Bootstrap
- Documentation Heroku
- Documentation AWS
- Documentation Stripe
- Markdown cheat sheet
- Mentoring help with final deployment issues
- Tutors helping along the way. Most times i solved the issues myself after being helped on the way by a tutor. Tutor help was contacted lots of times throughout my project. 
- And of course reading through thousands of Stackoverflow questions and explanations helped me understand what i was trying to do. If I copied the code, the link is above it in the project. It did not happen a lot though - the project is too specific to be able to use others code, it was more a learning opportunity of concepts and theory. 

It was quite an extensive project that I needed to finish in a really short time, and being new and fresh to Django I got done what I could in the time I had. I want to continue on this site end build it up to a fully functional, beautiful Django app, that it has the potential to become. 

*Pictures, text, and products*
Eco Era Store 
Text, Images, and Concept all copyright of Eco Era Store 
Promo video by Anna Kovesdi, intellectual property of Eco Era Store
Eveline Snoeij
KVK:77336542
BTW Number: NL003188712B85