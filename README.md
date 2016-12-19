# mail-dir

maildir
A python (Django based) application which stores names and email addresses in a SQLite database. 
  a) The home page (welcome page) is located at http://localhost/ 
      - this page has links to list and add pages
  b) List page displays all stored names / email address. located at http://localhost/list
  c) Add page displays a form that Adds  name / email addresses to the database. Located at http://localhost/add
      This page validates input and shows errors(if any).

# Dependencies
This script relies on the Django framework libraries/modules
The framework can be installed with pip
	pip install Django
    
# Security
XSS Prevention: 
No html was stored in the db as the form input are validated and cleaned
The application properly escapes user-provided data before it is placed on the page.
The Django template in use ensures expressions are HTML-escaped, and it'll automatically escape data that's dynamically inserted into the template
The use of mark_safe and safe tags in the templats were avoided 

Sql Injection: 
By using Django’s querysets and(ORM) layer as against writing RawSQL queries and making extra calls, the resulting SQL were  properly escaped by the sqlite3 database driver used.
The us of is_valid() helps to generate validated form data in its cleaned_data attribute. 

CSRF: 
The CSRF middleware is left active in the MIDDLEWARE setting.
The CSRF module is enabled for All views (globally)
In the template that use a POST form, csrf_tokens tag are inserted inside the <form> element 
In the corresponding view functions of the form action pages, the RequestContext is used to render the response so that {% csrf_token %} works properly.
The usage of render() function, protects the app since it uses RequestContext.

The X-Frame-Options header is left at its default value of  SAMEORIGIN for every outgoing HttpResponse.
This way,if the response contains the header with a value of SAMEORIGIN then the browser will only load the resource in a frame if the request originated from application.
			
The  'django.middleware.clickjacking.XFrameOptionsMiddleware' was set in MIDDLEWARE:This sets the same X-Frame-Options value for all responses in the application

Optional use of the package django-secure, can help to configure and check some security aspects such as ssl.

#Assumptions 
multiple records allowed to be inserted into the database
The records on list page appears in descending order
