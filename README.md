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
* [Wireframes](#wireframes)
</details>

***


## Demo

[View the live project here.](TBC)


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


## Wireframes

### Desktop Balsamiq Mockups

#### Landing and About Pages
<img src="/wireframes/desktopView1.jpg" style="margin: 0;">

#### Contact and Register Pages
<img src="/wireframes/desktopView2.jpg" style="margin: 0;">

#### Login and Password Reset Pages
<img src="/wireframes/desktopView3.jpg" style="margin: 0;">

#### Profile and Product Pages
<img src="/wireframes/desktopView4.jpg" style="margin: 0;">

#### Product Detail and Shopping Bag Pages
<img src="/wireframes/desktopView5.jpg" style="margin: 0;">

#### Checkout and Checkout Success Pages
<img src="/wireframes/desktopView6.jpg" style="margin: 0;">

#### Manage Categories and Add Category Pages
<img src="/wireframes/desktopView7.jpg" style="margin: 0;">

#### Add Product and Edit Product Pages
<img src="/wireframes/desktopView8.jpg" style="margin: 0;">

#### Admin Product and Admin Product Detail Pages
<img src="/wireframes/desktopView9.jpg" style="margin: 0;">


***


[Back to Contents](#table-of-contents)


## Database Structure

<div align="center">

</div>


### User Profile Model
Name			|  Properties                                                                                                                          		    |
:--    			| :------------------------------------------------------------------------------------------------------------------------------------------   |
full_name		| models.CharField(max_length=32, null=False, editable=False)                                                                                   |
full_name		| models.CharField(max_length=32, null=False, editable=False)                                                                                   |
full_name		| models.CharField(max_length=32, null=False, editable=False)											                                        |
full_name		| models.CharField(max_length=32, null=False, editable=False)											                                        |
full_name		| models.CharField(max_length=32, null=False, editable=False)											                                        |
full_name		| models.CharField(max_length=32, null=False, editable=False)											                                        |
full_name		| models.CharField(max_length=32, null=False, editable=False)											                                        |
full_name		| models.CharField(max_length=32, null=False, editable=False)											                                        |
full_name		| models.CharField(max_length=32, null=False, editable=False)											                                        |
full_name		| models.CharField(max_length=32, null=False, editable=False)											                                        |


### Category Model
Name			| Properties                                                                                                                          		    |
:--    			| :------------------------------------------------------------------------------------------------------------------------------------------   |
full_name		| models.CharField(max_length=32, null=False, editable=False)                                       											|
full_name		| models.CharField(max_length=32, null=False, editable=False)                                                                                   |
full_name		| models.CharField(max_length=32, null=False, editable=False)											                                        |
full_name		| models.CharField(max_length=32, null=False, editable=False)											                                        |
full_name		| models.CharField(max_length=32, null=False, editable=False)											                                        |
full_name		| models.CharField(max_length=32, null=False, editable=False)											                                        |
full_name		| models.CharField(max_length=32, null=False, editable=False)											                                        |
full_name		| models.CharField(max_length=32, null=False, editable=False)											                                        |
full_name		| models.CharField(max_length=32, null=False, editable=False)											                                        |
full_name		| models.CharField(max_length=32, null=False, editable=False)											                                        |


### Product Model
Name			| Properties                                                                                                                          		    |
:--    			| :------------------------------------------------------------------------------------------------------------------------------------------   |
full_name		| models.CharField(max_length=32, null=False, editable=False)                                       											|
full_name		| models.CharField(max_length=32, null=False, editable=False)                                                                                   |
full_name		| models.CharField(max_length=32, null=False, editable=False)											                                        |
full_name		| models.CharField(max_length=32, null=False, editable=False)											                                        |
full_name		| models.CharField(max_length=32, null=False, editable=False)											                                        |
full_name		| models.CharField(max_length=32, null=False, editable=False)											                                        |
full_name		| models.CharField(max_length=32, null=False, editable=False)											                                        |
full_name		| models.CharField(max_length=32, null=False, editable=False)											                                        |
full_name		| models.CharField(max_length=32, null=False, editable=False)											                                        |
full_name		| models.CharField(max_length=32, null=False, editable=False)											                                        |


### Order Model
Name			| Properties                                                                                                                          		    |
:--    			| :------------------------------------------------------------------------------------------------------------------------------------------   |
full_name		| models.CharField(max_length=32, null=False, editable=False)                                       											|
full_name		| models.CharField(max_length=32, null=False, editable=False)                                                                                   |
full_name		| models.CharField(max_length=32, null=False, editable=False)											                                        |
full_name		| models.CharField(max_length=32, null=False, editable=False)											                                        |
full_name		| models.CharField(max_length=32, null=False, editable=False)											                                        |
full_name		| models.CharField(max_length=32, null=False, editable=False)											                                        |
full_name		| models.CharField(max_length=32, null=False, editable=False)											                                        |
full_name		| models.CharField(max_length=32, null=False, editable=False)											                                        |
full_name		| models.CharField(max_length=32, null=False, editable=False)											                                        |
full_name		| models.CharField(max_length=32, null=False, editable=False)											                                        |

    
[Back to Contents](#table-of-contents)

