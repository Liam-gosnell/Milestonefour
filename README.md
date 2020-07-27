# Milestone-Four

# DESIGNDROP
<p>Stream Four Project: Full Stack Frameworks with Django - Code Institute<p>

<p>This site is for a Graphic design Agency, DEISGNDROP. 
The main goal of this site was to make a system for the designers to upload/sell their work to customers, along with
showing the creators previous work as inspiration for companies that needed branding/services for their company.
This Django based site is perfect for any Design agency looking to promote their own brand. This is a A system for employees to be more efficient, 
and a system for customers to easily navigate through.
</p>

## Demo 

A live demo can be found [here](https://designdrop.herokuapp.com/).

# UX

<p>
To make the system/site as clear as possible to the end-user, a basic but modern, clean design has been implemented. 
Options are limited and the end-user will not be overloaded with options to do anything other than the bare minimum. 
The navigation bar, buttons, cart system and dashboard have been built and have an easy to understand logic, So that a user can 
use this site free of worry or confusion.
</p>

# User stories

With years of Graphic design experience, we have built a well-known form and work ethic in creating designs. 
We asked our customers from day to day what they would like to see in a sample and came up with the following points:

* As a user, I want to easily fill in the forms for a service request
* As a user, I want to upload my artwork fast and easy in the same system
* As a user, I want a secured overview of my order history (dashboard)
* As a user, I want the system to remember my cart, for if I want to make changes later
* As a user, I do not want to fill in my details every time, but do want to change them if needed
* As an employee, I want to know which service are required per order
* As an employee, I want to change the status of an order
* As an employee, I would like to edit and upload new artwork
* As an employee, I want to search all orders

## Strategy

<p>
The goal of the system is to make it as easy as possible to access, short and informative,
while striving for a simple and user-friendly design. Whether the person using the system is an employee/client,
it will be easily navigated and layed-out for optimum use.
</p>

## Scope

<p>
For customers, we wanted to provide them with an easy to understand system. 
This way, they would be able to request services: faster, easier and on their own, 
so our studio employees have more  time to produce the designs that are being ordered daily.
This system is perfect for DESIGNDROP employees.
</p>

## Structure

<p>
The system is structured to get the right information as quickly as possible. 
The order of the options provided are placed in a logic workflow while the design provided will use a messages 
bar that should be easy to understand and gives the customer a straight away no-nonsense feedback. 
The Our Work section shows completed projects for previous clients. 
The contact section is there for people who need to know more information about the agency.
</p>

## Skeleton

<p>By using Mockflow the following wireframes were created:</p>

![Wireframe pdf](https://raw.githubusercontent.com/Liam-gosnell/Milestonefour/master/wireframes/designdrop-main.pdf "About wireframe")


# Technologies

* Mockflow - To create a wireframe
* HTML - To create the basics
* CSS - To style and design
* JavaScript - The Interaction of the site
* Python - Programming language for logic of the site 
* Postgres - Opensource database to save the transactions, profile, and orders
* Django - Web framework in python
* Bootstrap - To make the design responsive and for layouts of cards
* Font Awesome - Easy icon access for the icons


## JavaScript Libraries

* jQuery - To improve input field feedback
* Stripe - For credit card transactions

## Python & Django Libraries

* pillow - Python Imaging Library
* Stripe - Credit card payments and transaction security
* boto3 - To connect to AWS for S3 bucket and other services
* django-allauth - Authentication, registration & account management
* django-countries - Provides country choices for use with forms for user profile
* django-phonenumber-field - A Django library which interfaces with python-phonenumbers to validate
* django-crispy-forms - Controls the rendering behaviour of Django forms


# Features 

<p>
This system is an e-commerce-based website with a simplistic but easy to understand build-up. 
Providing the user with 2 call-to-action buttons, a choice can be made in seconds. The services are only one click away and are 
available by the click of ethier the services button in the navbar or the services button underneath the 'Team' on the 
home page. 
  The services page will show all the available services that can be ordered. All the user has to do is find the service that will 
solve their problem.Once the user has decided, there is a button for more details, then a button to add to cart. The user can add the 
service to their cart but can only purchase the service if logged in. If the user is not logged in, they will be asked to register an 
account. An admin account is available for employees to, update service request, delete, and also add new services if needed.
 Users can add or delete services to their cart which will be saved in the backend right away.
     As a user logs out the cart will be remembered in the system to be finished later. When the customer checkout, 
     a secured payment can be made with credit card and the site admin will revieve the order for the project to be started by the DESIGNDROP team.
</p>


## Features Left to Implement

At a later stage I hope to add a section to the site where freelance graphic deisngers can upload their own work for people to request,
This would form relationships with the agency and more freelance clients. I would also like to add to the 'Our Work" section with a 
testimonial comment/submission section for clients to add their own experiences with the DESIGNDROP team.

# Testing

<p>
This system was tested across multiple screen sizes on Chrome, Safari, and Internet Explorer. 
To ensure compatibility and responsiveness it is also tested on a range of android devices such as Pixel XL2, surface duo, Moto G4. 
The system has been field-tested by friends and family. 
I have tested all the forms/links and all buttons on the site. Which gives the system a smooth, responive look and feel. 
</p>

<p>Throughout the process I continually manually tested the frontend, 
by saving my work in Gitpod and running it in Google Chrome. 
I used Chrome Developer Tools to ensure that my site was responsive and 
functioned in all screen sizes and that my styling was applied appropriately throughout.</p>

<p>I had several users log in and out of the website using all the functions of the website. </p>

<p>I have tested the website on:</p>

* Google Chrome
* Apple Safari
* Internet Explorer
* Mozilla Firefox

<h4>Devices</h4>

* Iphone X
* Iphone 8
* Iphone 6/7
* iPad 
* iPad Pro
* Pixel
* Pixel 2XL
* Galaxy Note 3
* Kindle fire XDH
* Galaxy s5

<p>
For testing the admin interface an admin test account has been created on the deployed version to Heroku. The logins are:
</p>

* Username: developer_liam
* Password: hello123456

<p>
The following tests have been used to ensure proper site functionality:
</p>

* [GTmetrix](https://gtmetrix.com/) - To test on website loading times.
* [W3C HTML Validator](https://validator.w3.org/) - This validator checks the mark-up validity of Web documents in HTML.
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) -  CSS Validator
* [Python Validator](https://extendsclass.com/python-tester.html) - Python Validator
* [JSLINT](https://www.jslint.com/) - JS Validator


# Bugs

## CSS

<p>
CSS written code is tested with the W3C CSS Validator. As it does not give any problems, 
the deployed version of the site does gives a couple of warnings and errors coming from Bootstrap and the Font Awesome animations Library.
</p>

## JavaScript

<p>
All javascript in this Website have been tested with JSLINT as listed above. There are no JavaScript erros in the deployed site.
</p>


# Deployment

<p>
he code of this system is hosted by using Heroku and Amazon S3, 
this code is deployed to GitHub directly from the master branch. 
The deployed site will update automatically upon new commits to the master branch. 
This code can be run locally or deployed to a live environment. Directions are based on deployment locally and to Heroku.
</p>

## Deployment requirements

* Gitpod - An environment to develop software
* Python3 - A programming language
* Pip - To get python installation packages
* Git - Version control for code source
* AWS_S3 - Web based cloud storage service
* Stripe - To securely collect credit card payments

## How to install DESIGNDROP

1. From your terminal enter git clone https://github.com/Liam-gosnell/Milestonefour to clone the project and download to your IDE

2. Set up your Virtual Environment Variables

* this can be done by creating folder named .venv to hold your variables and importing them into your app.py
* this can be done in your IDE bash terminal - e.g. cd .. to your root directory and type nano.bashrc and type in your important environment variables

3. You should now install the requirements by typing $ pip3 -r install requirements.txt

4. You will also have to create your own database to get full functionality from the project.

### How to Deploy your site

<p>I committed my code to GitHub at regular intervals. I am now using git more often, making sure to give detailed commit messages as I know it provides version control.</p>

1. In order to deploy the site to Heroku, you must create a Procfile and requirements.txt. These will tell Heroku how to run your app.

* To create a Procfile - echo web: python (your filename).py > Procfile
* To create a requirements.txt - pip3 freeze --local > requirements.txt

2. Next, log into Heroku and set up the remote.
 * heroku login
 * then enter details

3. You then need to setup your Heroku Enivronment Variables and you can do this in two ways, either through the terminal or by navigating to Heroku.

4. On navigating to the Heroku website, log in and select your app from the dashoboard.

5. Choose settings and click on 'Reveal Config Vars' and insert the environment variables that are essential for your project to run. For example,
   "IP - 0.0.0.0 PORT - 8080, STRIPE_SECRET_KEY , STRIPE_WH_KEY etc..

6. Set up the databases by running the following management command in your terminal:
    "python manage.py migrate"

7. Create a superuser so you can have access to the django admin by running the following command in your terminal:
    "python manage.py createsuperuser"

8. Now that the server is running, we need to add the required data into the database in the following order:
    1. "python manage.py loaddata itemtags.json"
    2. "python manage.py loaddata items.json"
    3. "python manage.py loaddata portfolio.json"

9. Finally start your server by running the following management command in the terminal:
    "python manage.py runserver" - If everything went correctly the terminal will provide a message telling that the development server is running at a provided URL mostly
    PORT 8000.

# Heroku deployment

To run this application in a cloud-based environment, you can deploy the code to Heroku. 
This section assumes you have succeeded at running the application in your local environment first, as described above.

1. Login to Heroku and set up a new app with an unique name (NOTE: designdrop is already taken)

2. On the Resources tab, in the Add-ons field type Heroku Postgres select the Hobby Dev then click the Provision button.

3. After setting the Postgress database go back to the Settings tab and click Reveal Config Vars. Copy the values from your env.py file into Heroku. Make sure you load the following:
    "Key	Value
AWS_ACCESS_KEY_ID	<your_value>
AWS_SECRET_ACCESS_KEY	<your_value>
DATABASE_URL	<your_value>
SECRET_KEY	<your_value>
STRIPE_PUBLIC_KEY	<your_value>
STRIPE_SECRET_KEY	<your_value>
USE_AWS	<your_value>"

 - Grab the DATABASE_URL link from Heroku's Config Vars as we gonna need it later to migrate to the Heroku Postgres database.

4. Now that the database on Heroku is created the following rule needs to be added to the env.py file
 - os.environ.setdefault('DATABASE_URL', '<your postgres url grabbed from Heroku>') - Be assured to not share this URL with anybody.

5. Because this is a new database connection, the migrate command must be executed with the following command in your terminal:
    "python manage.py makemigrations"
    then - "python manage.py migrate"

6. Create the superuser for the postgres database so you can have access to the django admin.
 - python manage.py createsuperuser

7. Now we need to add the required data into the database in the following order:
    1. "python manage.py loaddata itemtags.json"
    2. "python manage.py loaddata items.json"
    3. "python manage.py loaddata portfolio.json"

8. With everything set push the code to a GitHub account of yourself(also turn on automatic deployments on heroku settings, to link with your github repo)
    " git push "
    "git push heroku master"

9. From the Heroku dashboard of your newly created application, click on the "Deploy" tab, then scroll down to the "Deployment method" section and select GitHub.

10. Use the GitHub link and type in the name of the repository and click the search button. Then connect the Heroku app to the desired GitHub repository.

11. On the Deployment Tab, scroll a bit further down to the "Manual Deploy" section, select the master branch then click "Deploy Branch".

12. Once your application is running, you may want to update the Deployment method from Manual to Automatic

13. From the Heroku dashboard select the Open app button on the top right. 

14. The deployed project is now ready to be used.


### Differences between Development and Deployed version

<p>I set the debug to false for deployment.</p>

# Credits 

## Content 
All the Portfolio descriptions and testimonials were written by Isobel Connors. All other content was written by me.

## Media 

The Team section images were taken from an example @ [bootstrap](https://getbootstrap.com/). All of the portfolio images I created myself 
on [Canva](https://www.canva.com/). The services images were taken from canva also. The images on the main page were taken from 
[Illustrations](https://illlustrations.co/).

## Acknowledgements

* [Django docs](https://www.djangoproject.com/).
* <p>Throughout this project I have sought support and guidance from Stack-Overflow, Code-Institue Slack Community, Tutors, W3Schools, CSS Tricks, YouTube videos.</p>
* <p>I used styles from Bulma. I have clearly marked the borrowed code in my CSS.</p>



