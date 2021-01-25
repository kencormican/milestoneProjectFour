<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">


--------
<h1 align="left">Ken Cormican | Milestone Project Four</h1>


<h2 align="left">Full Stack Frameworks with Django</h2>



## Table of Contents

**<details><summary>Project Overview</summary>**
* [Demo](#demo)
* [Travis CI](#travis-ci)
* [Dummy account details](#placeholder-dummy-account-details)
* [Purpose](#purpose)
* [Project Brief](#project-brief)

</details>

**<details><summary>User Experience (UX)</summary>**

* [UX](#user-experience-(ux))
* [Requirements](#requirements)
* [User Stories](#user-stories)
* [Design](#design)
* [Scope](#scope)
* [Preparation](#preparation)
* [Colour Scheme](#colour-scheme)
* [Typography](#typography)
* [Imagery](#imagery)
* [Responsive Elements](#responsive-elements)
* [Interactive Elements](#interactive-elements)
* [Authentication](#authentications)
* [Wireframes](#wireframes)
</details>

**<details><summary>Database Structure (Django Models)</summary>**

* [Database Structure](#database-structure)
* [User Profile Model](#user-profile-model)
* [Main Category Model](#main-category-model)
* [Subcategory Model](#subcategory-model)
* [Product Model](#product-model)
* [Order Model](#order-model)
* [Order Line Items Model](#order-line-items-model)
* [Contact Model](#contact-model)
</details>

**<details><summary>Testing</summary>**

* [Testing](#testing)
* [Bugs Found](#bugs-found)
</details>

***


## Demo

[View the live project here.](https://kjc-off-piste-skishop.herokuapp.com/)


--------
## Travis CI
[![Build Status](https://travis-ci.com/kencormican/milestoneProjectFour.svg?branch=master)](https://travis-ci.com/kencormican/milestoneProjectFour)

--------
### Placeholder dummy account details
--------

## Purpose

Winter sports such as Skiing & Snowboarding have become increasingly popular within Ireland over the past two decades.   
With that in mind I've decided to make the sale of Ski and Snowboard related goods the focus of this ecommerce website.

In doing so I hope the provide a positive user experience that utilizes HTML, CSS, Bootstrap, Python, Django, Heroku, Postgres & Stripe and demonstrates the skills I've developed under the tutileage of the Code Insitute team while studying the Diploma in Full Stack Development.
Time permitting, in addition to the above I'm also hoping to capture some of the backend validation and redundancy described, in particular during the Webhooks tutorials.

***


[Back to Contents](#table-of-contents)

--------

<h2 align="center"><img src="assets/images/responsiveMockupMilestoneFour.jpg"></h2> 


## Project Brief

The brief was to create a full-stack site based around the business logic used to control a centrally-owned dataset.
The developer is tasked with providing an authentication mechanism and paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service.  
In creating the site, the developer should expose the learnings from the HTML, CSS, JavaScript, Python, Django & Relational Database Modules. 


1. Design, develop and implement a full stack web application, with a relational database, using the Django/Python full stack MVC framework and related contemporary technologies.
2. Design and implement a relational data model, application features and business logic to manage, query and manipulate relational data to meet given needs in a particular real-world domain.
3. Identify and apply authorisation, authentication and permission features in a full stack web application solution
4. Design, develop and integrate an e-commerce payment system in a cloud-hosted full stack web application
5. Document the development process through a git based version control system and deploy the full application to a cloud hosting platform.
6. Test the application through the development, implementation and deployment stages
7. Deploy a final version of the full-stack application code to a cloud-based hosting platform (e.g. Heroku) and test to ensure it matches the development version 
8. Demonstrate and document the development process through a version control system 

***


[Back to Contents](#table-of-contents)

--------

# User Experience (UX)

## Requirements

Use the Bootstrap and Django Frameworks, in conjunction with Postgres and the Stripe API to render a clean, robust fully functional ecommerce site.  
The Website should be responsive, allowing end users to purchase goods, register to the site and perform the full set of CRUD operations on their shopping baskets.
The end users should be able to view all products or search based on category, price or rating criteria.
In addition to the above, en users should be able to select individual products to view more detailed information.
Admin users should be able to display, add, edit or delete products or categories.
Site structure and purpose should be clear from the outset, providing the end user with an intuitive learning experience.
The website should be fully responsive and clearly display good UX design for small, medium and large breakpoints.

***


[Back to Contents](#table-of-contents)

--------

## User stories

Ask Num | Scenario                                                                                                                                              |
:--     | :---------------------------------------------------------------------------------------------------------------------------------------------------  |
1       | As a First Time Visitor, I want to easily understand the main purpose of the site?                                                                    |
2       | As a First Time Visitor, I want to be able to easily navigate the site and search for a product based on Category, Subcategory or my own Criteria     |
3       | As a First Time Visitor, I would like to be able to select and view detailed product information including price, rating and size where applicable    |
4       | As a First Time Visitor, I would like the ability to purchase an item or quantity of items, adding them to my shopping basket in a single step. 	    |
5       | As a First Time Visitor, I would like the ability to view a summary of the contents of my shopping basket.                	       					|
6       | As a First Time Visitor, I would like the ability to edit or delete the contents of my shopping basket.                                               |
7       | As a First Time Visitor, I would like the ability to register to the shopping site and store my details                                               |
8       | As a First Time Visitor, I would like the ability to make a purchase using a secure process   		                                                |
1       | As a Returning Visitor, I would like the ability to login or logout using my profile credentials           			                                |
2       | As a Returning Visitor, I would like the website to provide a facility to display my stored details                   				                |
3       | As a Returning Visitor, I would like the website to provide a facility to sort products based on category, product price, rating etc          		|
1       | As an Admin User, I would like to be able to perform the full set of CRUD operations on products and categories                         				|
2       | As an Admin User, I would like to be able to be able to modify delivery information globally for all products	                        				|
3	    | As an Admin User, I would like to be able to be able to view an order summary	for the entire site			                                    		|
1       | As a developer, I would like to be able to provide the back end redundancy described in Stripe Webhook tutorials	                        			|
2       | As a developer and time permitting, I would like to be able to integrate the inbuilt django test functionality described Hello Django Module	        |
3	    | As a developer and time permitting, I would like to be able to be in a position to present a clean secure, scalable and error free site	            |

***


[Back to Contents](#table-of-contents)


# Design

## Preparation
- As part of the preparation for this project I visited  several winter sports ecommerce sites reviewing site structure, theme and content, to gauge how best to approach the design and planning stages. These sites included but were not limited to [Blue Tomatoe](https://www.blue-tomato.com/en-IE/), [Dare2B](https://www.dare2b.ie/) & [53 Degrees North](https://www.53degreesnorth.ie/activity/skiing.html). 

## Scope
- The intent from the outset of the scoping process was to attempt is to meet all user requirements and provide additional functionality where possible within the existing time constraints.
- Given the extent of the deliverables and the very tight timelines (submission must be made by end of Jan'21), I thought it prudent to utilse the Tutorial code where possible without making my site a carbon copy of the 'Boutique Ado' example.
- To that end I've decided to create ~8 Django Apps:
* A home application used to render the store landing page styled to adhere to the overall site theme.
* A contact application to provide providing a form that will allow end users to contact the store owner or site admin.
* An about application to render site about details.  Note* I created this outside of the home application because, post submission, I intend on introducing additional functionality. The intent is to provide a site admin with a full set of CRUD capabilities for the about page.
* A categories application that will provide a site admin with the CRUD capabilities associated with the product categories. This will be rendered to adhere to the site theme and be wired up to the products views, such that, new categories will be automatically added to a New Offers dropdown in the main-nav.  In addition to the Categories CRUD capbilities available in the application a set of 22 Categories (4 Main & 18 Subcategories) will be loaded via manually created JSON files and the Django fixtures feature.
* A profiles application that will be wired up to the end users order history (time permiting) and utilising the allauth package to provide additional authenication, confirmation and user account functionality.  These templates will be customised to adhere the the winstersports site theme.
* A Products app used to render site products & details. Admin users will have CRUD capabilities for all products.  
Again per Category app items the initial set of products will be loaded via a manually created JSON file and the Django fixtures feature.  
Note* as mentioned above, in an effort to use my limited time as effeciently as possible, much of the product code will be derived from the CI Tutorials.  So Thank you kindly in advance Chris!  
I do, however, fully intend to customise the code, style it differently and provide additional functionaly where possible.  The intent, again time permitting, is to provide additional stock monitoring logic, and for the Detailed templates some carousel and tabbed views.
* A Shopping Bag application will provide the end user with the ability to add, delete and manipulate bag items.  Again much of teh code will have to be derived from the Tutorials.
* The Shopping bag app will be wired up to a Checkout application, which will use Stripe to provide a secure mechanism to make payments.  Time permitting I'll attempt to introduce webhooks and signal functionality to provide additional redundancy.
* The plan is to wire all this up to AWS's S3 to provide static file storage but this may not be possible in the tight timeframe.  As a result I intend to provide a Heroku based deployment using the Whitenoise package as a fallback.
* Re front end capabilties. I intend on creating uniquely styled base templates, navigation and and mobile views as a differentiator.  
* Re backend capabilities I've decided to turn the tutorial developement sequency on it's head, deploying the site to Heroku as a first step.  This is followed by development of the Profiles, Homepage, About, Contact, Categories, Product, Bag & Checkout applications in that sequence.  The thought process here is that it will communicate, a decent understanding of the underlying coding mechanisms and how to tie Django applications together.

[Back to Contents](#table-of-contents)

## Colour Scheme
-   I felt that a basic light blue theme contrasted against a white background was both aesthetically pleasing and reflected the outdoor winter sports nature of this ecommerce site. 
-   Additional Colour is to be introduced via the poster and images/urls associated with the individual products.
-	Re the Landing Page , I've decided use a Hero image that immediately communicates the nature of the site and enhances the existing colour the,.

## Typography
-   I've decided to use The Segoe UI family of fonts as defaults with Roboto and Sans Serif acting as the fallback alternatives.
-   They happen to be my preffered fonts given the crisp, basic styling.
-   I've decided to use both Font Awesome icons to highlight functionality and make the site more intuitive.
-	I'll use CSS to customise Bootstrap defaults further. These will include but will not be limited to various degrees of text-shadowing, font-sizes and text decoration
-	Finally, The plan is to use a combination of CSS transforms, python and Jinga methods to alter text capitalisation at various points within the project.

## Imagery
-   The intention is to use Bootstrap card-image components in conjunction with the product image urls to provide a central point of focus for the website. I also intend on using standard Bootstrap card elements, and icons styled with the sites light blue theme to provide secondary points of focus.
-	As described above the Landing Page Hero image is intended to both, enhance the site's theme, and immediately communicate its purpose.
-	Time permitting I also intend on creating a default poster, derived from ski related imagery, to be used in the event an admin user fails to select an image during the product creation process. 
-   This poster will be used to populate all empty proudct card-image elements, thereby maintaining consistency of UX across the site.

[Back to Contents](#table-of-contents)

## Navigation
-   Having reviewed several online ski shops it appears to be convention to allow the end user to filter based on gender and age aswell as product type. Snow/Skiwear is categorised not only by product type but whether it's targetting Men, Women or Children.  
There are several approaches to achieving this on the production sites, however, I've decided to use a three layer tabbed nav menu on desktop views and a two layer collapsible sidenav menu on mobile/tablet views.  
In maintaining this convention, it is hoped that it will make the site more intuitive for end users.
- In addion to the above I've also used an collapsible search box on mobile/tabled view and a fixed top nav search on desktop views.  
- Finally, in an attempt to, again enhance UX, I've seperated site admin and product related elements into there own menus.

## Responsive Elements
-   Placeholder

## Interactive Elements
-   Placeholder

## Authentication
-	The Profiles app when used in conjunction with Django's inbuilt capabilities and the allauth package provide the site with the functionality to authenticate users, send confirmation emails, reset passwords etc via multiple allauth templates customised work within the sites theme and colour scheme. 

***

[Back to Contents](#table-of-contents)

## Wireframes

### Mobile Balsamiq Mockups

#### Landing, About, Registration & Login Pages

<img src="/assets/wireframes/mobileView1.jpg" style="margin: 0;">

#### Product, Category & Checkout Pages

<img src="/assets/wireframes/mobileView2.jpg" style="margin: 0;">

### Tablet Balsamiq Mockups

#### Landing & Registration Pages

<img src="/assets/wireframes/tabletView1.jpg" style="margin: 0;">

#### Login, About & Category Pages

<img src="/assets/wireframes/tabletView2.jpg" style="margin: 0;">

#### Product & Checkout Pages

<img src="/assets/wireframes/tabletView3.jpg" style="margin: 0;">

### Desktop Balsamiq Mockups

#### Landing and About Pages
<img src="/assets/wireframes/desktopView1.jpg" style="margin: 0;">

#### Contact and Register Pages
<img src="/assets/wireframes/desktopView2.jpg" style="margin: 0;">

#### Login and Password Reset Pages
<img src="/assets/wireframes/desktopView3.jpg" style="margin: 0;">

#### Profile and Product Pages
<img src="/assets/wireframes/desktopView4.jpg" style="margin: 0;">

#### Product Detail and Shopping Bag Pages
<img src="/assets/wireframes/desktopView5.jpg" style="margin: 0;">

#### Checkout and Checkout Success Pages
<img src="/assets/wireframes/desktopView6.jpg" style="margin: 0;">

#### Manage Categories and Add Category Pages
<img src="/assets/wireframes/desktopView7.jpg" style="margin: 0;">

#### Add Product and Edit Product Pages
<img src="/assets/wireframes/desktopView8.jpg" style="margin: 0;">

#### Admin Product and Admin Product Detail Pages
<img src="/assets/wireframes/desktopView9.jpg" style="margin: 0;">


***


[Back to Contents](#table-of-contents)


# Database Structure

<div align="center">

</div>


## User Profile Model
Name			        |  Properties                                                                                                               		    |
:--    			        | :-----------------------------------------------------------------------------------------------------------------------------------  |
user    		        | models.OneToOneField(User, on_delete=models.CASCADE)                                                                                  |
default_phone_number    | models.CharField(max_length=20, null=True, blank=True)                                                                                |
default_street_address1 | models.CharField(max_length=80, null=True, blank=True)                                                                                |
default_street_address2 | models.CharField(max_length=80, null=True, blank=True)                                                                                |
default_town_or_city    | models.CharField(max_length=40, null=True, blank=True)                                                                                |
default_county          | models.CharField(max_length=80, null=True, blank=True)                                                                                |
default_country         | CountryField(blank_label='Country', null=True, blank=True)                                                                            |


## Main Category Model
Name			        |  Properties                                                                                                               		    |
:--    			        | :-----------------------------------------------------------------------------------------------------------------------------------  |
name                    | models.CharField(max_length=254)                                                                                                      |
friendly_name           | models.CharField(max_length=254, null=True, blank=True)                                                                               |

## Subcategory Model
Name			        |  Properties                                                                                                               		    |
:--    			        | :-----------------------------------------------------------------------------------------------------------------------------------  |
name                    | models.CharField(max_length=254)                                                                                                      |
friendly_name           | models.CharField(max_length=254, null=True, blank=True)                                                                               |
new                     | models.BooleanField(default=False, null=True, blank=True)                                                                             |

## Product Model
Name			        |  Properties                                                                                                               		    |
:--    			        | :-----------------------------------------------------------------------------------------------------------------------------------  |
main_category           | models.ForeignKey('MainCategory', null=False, blank=False, on_delete=models.SET_NULL)				             						|
sub_category            | models.ForeignKey('SubCategory', null=False, blank=False, on_delete=models.SET_NULL)    	                    						|
sku                     | models.CharField(max_length=254, null=True, blank=True)                                                                               |
name                    | models.CharField(max_length=254)                                                                                                      |
quantity                | models.PositiveIntegerField(default=1, max_value=99, null=True, blank=True)                                                           |
price                   | models.DecimalField(max_digits=6, decimal_places=2)                                                                                   |
rating                  | models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)                                                            |
summary                 | models.TextField(null=True, blank=True)                                                                                               |
details                 | models.TextField(null=True, blank=True)                                                                                               |
has_sizes               | models.BooleanField(default=False, null=True, blank=True)                                                                             |
image_url_1             | models.URLField(max_length=1024, null=True, blank=True)                                                                               |
image_1                 | models.ImageField(null=True, blank=True)                                                                                              |
image_url_2             | models.URLField(max_length=1024, null=True, blank=True)                                                                               |
image_2                 | models.ImageField(null=True, blank=True)                                                                                              |

## Order Model
Name			        |  Properties                                                                                                               		    |
:--    			        | :-----------------------------------------------------------------------------------------------------------------------------------  |
order_number	        | models.CharField(max_length=32, null=False, editable=False)                                                                           |
user_profile            | models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')                               |
full_name		        | models.CharField(max_length=50, null=False, blank=False)                                                                              |
email   		        | models.EmailField(max_length=254, null=False, blank=False)                                                                            |
phone_number            | models.CharField(max_length=20, null=True, blank=True)                                                                                |
street_address1         | models.CharField(max_length=80, null=True, blank=True)                                                                                |
street_address2         | models.CharField(max_length=80, null=True, blank=True)                                                                                |
town_or_city            | models.CharField(max_length=40, null=True, blank=True)                                                                                |
county                  | models.CharField(max_length=80, null=True, blank=True)                                                                                |
country                 | CountryField(blank_label='Country', null=True, blank=True)                                                                            |
date                    | models.DateTimeField(auto_now_add=True)                                                                                               |
delivery_cost           | models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)                                                            |
order_total             | models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)                                                           |
grand_total             | models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)                                                           |


## Order Line Items Model
Name			        |  Properties                                                                                                               		    |
:--    			        | :-----------------------------------------------------------------------------------------------------------------------------------  |
order       	        | models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')                                 |
product  		        | models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)                                                         |
product_size	        | models.CharField(max_length=2, null=True, blank=True)                                                                                 |
quantity                | models.IntegerField(null=False, blank=False, default=0)                                                                               |

## Contact Model
Name			        |  Properties                                                                                                               		    |
:--    			        | :-----------------------------------------------------------------------------------------------------------------------------------  |
full_name		        | models.CharField(max_length=50, null=False, blank=False)                                                                              |
email   		        | models.EmailField(max_length=254, null=False, blank=False)                                                                            |
subject                 | models.CharField(max_length=80, null=True, blank=True)                                                                                |
message                 | models.TextField(null=False, blank=False)                                                                                             |

***
    
[Back to Contents](#table-of-contents)

# Testing

## Bugs Found
- Issue with navbar toggler.  When elements added to mobile-header template whitespace introduced on left of row container for main nav.  Issue was resolved with help fo mentor. Required zero margin on toggler list-inline-items and zero padding on nav expand in base tenmplate. 
- Had difficulty getting Travis CI to integrate with repo.  Was a bit of a noob when it came to using Travis but with support from Stephen in Tutor team I found that the issue related settings config for development environment. Resolution to problem was changing the logic around database if else statement.
- Wanted to use Heroku deployment with staticfiles as part of ongoing testing for solution and as fall back in the event time ran short on submission.  Initially had difficulty getting css static files to load but used whitenoise and modification of settings.py middleware & statict storage to resolve same.  Unfortuantely still having difficulty with allauth components.
- On Profile and Contact form templates noted that I cannot apply margin or padding to columns or rows.  Used flexbox css to resolve spacing issue on contact details. Margin and padding problems related to incorrect use of Bootstrap helper classes.
- After I introduced a modal confirmation window for the category delete opeartion I noted that the delete function was no longer deleting the appropriate category, rather the first category in the database. Problem was due to same modal id being data target and resolved through use of template logic to tag each modal with unique idenifier.
- When first implementing toast messages I found that the toast was not rendering cleanly and none of the interfactive components worked. Used chrome DevTools to inspect console and found I was receiving error - "TypeError: $.toast is not a function" in jQuery?.  The ultimate resolution to the problem was to update the Bootstrap CDNs to v4.4.  I had previously been using v4.0 and toast are not supported on this release.
- I have truly been down the rabbit hole and like Alice ..... through the looking glass over the past 24hrs (",). 
Something that should have taken only half an hour, wiring up email backend to the project, took about a day in the round.  
I followed the tutorials to the letter but I had to integrate the backend with my development environment because the heroku deployment wasn't functioning outside of the homepage.
Even though Heroku was correctly displaying static css because of the whitenoise implementation I was receiving server error 500 for every other page I attempted to load.  
So back in the developement environment, every time I attempted to utilize email backend it failed with an authentication error message, and when I checked the gmail backend itself, it hadn't registered the auth attempt from my django app.
I went through numerous iterations of testing, each one itself requiring the registered email to be removed for the django admin, before I ultimately discovered the root cause.  Also...by way of FYI, flipping back and forth between the admin and unregistered views presented its own problems.....in that, if I failed to logout of django admin panel the session variables associated with the admin account would result in a CSRF error when attempting to register with the new temp email account.  
Long and short of it is the failure was not in off-piste code itself but the residual environmental variables I had loaded via the GitPod GUI interface during the Boutique_Ado tutorials.  Once they were removed the local developement environment started to behave more consistently.
I then moved onto the heroku depoyment itself. Altering the logic around access to the local environment using development and production variables in the django settings files sorted the problem with the 500 server error for the majority of pages but did not for the the about page, which is strange because it is the simplest of the apps to render.
I tried multiple combinations and permutations of configurations in attempt to resolve the server error, I even went as far as deleting, readding and reinitialising the heroku app but to no avail. 
During this time I also attempted to integrate the media data using suggestions I picked up from slack but to no avail.
I'm now going to park this and return to developing the site again.......wasted far too much time on these issues.

***

## Development Testing
- During cretaion of Add Category view, validated that category name did not already exist through use of form cleaned_data() method and multiple iterations of add task. cleaned_data() methid used to standardise form iputs to dictionary before check.
Also confirmed Boolean True attribute assigned correctly to new field upon creation through use of django admin.
- When testing the CRUD functionality for the categories app I found an issue with the delete view after introducing a modal confirmation window.
the same category id was being targetted regardless if the catergory selected.  This was resolved through use of template logic to uniquely identify each modal id.
- When wiring up toasts to the manage category crud functionality I decided to add in additional backend validation to prevent adding of category name if already exists in database. In addition to this I also set name field to readonly and validation against friendly name on edit category view.
Toasts were tested against form validation for display, add, edit and delete operations.   


[Back to Contents](#table-of-contents)
