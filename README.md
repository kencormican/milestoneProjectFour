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

***

## Development Testing
- During cretaion of Add Category view, validated that category name did not already exist through use of form cleaned_data() method and multiple iterations of add task. cleaned_data() methid used to standardise form iputs to dictionary before check.
Also confirmed Boolean True attribute assigned correctly to new field upon creation through use of django admin.


[Back to Contents](#table-of-contents)
