# Blog Redesign
You have a very simple Blog Application written in Django. PyCharm was the IDE used but you can use whatever IDE you want.

This is a functioning system with 4 templates you will restyle (view.html, create.html, create_comment.html, and edit.html)

We need you to style it to look like a commercial, production application.

## Specific Features:
- Interface and Forms need to be restyled to look like a production application. Choose a nice design for the interface and implement it, styling is important here.
- JavaScript Pagination of Blog Posts
- Truncation of Comments so they don't overtake the screen (allow comments to be made visible again as well, think of a blog, you can view all comments but they don't take up the whole page)
- Forms need JavaScript Form Validation for empty fields, and legnth of content input less than 5 characters
- Alter the navigation to work however you need
- JavaScript Modals for successful submission of posts, comments, and deletions
- JavaScript image slider on the "View Posts" page with overlaying text stating the current time with counting seconds, and the total number of posts submitted

## Django Information:

You need to install the requirements like so with the terminal from the directory with requirement.txt file in it:

```pip3 install -r requirements.txt```

Now run migrations:

```python manage.py migrate```

Now to run the server enter this command, then go to 127.0.0.1:8000 in your browser:

```python manage.py runserver 127.0.0.1:8000```



You will be working with Django here so we can see if you are able to understand the framework we are using in our company at a base level. Although not required as we have set the entire project up for you, you may want to go over some starters in the documentation before you begin to familarize yourself with what we are doing. There is also a link to the standard "Polls" App Django uses to teach beginners the ropes.

**Django Docs:** 

https://docs.djangoproject.com/en/2.2/

**Polls App (Starter Django App):**  

https://docs.djangoproject.com/en/2.2/intro/tutorial01/

We have already added `crispy-forms` and `django-widget-tweaks` to the project and they are loaded to each page so simply look up the documentation and implement them if you wish. Alternatively it is fine to implement a different pakckage if you feel the need, we want a nice design here.

**Crsipy-Forms:** 

https://django-crispy-forms.readthedocs.io/en/latest/index.html

**Django-Widget-Tweaks:** 

https://github.com/jazzband/django-widget-tweaks

Use any custom JQuery or CSS, or JQuery Packages/CSS frameworks you want to accomplish the task at hand. JQuery is already loaded in the base.html template

