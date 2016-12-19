# mail-dir

maildir
A python (Django based) application which stores names and email addresses in a SQLite database. 
	a) The home page (welcome page) is located at http://localhost:8000/ 
	- this page has links to list and add pages
	b) List page displays all stored names / email address. located at http://localhost:8000/list
	c) Add page displays a form that Adds  name / email addresses to the database. Located at http://localhost:8000/add
	This page validates input and shows errors(if any).

# Dependencies
This script relies on the Django framework libraries/modules
The framework can be installed with pip
	pip install Django

# Usage
If running on a PC
Pull the repository into a folder on your platform.
Run the command 'python manage.py runserver' in a command line shell from the projects folder to start the server.
Visit http://localhost:8000 or http://127.0.0.1:8000 to access the application index page.

# Database
The sqlite database  model is created as thus:
first_name = models.CharField(max_length=100)
last_name = models.CharField(max_length=100)
email = models.EmailField(max_length=100)
    
# Security
XSS Prevention: 
No html was stored in the db as the form input are validated and cleaned.
The application properly escapes user-provided data before it is placed on the page.
The Django template in use ensures expressions are HTML-escaped, and it'll automatically escape data that's dynamically inserted into the template.
The use of mark_safe and safe tags in the templats were avoided.

Sql Injection: 
By using Django’s querysets and(ORM) layer as against writing RawSQL queries and making extra calls, the resulting SQL were  properly escaped by the sqlite3 database driver used.
The use of is_valid() helps to generate validated form data in its cleaned_data attribute. 

CSRF: 
The CSRF middleware is left active in the MIDDLEWARE setting.
The CSRF module is enabled for All views (globally).
In the template that use a POST form, csrf_tokens tag are inserted inside the <form> element .
In the corresponding view functions of the form action pages, the RequestContext is used to render the response so that {% csrf_token %} works properly.
The usage of render() function, protects the app since it uses RequestContext.

The X-Frame-Options header is left at its default value of  SAMEORIGIN for every outgoing HttpResponse.
This way, if the response contains the header with a value of SAMEORIGIN then the browser will only load the resource in a frame if the request originated from application.
			
The 'django.middleware.clickjacking.XFrameOptionsMiddleware' was set in MIDDLEWARE:This sets the same X-Frame-Options value for all responses in the application.

Optional use of the package django-secure, can help to configure and check some security aspects such as ssl.

#Assumptions 
Debug is turned ON on purpose. This is to enable Django handle static files (css) for the app.  In a production scenario, the web server (Apache, Nginx) will be made to take care of that. With debug turned on, the 404 error page maks use of the default Django template.
Duplicate records are allowed to be inserted into the database
The records on the list page appears in descending order.
