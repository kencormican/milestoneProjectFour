# Table of Contents

**<details><summary>Testing</summary>**

* [Testing](#testing)
* [Stripe Checkout testing](#stripe-checkout-testing)
* [Post Production Testing](#post-production-testing)
* [Post Production Bugs Found](#post-production-bugs-found)
* [Pre Production Testing](#pre-production-testing)
* [Pre Production Bugs Found](#pre-production-bugs-found)

</details>


# Testing

## Stripe Checkout testing
To emulate card transactions please you the following card codes.
```
Your integration handles payments that don’t require authentication
0/3 tests completed
4242424242424242
Your integration handles payments that require authentication
0/4 tests completed
4000002500003155
Your integration handles card declines codes like insufficient_funds
0/4 tests completed
4000000000009995
```

## Post Production Testing
|TesT No.|Page           |Test Description                     |Anonymous|Registered|Superuser|Chrome|Edge|Corrected|Comments|
|--------|---------------|-------------------------------------|---------|----------|---------|------|----|---------|--------|
|1       |Home           |Top Nav anchors working              |         |          |         |      |    |         |        |
|2       |Home           |Top Nav responsive                   |         |          |         |      |    |         |        |
|3       |Home           |Mobile Top Nav anchors working       |         |          |         |      |    |         |        |
|4       |Home           |Mobile Top Nav responsive            |         |          |         |      |    |         |        |
|5       |Home           |Nav Filtering Applied Desktop        |         |          |         |      |    |         |        |
|6       |Home           |Nav Filtering Applied Mobile         |         |          |         |      |    |         |        |
|7       |Home           |Landing Page Nav links working       |         |          |         |      |    |         |        |
|8       |Home           |Landing Page Nav links responsive    |         |          |         |      |    |         |        |
|9       |Home           |Category Nav links working           |         |          |         |      |    |         |        |
|10      |Home           |Category Nav Links rendering         |         |          |         |      |    |         |        |
|11      |Home           |Category Nave Links responsive       |         |          |         |      |    |         |        |
|12      |About          |Rendering correctly at breakpoints   |         |          |         |      |    |         |        |
|13      |Contact        |Rendering correctly at breakpoints   |         |          |         |      |    |         |        |
|14      |Contact        |Form responsive                      |         |          |         |      |    |         |        |
|15      |Contact        |Form validation working              |         |          |         |      |    |         |        |
|16      |Contact        |Environmental variables displayed    |         |          |         |      |    |         |        |
|17      |Contact        |Success template rendering correctly |         |          |         |      |    |         |        |
|18      |Contact        |Email backend working                |         |          |         |      |    |         |        |
|19      |Contact        |Email templates working              |         |          |         |      |    |         |        |
|20      |Contact        |Internal & External Mails sent       |         |          |         |      |    |         |        |
|21      |Contact        |Toasts working                       |         |          |         |      |    |         |        |
|22      |Categories     |View Secure                          |N/A      |N/A       |         |      |    |         |        |
|23      |Categories     |Rendering correctly at breakpoints   |N/A      |N/A       |         |      |    |         |        |
|24      |Categories     |Anchor/Button elements working       |N/A      |N/A       |         |      |    |         |        |
|25      |Categories     |Categories jinga templates working   |N/A      |N/A       |         |      |    |         |        |
|26      |Categories     |Add, Edit and Delete links working   |N/A      |N/A       |         |      |    |         |        |
|27      |Categories     |Delete Modal Working                 |N/A      |N/A       |         |      |    |         |        |
|28      |Categories     |Delete view working                  |N/A      |N/A       |         |      |    |         |        |
|29      |Categories     |Delete view secure                   |N/A      |N/A       |         |      |    |         |        |
|30      |Categories     |Toasts working                       |N/A      |N/A       |         |      |    |         |        |
|31      |Add Category   |view secure                          |N/A      |N/A       |         |      |    |         |        |
|32      |Add Category   |view and url working                 |N/A      |N/A       |         |      |    |         |        |
|33      |Add Category   |Template responsive                  |N/A      |N/A       |         |      |    |         |        |
|34      |Add Category   |Form validation working              |N/A      |N/A       |         |      |    |         |        |
|35      |Add Category   |Defensive logic working              |N/A      |N/A       |         |      |    |         |        |
|36      |Add Category   |Toasts working                       |N/A      |N/A       |         |      |    |         |        |
|37      |Add Category   |Automatic update of New Offers Nav   |         |          |         |      |    |         |        |
|38      |Add Category   |New Offer nav filter correct         |         |          |         |      |    |         |        |
|39      |Edit Category  |view secure                          |N/A      |N/A       |         |      |    |         |        |
|40      |Edit Category  |view and url working                 |N/A      |N/A       |         |      |    |         |        |
|41      |Edit Category  |Template responsive                  |N/A      |N/A       |         |      |    |         |        |
|42      |Edit Category  |Form validation working              |N/A      |N/A       |         |      |    |         |        |
|43      |Edit Category  |Defensive logic working              |N/A      |N/A       |         |      |    |         |        |
|44      |Edit Category  |Toasts working                       |N/A      |N/A       |         |      |    |         |        |
|45      |Products       |Anchor elements working              |         |          |         |      |    |         |        |
|46      |Products       |Filtering Working                    |         |          |         |      |    |         |        |
|47      |Products       |Filter counting working              |         |          |         |      |    |         |        |
|48      |Products       |Filter helper links working          |         |          |         |      |    |         |        |
|49      |Products       |Sorting  Working                     |         |          |         |      |    |         |        |
|50      |Products       |Top & Mobile Search inputs working   |         |          |         |      |    |         |        |
|51      |Products       |Top & Mobile Search responsive       |         |          |         |      |    |         |        |
|52      |Products       |Product lables & pricing  correct    |         |          |         |      |    |         |        |
|53      |Products       |Responsive rating working            |         |          |         |      |    |         |        |
|54      |Products       |Responsive Qty & Out of stock correct|         |          |         |      |    |         |        |
|55      |Products       |View Secure                          |         |          |         |      |    |         |        |
|56      |Products       |Edit and Delete links working        |N/A      |N/A       |         |      |    |         |        |
|57      |Products       |Image working for file or url        |         |          |         |      |    |         |        |
|58      |Products       |No image file working                |         |          |         |      |    |         |        |
|59      |Product Details|Select and redirect working          |         |          |         |      |    |         |        |
|60      |Product Details|Anchor elements working              |         |          |         |      |    |         |        |
|61      |Product Details|Carousel working                     |         |          |         |      |    |         |        |
|62      |Product Details|Tab Nav working                      |         |          |         |      |    |         |        |
|63      |Product Details|Responsive rating working            |         |          |         |      |    |         |        |
|64      |Product Details|Responsive Qty & Out of stock correct|         |          |         |      |    |         |        |
|65      |Product Details|Product lables & pricing  correct    |         |          |         |      |    |         |        |
|66      |Product Details|Quantity & Out of stock correct      |         |          |         |      |    |         |        |
|67      |Product Details|View Secure                          |         |          |         |      |    |         |        |
|68      |Product Details|Edit and Delete links working        |N/A      |N/A       |         |      |    |         |        |
|69      |Product Details|Image working for file or url        |         |          |         |      |    |         |        |
|70      |Product Details|No image file working                |         |          |         |      |    |         |        |
|71      |Product Details|Select and redirect working          |         |          |         |      |    |         |        |
|72      |Product Details|Add Button and qty working           |         |          |         |      |    |         |        |
|73      |Product Details|Sizes Options working                |         |          |         |      |    |         |        |
|74      |Product Details|Toasts working                       |         |          |         |      |    |         |        |
|75      |Add Product    |view secure                          |         |          |         |      |    |         |        |
|76      |Add Product    |view and url working                 |N/A      |N/A       |         |      |    |         |        |
|77      |Add Product    |Template responsive                  |N/A      |N/A       |         |      |    |         |        |
|78      |Add Product    |Form validation working              |N/A      |N/A       |         |      |    |         |        |
|79      |Add Product    |Defensive logic working              |N/A      |N/A       |         |      |    |         |        |
|80      |Add Product    |Toasts working                       |N/A      |N/A       |         |      |    |         |        |
|81      |Edit Product   |view secure                          |         |          |         |      |    |         |        |
|82      |Edit Product   |view and url working                 |N/A      |N/A       |         |      |    |         |        |
|83      |Edit Product   |Template responsive                  |N/A      |N/A       |         |      |    |         |        |
|84      |Edit Product   |Form validation working              |N/A      |N/A       |         |      |    |         |        |
|85      |Edit Product   |Defensive logic working              |N/A      |N/A       |         |      |    |         |        |
|86      |Edit Product   |Toasts working                       |N/A      |N/A       |         |      |    |         |        |
|87      |Shopping Bag   |view and url working                 |         |          |         |      |    |         |        |
|88      |Shopping Bag   |Template responsive                  |         |          |         |      |    |         |        |
|89      |Shopping Bag   |Defensive logic working              |         |          |         |      |    |         |        |
|90      |Shopping Bag   |Update & Delete working              |         |          |         |      |    |         |        |
|91      |Shopping Bag   |Image working for file or url        |         |          |         |      |    |         |        |
|92      |Shopping Bag   |No image file working                |         |          |         |      |    |         |        |
|93      |Shopping Bag   |Sizes Options working                |         |          |         |      |    |         |        |
|94      |Shopping Bag   |Subtotals and Grand Total working    |         |          |         |      |    |         |        |
|95      |Shopping Bag   |Link to checkout and return working  |         |          |         |      |    |         |        |
|96      |Shopping Bag   |Form validation working              |         |          |         |      |    |         |        |
|97      |Secure Checkout|view and url working                 |         |          |         |      |    |         |        |
|98      |Secure Checkout|Template responsive                  |         |          |         |      |    |         |        |
|99      |Secure Checkout|Defensive logic working              |         |          |         |      |    |         |        |
|100     |Secure Checkout|Form validation working              |         |          |         |      |    |         |        |
|101     |Secure Checkout|Profile Feedback working             |         |          |         |      |    |         |        |
|102     |Secure Checkout|Order Summary Working                |         |          |         |      |    |         |        |
|103     |Secure Checkout|Stripe Working                       |         |          |         |      |    |         |        |
|104     |Secure Checkout|Webhooks working                     |         |          |         |      |    |         |        |
|105     |Secure Checkout|Email Confirmation working           |         |          |         |      |    |         |        |
|106     |Allauth        |Sign In/Out views working            |         |          |         |      |    |         |        |
|107     |Allauth        |Register, Reset views working        |         |          |         |      |    |         |        |
|108     |Allauth        |Email Confirmation working           |         |          |         |      |    |         |        |
|109     |Allauth        |Templates responsive                 |         |          |         |      |    |         |        |
|110     |Allauth        |Templates per site Theme             |         |          |         |      |    |         |        |
|111     |My Profile     |View working                         |N/A      |          |         |      |    |         |        |
|112     |My Profile     |Template responsive                  |N/A      |          |         |      |    |         |        |
|113     |My Profile     |Order History Working                |N/A      |          |         |      |    |         |        |
|114     |My Profile     |Feedback with checkout working       |N/A      |          |         |      |    |         |        |
|115     |My Profile     |Form validation working              |N/A      |          |         |      |    |         |        |

***

[Back to Contents](#table-of-contents)

## Post Production Bugs Found


***
[Back to Contents](#table-of-contents)

## Pre Production Testing
- During cretaion of Add Category view, validated that category name did not already exist through use of form cleaned_data() method and multiple iterations of add task. cleaned_data() methid used to standardise form iputs to dictionary before check.
Also confirmed Boolean True attribute assigned correctly to new field upon creation through use of django admin.
- When testing the CRUD functionality for the categories app I found an issue with the delete view after introducing a modal confirmation window.
the same category id was being targetted regardless if the catergory selected.  This was resolved through use of template logic to uniquely identify each modal id.
- When wiring up toasts to the manage category crud functionality I decided to add in additional backend validation to prevent adding of category name if already exists in database. In addition to this I also set name field to readonly and validation against friendly name on edit category view.
Toasts were tested against form validation for display, add, edit and delete operations.
- Spent a significant amount of time over past two days validating, development and heroku environments to ensure the backend email functionality was wired up correctly before commencing final steps with contact app.  Having cleaned up the os environment in the settings.py file I tied myself up in knots for a couple of hours by accidentally changing one the develepment variables to a string.  Knew where the problem had to lie but couldn't make the wood from the trees when looking at the code. Quotation marks ehh!
- Contact app form submission was tested for both internal external comms to development console level the external email backend.
I also validated insertion of appropriate variable details in conact and confirm email text templates.
Attempted to integtrate the methodology described in the Stripe Webhooks email tutorials with that of this [Online Django Email/Contact Form Tutorial](https://learndjango.com/tutorials/django-email-contact-form).
- When testing the tabbed views I found it very difficult to develop the logic to approriately render the tabs with assoicated sub menu searches results while also highlighting the appropriate tab.  The plan is to complete the logic for all products and then move onto the Men, Women and Kids tab views.  At this point in time I think teh simplest way to approach it is to generate independent views and templates for the tob level categories.  
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

* When testing the add category functionality I initially had difficulty loading the newly added categories to teh main-nav template because it was part of the base template infrastructure, needed to be available for all apps and didn't have its own view.  So needed a way to pass data from the backend through to the front end without explicitly being called by an app.  I found a very useful [stack overflow](https://stackoverflow.com/questions/34902707/how-can-i-pass-data-to-django-layouts-like-base-html-without-having-to-provi) link explaining that it needed to be created as a user generated context processor and then loaded to the of base infrastructure via settings.py under TEMPLATE options per below.
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
* Profile order history update testing clean for registered users and working when stripe element form submit is diabled proving out webhook redundancy.  Link between indivual history order  and checkout view also testing clean.
* Order Email confirmation testing cleanly to both console and email backend.
* Production site wired up to AWS S3. Static files and Images uploading and displaying correctly.  
***

[Back to Contents](#table-of-contents)

## Pre Production Bugs Found
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
- Encountered a problem when trying to migrate Products models with categories models. Receiving following error.
products.Product.category: (fields.E300) Field defines a relation with model 'Category', which is either not installed, or is abstract.
Fix was found on Slack.  Even though the models were imported the foreignkey model name still needed to be prefixed with app name i.e. categories.Category before the system would make the relationship.
- Had issue rendering no_image using {{ MEDIA_URL }} template prefix.  Resolve was to include "django.template.context_processors.media" in TEMPLATES object of settings.py 
- When adding search for subcategory name to products query function it produced following error:
Related Field got invalid lookup: icontains
I found through this [stackoverflow URL](https://stackoverflow.com/questions/11754877/troubleshooting-related-field-has-invalid-lookup-icontains) that this was because subcategory is a foreign key in teh products model.
To resolve this I had to add the foreign key field with a search fields option in the ProductAdmin model 
```
search_fields = ['subcategory__name']
```
Then explicity call out the name in query logic in the products view:
```
queries = Q(name__icontains=query) | Q(summary__icontains=query) | Q(subcategory__name__icontains=query)
```
* When adding the code to render the image widget more cleanly I found it difficult rendering the two crispy-form image widgets as a pair of side-by-side bootstrap col-6 divs.
Have read several articles and tried several crispy forms helpers and widget tweaker addons but have been unable to resolve completeely.  At present the divs are both col-6 divs but they are stacking as opposes to inline. Will need to come back to this later.
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
* The second occurs only if the bag form updated without changing the entry.  It therefore posts the qunatity as an empty string.  The view then fails because it is expecting integer value.
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

