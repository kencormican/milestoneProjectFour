# Table of Contents

**<details><summary>Testing</summary>**

* [Testing](#testing)
* [Testing Stripe Credit Card Transactions](#testing-stripe-credit-card-transactions)
</details>

**<details><summary>Testing User Stories</summary>**
* [Testing User Stories from User Experience (UX) Section](#testing-user-stories-from-user-experience-(ux)-section)
* [First Time Visitor Goals](#first-time-visitor-goals)
* [Returning Visitor Goals](#returning-visitor-goals)
* [Admin User Goals](#admin-user-goals)
* [Developer Goals](#developer-goals)
</details>

**<details><summary>Post Production Testing</summary>**
* [Post Production Testing](#post-production-testing)
* [Post Production Bugs Found](#post-production-bugs-found)
</details>

**<details><summary>Pre Production Testing</summary>**
* [Pre Production Testing](#pre-production-testing)
* [Pre Production Bugs Found](#pre-production-bugs-found)
</details>



# Testing

## Testing Stripe Credit Card Transactions

* If testing Stripe Credit Card Checkout Transactions please use the following test codes to emulate card transactions on the Stripe System:
```
If your Your integration handles payments that don’t require authentication:
Card Number: 4242424242424242
Your integration handles payments that require authentication
Card Number: 4000002500003155
Your integration handles card declines codes like insufficient_funds
Card Number: 4000000000009995
```
* Note The Webhooks events can be accessed directly from the Stripe dashboard, selecting developers, the events.

***
[Back to Contents](#table-of-contents)

### Testing User Stories from User Experience (UX) Section

#### First Time Visitor Goals
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

***
[Back to Contents](#table-of-contents)

#### To facilitate the First Time Visitor Goals:
* User Goal #1. 
    - Upon entering the site, users are greeted with clean and easily readable Banner, Navigation and Callout messages highlighting the sites intent. 
    - The Landing Page Hero image is intended to both, enhance the site's theme, and immediately communicate its purpose.
    - I felt that a basic light blue theme reflected the outdoor winter sports nature of this ecommerce site.
    - Functionality is replicated but represented differently on Mobile & Tablet Views.
    - Finally, per similar winter sports related e-commerce sites there are nav links to the main categories emphasised directly on the Landing Page Hero Image.
* User Goal #2.
    - Beneath  that they are presented with one of three high level options via Three discrete Nav areas:
    - Account and Store Infomation
    - Search Query, Brand Logo anchor or
    - Main site nav where they are invited to navigate the stores products.
* User Goal #2. 
    - Per Sample production sites that I reviewed as preparation for this site the product nav is divided into Category (All, Men, Women, Kids, Generic) and subcategory(Snowboard, Freeskie etc) views.
* User Goal #3. 
    - Users are provided with a large amount of detail on the main products page itself. This includes Name, Category, Price, Rating, & Stock Level.  
    - However, this is expanded upon further in the product detail view.  By select the image on the products page the user is brought to the individual Product's detailed view.  
    - Here the customer is provided with additional information such a product summary and product detailed information on the tabbed panel at the base of the page. 
    - The user is also provided with multiple product images (if available) in the form of a carousel or a placeholder image if no image is available.
* User Goal #4. 
    - To the right of the image carousel on desktop views or directly beneath the carousel on mobile views the user is provided with other details such as Stock Keeping Unit number, Sizes if available,  a Back to Shop and an Add to Bag  button.  
    - If they choose to add one or more items from the Add to Bag select button it is immediately reflected in the Bag icon in the Top Nav area.
* User Goal #5. 
    - The user is provided with a summary of their shopping basket contents of by clicking the shopping back icon on the top right of the page.
    - The Bag Icon is itself interactive changing colour when items are added to it and automatically displaying the basket total amount directly underneath it.
    - Within the Bag summary item, the user is presented with an empty bag message and a link back to the shop if they select it without having purchased anything.
    - If they have purchased one or more items, for each lineitem they are presented with an image card representing the purchase, the product name & sku, price, quantity & subtotal.
    - If the product has sizes each product size grouping is represented by a single line item.
    - Finally, at the base of the Bag is a Grand total calculating the delivery charges based on the FREE-DELIVERY values in the settings.py file and bag tools functions.
* User Goal #6. 
    - The end user is also provided with button to delete or update lineitem quantities.
    - Any changes are immediately reflected in the lineitem values, subtotal and grand total ammounts.
    - Toast Notification messages are provided as a further feedback mechanism for the end user.
* User Goal #7.
    - Registered users are provided with the ability to update and store there details via form inputs on the My Profile or Checkout pages.
    - The Checkout and Profile views have been wired up such that an order history summary is provided on the Profile page and can be linked to an invidual cached order using the order_history() and checkout_success() methods.
 User Goal #8.
    - A secure checkout with redundant back functionality has been provided via Stripe, the checkout form and associated views.  Backend form validation is present to mitigate against the end user breaking the transaction. Webhooks are also used to complete the transactions in the event a form submission partilally completes for any reason. This can be emulated by setting the commenting out the form.submit() method in the stripe_elements.js code.

***
[Back to Contents](#table-of-contents)

#### Returning Visitor Goals
Ask Num | Scenario                                                                                                                                              |
:--     | :---------------------------------------------------------------------------------------------------------------------------------------------------  |
1       | As a Returning Visitor, I would like the ability to login or logout using my profile credentials           			                                |
2       | As a Returning Visitor, I would like the website to provide a facility to display my stored details                   				                |
3       | As a Returning Visitor, I would like the website to provide a facility to sort products based on category, product price, rating etc          		|

* User Goal #1. 
    -  As a returning registered user, the functionality provided view the allauth package provides a standardised means (obviously styled to adhere to the sites theme) of registering, sending confimation emails, logging in/out using stored credentials, resetting passwords etc.
* User Goal #2.   
    - The profiles view, associated templates and forms provide the user with the ability to not only inspect their stored details but to amend them.  As described above this functionality is also wired up to the checkout/ordering process such that a registered end user can inspect their order history.
* User Goal #3.   
    - The products template and the main nav elements provide end users with the ability to filter or sort products based on price, rating, name and category.  The sort select box on the main products page is also wired up an event listener in products.js augmenting the products view itself by dynamically facilitating a change in sort direction on the page.

***
[Back to Contents](#table-of-contents)

#### Admin User Goals
Ask Num | Scenario                                                                                                                                              |
:--     | :---------------------------------------------------------------------------------------------------------------------------------------------------  |
1       | As an Admin User, I would like to be able to perform the full set of CRUD operations on categories                                    				|
2       | As an Admin User, I would like to be able to perform the full set of CRUD operations on products                                        				|

* User Goal #1. 
    - Admin users can now perform the full set of CRUD opearations on the subcategories.
    - The Categories view and associated template provide a super user with a list of subcategory cards diplayed responsively at diffent breakpoints.
    - The cards contain both the subcategory name and freindly name and allow the user to edit the friendly name only, or delete the category via one of two buttons on the card itself.
    - Defensive logic has been introduced firstly on the front end via the delete modal and secondly on the edit view, preventing users from assigning a friendly name already on the database, while also facilitating the empty field.   
    - On the catergories page directly above the subcategory cards themselves I've provided an add button allowing the user the create brand new subcategories on the database.  
    - Again, defensive logic has been introduced on the backend preventing the addition of a used subcategory name or friendly name.
    - Note* When adding new subcategories I've set the default the new so that the tag can be used to auto populate the New Offers Nav in the Main Nav area.
    - I've chosen not to make this an alterable value in the template itself, assuming any similar store will have a base product set which will have 'new' set to false by default and that the store owner would prefer to have new categories automatically added to the New Offers Nav section.
    - This could be altered  easily enough if the business logic changed.
    - Note* if you want to test this logic on your own clone iwthout having to manually create the necessary categories and products I've provided two sets of subcategory and products fixtures with this repo.
    - python3 manage.py loaddate subcategories and products with load the categories and associated products with the new tag set to false.
    - python3 manage.py loaddate new_subcategories and new_products with load the categories and associated products with the new tag set to True.
* User Goal #2. 
    - I've provided the superuser with the Product CRUD capabilities in a simlar fashion to that of categories views.  
    - There are a couple of key difference in that the add product url is accessed via the top nav and the edit and delete functions can be accessed via anchor elements in either the all products template or the product detail templete.
    - Again I've provided defensive front end logic in the form of a modal on delete.
    - I've chosen to diverge from the tutorials in providing to option to add two images for the detailed view carousel. In doing so I had to create some bespoke js code to capture the change event on both widgets given the tutorial logic uses an id common to both.


***
[Back to Contents](#table-of-contents)

#### Developer Goals
Ask Num | Scenario                                                                                                                                              |
:--     | :---------------------------------------------------------------------------------------------------------------------------------------------------  |
1       | As a developer, I would like to be able to provide the back end redundancy described in Stripe Webhook tutorials	                        			|
2	    | As a developer and time permitting, I would like to be able to be in a position to present a clean secure, scalable and error free site	            |

* User Goal #1. 
    - Thankfully I had just enough time to introduce the Webhook defensive logic on the checkout related views. This can be tested by emulating a break in form submission. This can be achieved by commenting out the form_submit() method in the stripe_elements.js static file, submitting a new order and checking the webhook event on the stripe dashboard for the "created using wenhook" as opposed to "created using databse" response text.
* User Goal #2.
    - Time was my enemy for this project but I believe I achieved the majority of my origianl goals as a developer. These include securing the Category, Product & Profile views using backend defensive logic.  Making the site a little more scalable with the CRUD and Autopopulate functionality provided by the categories templates and views.  A relatively clean delivery in that where store specific details, such as those in the contact form, or indeed the FREE_DELIVERY & RETURN related material,  can be variabalised or centralised, they were.
    - If I had more time I would iron out some of the styling limitations, introduce some further js around data toggling on both menus and create some automation functionality on the about app but I beleieve I have achieved all I can in the time alloted.


***
[Back to Contents](#table-of-contents)


## Post Production Testing
##### Note* I've placed the Post Production tesing section before the Pre Production section for two reasons.  One, it more closely mirrors the end user goals and associated testing. Two it is less verbose. That said please read the pre-production section if you wish to get an understanding of the types of hurdles I encountered during the development process.

|TesT No.|Page           |Test Description                     |Anonymous|Registered          |Superuser|Chrome|Edge|Comments                                                         |Corrected|
|--------|---------------|-------------------------------------|---------|--------------------|---------|------|----|-----------------------------------------------------------------|---------|
|1       |Home           |Landing Page Nav links working       |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|2       |Home           |Landing Page Nav links responsive    |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|3       |Home           |Landing Page Nav links interactive   |Pass     |Pass                |Pass     |Pass  |Pass|Amber on hover.  Nice Contrast.                                  |         |
|4       |Home           |Landing Page image responsive        |Pass     |Pass                |Pass     |Pass  |Pass|Works well at all breakpoints                                    |         |
|5       |Nav            |Top Nav anchors working              |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|6       |Nav            |Top Nav responsive                   |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|7       |Nav            |Top Nav interactive                  |Pass     |Pass                |Pass     |Pass  |Pass|Both Text & Pointer                                              |         |
|8       |Nav            |Mobile Top Nav anchors working       |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|9       |Nav            |Mobile Top Nav responsive            |Pass     |Pass                |Pass     |Pass  |Pass|Both Text & Pointer                                              |         |
|10      |Nav            |Mobile Top Nav interactive           |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|11      |Nav            |Nav Filtering Applied Desktop        |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|12      |Nav            |Nav Filtering Applied Mobile         |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|13      |Nav            |Category Nav links working           |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|14      |Nav            |Category Nav Links rendering         |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|15      |Nav            |Category Nav Links responsive        |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|16      |Nav            |Category Nav Links interactive       |Pass     |Pass                |Pass     |Pass  |Pass|Both Text & Pointer.  Need to return to active tab jinga if time.|         |
|17      |Nav            |Subategory Nav Links responsive      |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|18      |Nav            |Subategory Nav Links interactive     |Pass     |Pass                |Pass     |Pass  |Pass|Pointer Only                                                     |         |
|19      |Nav            |Top & Mobile Search inputs working   |Pass     |Pass                |Pass     |Pass  |Pass|Bootstrap toggle a bit clunky                                    |         |
|20      |Nav            |Top & Mobile Search responsive       |Pass     |Pass                |Pass     |Pass  |Pass|Styling could better Mobnav                                      |         |
|21      |About          |Rendering correctly at breakpoints   |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|22      |Contact        |Rendering correctly at breakpoints   |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|23      |Contact        |Form interactive                     |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|24      |Contact        |Form validation working              |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|25      |Contact        |Environmental variables displayed    |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|26      |Contact        |Success template rendering correctly |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|27      |Contact        |Email backend working                |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|28      |Contact        |Email templates working              |Pass     |Pass                |Pass     |Pass  |Pass|Good Internal & External mail                                    |         |
|29      |Contact        |Internal & External Mails sent       |Pass     |Pass                |Pass     |Pass  |Pass|Good Internal & External mail                                    |         |
|30      |Contact        |Toasts working                       |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|31      |Categories     |View Secure                          |Fail     |Fixed This iteration|Pass     |Pass  |Pass|@login_required decorator required'                              |Yes      |
|32      |Categories     |Rendering correctly at breakpoints   |N/A      |N/A                 |Pass     |Pass  |Pass|                                                                 |         |
|33      |Categories     |Anchor/Button elements working       |N/A      |N/A                 |Pass     |Pass  |Pass|                                                                 |         |
|34      |Categories     |Categories jinga templates working   |N/A      |N/A                 |Pass     |Pass  |Pass|                                                                 |         |
|35      |Categories     |Add, Edit and Delete links working   |N/A      |N/A                 |Pass     |Pass  |Pass|                                                                 |         |
|36      |Categories     |Delete Modal Working                 |N/A      |N/A                 |Pass     |Pass  |Pass|                                                                 |         |
|37      |Categories     |Delete view working                  |N/A      |N/A                 |Pass     |Pass  |Pass|Modal Provides user with 2 changes to delete.                    |         |
|38      |Categories     |Delete view secure                   |N/A      |N/A                 |Pass     |Pass  |Pass|                                                                 |         |
|39      |Categories     |Toasts working                       |N/A      |N/A                 |Pass     |Pass  |Pass|                                                                 |         |
|40      |Add Category   |view secure                          |Pass     |Pass                |Pass     |Pass  |Pass|Redirected to signin/ and message if registered                  |         |
|41      |Add Category   |view and url working                 |N/A      |N/A                 |Pass     |Pass  |Pass|                                                                 |         |
|42      |Add Category   |Template responsive                  |N/A      |N/A                 |Pass     |Pass  |Pass|                                                                 |         |
|43      |Add Category   |Form validation working              |N/A      |N/A                 |Pass     |Pass  |Pass|                                                                 |         |
|44      |Add Category   |Defensive logic working              |N/A      |N/A                 |Pass     |Pass  |Pass|Prevents addition if Category if Name or Friendly/Name exits     |         |
|45      |Add Category   |Toasts working                       |N/A      |N/A                 |Pass     |Pass  |Pass|                                                                 |         |
|46      |Add Category   |Automatic update of New Offers Nav   |N/A      |N/A                 |Pass     |Pass  |Pass|                                                                 |         |
|47      |Add Category   |New Offer nav filter correct         |N/A      |N/A                 |Pass     |Pass  |Pass|                                                                 |         |
|48      |Edit Category  |view secure                          |Pass     |Pass                |Pass     |Pass  |Pass|Redirected to signin/ and message if registered                  |         |
|49      |Edit Category  |view and url working                 |N/A      |N/A                 |Pass     |Pass  |Pass|                                                                 |         |
|50      |Edit Category  |Template responsive                  |N/A      |N/A                 |Pass     |Pass  |Pass|                                                                 |         |
|51      |Edit Category  |Form validation working              |N/A      |N/A                 |Pass     |Pass  |Pass|                                                                 |         |
|52      |Edit Category  |Defensive logic working              |N/A      |N/A                 |Pass     |Pass  |Pass|Prevents updating if Category if Name or Friendly/Name exits     |         |
|53      |Edit Category  |Toasts working                       |N/A      |N/A                 |Pass     |Pass  |Pass|                                                                 |         |
|54      |Products       |Anchor elements working              |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|55      |Products       |Filtering Working                    |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|56      |Products       |Filter counting working              |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|57      |Products       |Filter Home links working            |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|58      |Products       |Sorting  Working                     |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|59      |Products       |Product lables & pricing  correct    |Pass     |Pass                |Pass     |Pass  |Pass|Zero, None & other Ratin good                                    |         |
|60      |Products       |Responsive Product Rating working    |Pass     |Pass                |Pass     |Pass  |Pass|Set ski binding qty to zero and good                             |         |
|61      |Products       |Responsive Qty & Out of stock correct|Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|62      |Products       |View Secure                          |Pass     |Pass                |Pass     |Pass  |Pass|Redirected to Sign In on /add                                    |         |
|63      |Products       |Edit and Delete links working        |N/A      |N/A                 |Pass     |Pass  |Pass|                                                                 |         |
|64      |Products       |Image working for file or url        |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|65      |Products       |No image file working                |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|66      |Product Details|Select cat and redirect working      |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|67      |Product Details|Anchor elements working              |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|68      |Product Details|Carousel working                     |Pass     |Pass                |Pass     |Pass  |Pass|Working for no, single and double image                          |         |
|69      |Product Details|Tab Nav working                      |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|70      |Product Details|Responsive rating working            |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|71      |Product Details|Responsive Qty & Out of stock correct|Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|72      |Product Details|Product lables & pricing  correct    |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|73      |Product Details|Quantity & Out of stock correct      |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|74      |Product Details|View Secure                          |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|75      |Product Details|Edit and Delete links working        |N/A      |N/A                 |Pass     |Pass  |Pass|                                                                 |         |
|76      |Product Details|Image working for file or url        |Pass     |Pass                |Pass     |Pass  |Pass|Leash has url only                                               |         |
|77      |Product Details|No image file working                |Pass     |Pass                |Pass     |Pass  |Pass|Test Product1 has no image                                       |         |
|78      |Product Details|Back to shop button workig           |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|79      |Product Details|Add Button and qty working           |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|80      |Product Details|Sizes Options working                |Pass     |Pass                |Pass     |Pass  |Pass|Kids Jacket has sizes                                            |         |
|81      |Product Details|Toasts working                       |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|82      |Add Product    |view secure                          |Pass     |Pass                |N/A      |Pass  |Pass|                                                                 |         |
|83      |Add Product    |view and url working                 |N/A      |N/A                 |Pass     |Pass  |Pass|                                                                 |         |
|84      |Add Product    |Template responsive                  |N/A      |N/A                 |Pass     |Pass  |Pass|                                                                 |         |
|85      |Add Product    |Template working fully               |N/A      |N/A                 |Fail     |Pass  |Pass|Problem with 2nd image select. Filename not showing.             |Yes      |
|86      |Add Product    |Form validation working              |N/A      |N/A                 |Pass     |Pass  |Pass|No add on rating or name none                                    |         |
|87      |Add Product    |Toasts working                       |N/A      |N/A                 |Pass     |Pass  |Pass|                                                                 |         |
|88      |Edit Product   |view secure                          |Pass     |Pass                |N/A      |Pass  |Pass|Redirected to Sign In on /edit/1                                 |         |
|89      |Edit Product   |view and url working                 |N/A      |N/A                 |Pass     |Pass  |Pass|                                                                 |         |
|90      |Edit Product   |Template responsive                  |N/A      |N/A                 |Pass     |Pass  |Pass|                                                                 |         |
|91      |Edit Product   |Template working fully               |N/A      |N/A                 |Fail     |Pass  |Pass|Problem with 2nd image select. Filename not showing.             |Yes      |
|92      |Edit Product   |Form validation working              |N/A      |N/A                 |Pass     |Pass  |Pass|No edit on rating or name none                                   |         |
|93      |Edit Product   |Toasts working                       |N/A      |N/A                 |Pass     |Pass  |Pass|                                                                 |         |
|94      |Shopping Bag   |view and url working                 |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|95      |Shopping Bag   |Template responsive                  |Pass     |Pass                |Pass     |Pass  |Pass|Padding on delete & edit button could be better                  |         |
|96      |Shopping Bag   |Bag Icon Interactive                 |Pass     |Pass                |Pass     |Pass  |Pass|Updated on change                                                |         |
|97      |Shopping Bag   |Bag interactive                      |Fail     |Fixed This iteration|Pass     |Pass  |Pass|Fail on Bag empty feedback                                       |Yes      |
|98      |Shopping Bag   |Defensive logic working              |Pass     |Pass                |Pass     |Pass  |Pass|Image if statements working                                      |         |
|99      |Shopping Bag   |Update & Delete working              |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|100     |Shopping Bag   |Image working for file or url        |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|101     |Shopping Bag   |No image file working                |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|102     |Shopping Bag   |Sizes Options working                |Pass     |Pass                |Pass     |Pass  |Pass|Separate line items for different sizes                          |         |
|103     |Shopping Bag   |Subtotals and Grand Total working    |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|104     |Shopping Bag   |Link to checkout and return working  |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|105     |Shopping Bag   |Form validation working              |Pass     |Pass                |Pass     |Pass  |Pass|Wont update unless new value applied                             |         |
|106     |Shopping Bag   |Toasts working                       |Fail     |Fixed This iteration|Pass     |Pass  |Pass|Fail on delete only. Resolved with empty bag issue.              |Yes      |
|107     |Secure Checkout|Form Interactive                     |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|107     |Secure Checkout|view and url working                 |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|108     |Secure Checkout|Template responsive                  |Pass     |Pass                |Pass     |Pass  |Pass|Good at different breakpoints                                    |         |
|109     |Secure Checkout|Defensive logic working              |Pass     |Pass                |Pass     |Pass  |Pass|Re images                                                        |         |
|110     |Secure Checkout|Form validation working              |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|111     |Secure Checkout|Profile Feedback working             |Pass     |Pass                |Pass     |Pass  |Pass|Different Checkout succes page                                   |         |
|112     |Secure Checkout|Order Summary Working                |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|113     |Secure Checkout|Stripe Working                       |Pass     |Pass                |Pass     |Pass  |Pass|Payment succeeded and event stored                               |         |
|114     |Secure Checkout|Webhooks working                     |Pass     |Pass                |Pass     |Pass  |Pass|Event Capture and WH recorded                                    |         |
|115     |Secure Checkout|Email Confirmation working           |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|116     |Allauth        |Sign In/Out views working            |N/A      |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|117     |Allauth        |Register, Reset views working        |Pass     |Pass                |Pass     |Pass  |Pass|Received confm mail on password reset                            |         |
|118     |Allauth        |Email Confirmation working           |Fail     |Fixed this iteration|Pass     |Pass  |Pass|Email sent but incorrect currency                                |Yes      |
|119     |Allauth        |Templates responsive                 |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|120     |Allauth        |Templates per site Theme             |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|121     |Allauth        |Form interactive                     |Pass     |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|122     |My Profile     |View working                         |N/A      |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|123     |My Profile     |Template responsive                  |N/A      |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|124     |My Profile     |Order History Working                |N/A      |Pass                |Pass     |Pass  |Pass|                                                                 |         |
|125     |My Profile     |Feedback with checkout working       |N/A      |Pass                |Pass     |Pass  |Pass|                                                                 |         |
***

[Back to Contents](#table-of-contents)

## Post Production Bugs Found
* Manage Categories. While the add, edit and delete views were secure the main categories nav template was still accessable for none admin users.  To resolve I assigned the @login_required decorator required' and if superuser statements to the manage_categories() view.
* Add/Edit Products. The change event js used in pre-production deployment targetted an id common to both widgets and when a second file was uploaded its details were not updated correctly.  Had to traverse the DOM to action the apporiate element.
* Bag empty template was failing to provide appropriate feedback due to an incorrectly assigned comment.  This was also affecting some of the bag toast messages. Was resolved by reactivating commented out code.
* Email Confirmation Currency displayed was incorrect.  Resolved by amending the appropriate template. 
***
[Back to Contents](#table-of-contents)



## Pre Production Testing

##### Please note * that this section is written in the present tense and captures issues as and when I encounterd them so please view it n that context.

- During cretaion of Add Category view, validated that category name did not already exist through use of form cleaned_data() method and multiple iterations of add task. cleaned_data() method used to standardise form iputs to dictionary before check.
Also confirmed Boolean True attribute assigned correctly to new field upon creation through use of django admin.
- When testing the CRUD functionality for the categories app I found an issue with the delete view after introducing a modal confirmation window.
the same category id was being targetted regardless if the catergory selected.  This was resolved through use of template logic to uniquely identify each modal id.
- When wiring up toasts to the manage category crud functionality I decided to add in additional backend validation to prevent adding of category name if already exists in database. In addition to this I also set name field to readonly and validation against friendly name on edit category view.
Toasts were tested against form validation for display, add, edit and delete operations.
- Spent a significant amount of time over past two days validating, development and heroku environments to ensure the backend email functionality was wired up correctly before commencing final steps with contact app.  Having cleaned up the os environment in the settings.py file I tied myself up in knots for a couple of hours by accidentally changing one the develepment variables to a string.  Knew where the problem had to lie but couldn't make the wood from the trees when looking at the code. Quotation marks ehh!
- Contact app form submission was tested for both internal external comms to development console level the external email backend.
I also validated insertion of appropriate variable details in contact and confirm email text templates.
Attempted to integtrate the methodology described in the Stripe Webhooks email tutorials with that of this [Online Django Email/Contact Form Tutorial](https://learndjango.com/tutorials/django-email-contact-form).
- When testing the tabbed views I found it very difficult to develop the logic to approriately render the tabs with assoicated sub menu searches results while also highlighting the appropriate tab.  The plan is to complete the logic for all products and then move onto the Men, Women and Kids tab views.  At this point in time I think the simplest way to approach it is to generate independent views and templates for the tob level categories.  
- When testing the search functionality in the products view I found that none of the catergory names were being returned in results. When I initially added the logic to return same it responded with an error.  See Bugs for resolution to problem.
- Gave whitenoise another crack of the whip last night.  This time went at it with the knowledge & acceptance that whitenoise treats media files differently to other static files, that per these [support notes](assets/support_info/whitenoise_media.jpg) it was not designed to serve user uploaded media, and that a Django project when deployed to Heroku using whitenoise serves media files differently when in DEBUG mode thand with DEBUG disabled.  It worked cleanly using the below setup:
from bash command line install whitenoise and freeze new dependency to requirements.txt:
```
pip3 install whitenoise
pip3 freeze --local > requirements.txt
```
* In settings.py setup HEROKU environment for DEBUG....remember to apply settings to hereoku config to facilitate same.  Also remember to disable same if you truely move to deploy a realworld application in production:

```
if development:
    DEBUG = True
elif production:
    DEBUG = True
else:
    DEBUG = False
```
* Configure the DATABASE options in settings.py explicitly for the Heroku Postgres setup:
```
# if production:
DATABASES = {'default': dj_database_url.parse(
    os.environ.get('DATABASE_URL'))}

# else:
#     print("Development Environment. Using SQLite")
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#         }
#     }

```
* Add whitenoise components to settings.py noting WhiteNoise middleware should be placed directly after the Django SecurityMiddleware and before all other middleware:
```
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # whitenoise dependency
    .....
]
.....
.....

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Extra places for collectstatic to find static files.
# Whitenoise dependency.

STATICFILES_DIRS = (os.path.join(
    BASE_DIR, 'static'),)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```
* Then push to Heroku perform migration, load any fixtures you may have and create your superuser.
```
git add .
git commit -m ""
git push heroku master
python3 manage.py migrate --plan
python3 manage.py migrate
python3 manage.py loaddate <fixture_name>
python3 manage.py createsuperuser
```
* Once complete launch the app from Heroku, confirm your seeing all the relavant styling......this confirms static is being loaded correctly.
Then confirm images nd media files are being loaded correctly. <strong>(NOTE* YOU MUST HAVE DEBUG SET TO TRUE FOR THIS TO WORK).</strong>
Then verify your fixtures and data base elements are functioning correctly.
* Finally, restore the database elements in the settings.py file to original setup which allows for development and production operations.
```
if production:
    DATABASES = {'default': dj_database_url.parse(
        os.environ.get('DATABASE_URL'))}

else:
    print("Development Environment. Using SQLite")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```

* When testing the add category functionality I initially had difficulty loading the newly added categories to the main-nav template because it was part of the base template infrastructure, needed to be available for all apps and didn't have its own view.  So needed a way to pass data from the backend through to the front end without explicitly being called by an app.  I found a very useful [stack overflow](https://stackoverflow.com/questions/34902707/how-can-i-pass-data-to-django-layouts-like-base-html-without-having-to-provi) link explaining that it needed to be created as a user generated context processor and then loaded to the of base infrastructure via settings.py under TEMPLATE options per below.
```
context_processors.py

from .models import Subcategory


def add_categories_to_context(request):

    subcategories = Subcategory.objects.all()

    return {
        'subcategories': subcategories,
    }

settings.py

TEMPLATES = [
    { ......
        ],.....
        'OPTIONS': {
            'context_processors': [
                '......
                'categories.context_processors.add_categories_to_context',
            ],

main-nav.html

            <li class="nav-item dropdown">
                <a class="mainnav-font font-weight-bold nav-link text-blue mr-5 text-uppercase" href="#" id="newcategories-link"
                    data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    <h6 class="mx-2 my-0">New Offers</h6>
                </a>
                <div class="dropdown-menu border-0 text-capitalize" aria-labelledby="newcategories-link">
                    {% for subcategory in subcategories %}
                        {% if subcategory.new %}
                            <a href="{% url 'products' %}?subcategory={{subcategory.name}}" class="dropdown-item text-secondary">
                                {% if subcategory.friendly_name %} 
                                    {{ subcategory.friendly_name }}
                                {% else %} 
                                    {{subcategory.name}}
                                {% endif %}
                            </a>
                        {% endif %}
                    {% endfor %}
                </div>
            </li>

```

* Tested clean for loading manually created subcategories to the nav menu and those set with new field to true in fixture.  Associated link items also tested clean.
* Products CRUD functionality testing clean from both Proucts and Product details views.   Defensive logic introduced in Product and product detailed views for products with or with images, urls etc. Initially encountered some issues with rendering Product image add and select options. Product detail carousel and tabbed views working cleanly for mobile, Tablet and Desktop views. 
* Securing Views - Products, Categories and Profile views secured on back-end against unauthorised users. Add, Edit and Delete views protected and testing clean.  Risk of URLs based post and delete fabrication requests mitigated by introducing @login_required decorators.  Unless user logged in such requests will be redirected back to home page. Further defensive logic has been introduced by checking if user is superuser in Add, Update & Delete views. If not the users are provided with error message and redirected back to home page.
* Shopping Bag CRUD functionality testing clean for add, edit and delete operations.  Bag also tested for products with and without sizes, with and without images, with and without image urls.  Initially encountered some minor problems with post on none operations and image template syntax but introduced some defensive logic to mitigate same.
* Checkout app testing clean and introduced redundancy to ordering process using Webhook Handler.  Order tested for completion using database and webhook datasets.  Form submission failure emulated by commenting out form.submit() method in stripe js code and submitting order. Response was order created using WH.  When form.submit() re-activated in js code response confirmed to be order created using database.
* Profile order history update testing clean for registered users and working when stripe element form submit is disabled proving out webhook redundancy.  Link between individual history order  and checkout view also testing clean.
* Order Email confirmation testing cleanly to both console and email backend.
* Production site wired up to AWS S3. Static files and Images uploading and displaying correctly.  
***

[Back to Contents](#table-of-contents)

## Pre Production Bugs Found
- Issue with navbar toggler.  When elements added to mobile-header template whitespace introduced on left of row container for main nav.  Issue was resolved with help from mentor. Required zero margin on toggler list-inline-items and zero padding on nav expand in base tenmplate. 
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
- Encountered a problem when trying to migrate Products models with categories models. Receiving following error.
products.Product.category: (fields.E300) Field defines a relation with model 'Category', which is either not installed, or is abstract.
Fix was found on Slack.  Even though the models were imported the foreignkey model name still needed to be prefixed with app name i.e. categories.Category before the system would make the relationship.
- Had issue rendering no_image using {{ MEDIA_URL }} template prefix.  Resolve was to include "django.template.context_processors.media" in TEMPLATES object of settings.py 
- When adding search for subcategory name to products query function it produced following error:
Related Field got invalid lookup: icontains
I found through this [stackoverflow URL](https://stackoverflow.com/questions/11754877/troubleshooting-related-field-has-invalid-lookup-icontains) that this was because subcategory is a foreign key in the products model.
To resolve this I had to add the foreign key field with a search fields option in the ProductAdmin model 
```
search_fields = ['subcategory__name']
```
Then explicity call out the name in query logic in the products view:
```
queries = Q(name__icontains=query) | Q(summary__icontains=query) | Q(subcategory__name__icontains=query)
```
* When adding the code to render the image widget more cleanly I found it difficult rendering the two crispy-form image widgets as a pair of side-by-side bootstrap col-6 divs.
Have read several articles and tried several crispy forms helpers and widget tweaker addons but have been unable to resolve completely.  At present the divs are both col-6 divs but they are stacking as opposes to inline. Will need to come back to this later.
* Encountered two issues when testing bag app last night. The first, initially appeared to be specific to items that did not have image urls datatabase.  Then discovered template syntax was also a factor.  Added in some defensive code to check for multiple locations, change the template syntax and it resolved problem.
 Error 1:
```
ValueError at /bag/
The 'image1' attribute has no file associated with it.
```
* offending code.
```
{% for item in bag_items %}
    <tr>
        <td class="p-3 w-25">
            <img class="img-fluid rounded" src="{{ item.product.image1.url }}">
        </td>
```
* fix
```
<td class="p-3 w-25">
    <img class="img-fluid rounded" src="
        {% if item.product.image %}
            {{ item.product.image }}
        {% elif item.product.image1_url %}
            {{ item.product.image1_url }}  
        {% else %}
            {{ MEDIA_URL }}noimage.png
        {% endif %}">
</td>
```
* The second occurs only if the bag form updated without changing the entry.  It therefore posts the quantity as an empty string.  The view then fails because it is expecting integer value.
```
invalid literal for int() with base 10: ''
....
quantity	''
```
* offending code.
```
def update_bag(request, item_id):
    quantity = int(request.POST.get('quantity'))
    size = None
```
* Resolved by making the input field required on this form therefore preventing it being subitted without a value being altered.
```
<input class="form-control form-control-sm qty_input w-100 rounded mt-1" type="number" name="quantity" placeholder="{{ item.quantity }}" min="0" max="99" required>
```
* long text in the manage categories template was creating oversized card.  Resolved setting text-truncate on field classes. 
* Initially had issue when moved to AWS S3 storage with some CSS was not rendering correctly.  Issue was residual STATIC_ROOT setup from whitenoise deployment was causing issues with custom_storage.py and settings.py file locations.  Applying STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),) resolved problem.

***

[Back to Contents](#table-of-contents)

