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

A live demo can be found [here]().

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

-wireframes-


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
