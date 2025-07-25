# Day 1 - Getting Started
In the first day:
1. I first install Django in my windows. 
2. Then I run this command 



>**COMMAND**=  django-admin startproject mysite .

what will this command do : This command will create a new django project called
> **mysite**-: inside this folder it sets up all the necessary files and structure to begin my web development journey.

>**manage.py**-: manage.py is your project-level tool that makes Django development easier. It connects your commands to Django's internal systems and ensures your settings are correctly loaded.
manage.py is the command-line utility script Django gives you to:

1.  Run your development server

2. Create apps

3. Apply migrations

4. Access the database shell

5. Perform admin tasks

Next Step:
> python manage.py startapp blog

I run this command in this directory: PS C:\Users\ASUS\Desktop\100_Days_of_Django\Day01_Getting_Started> 

>It creates a new Django app called blog — a self-contained unit where I'll write logic for a feature/module (like a blog, users, products, etc.).

>blog/

├── admin.py          # Admin panel settings

├── apps.py           # App config class (used in settings)

├── models.py         # Database models (tables)

├── views.py          # Python functions/classes that handle web requests

├── tests.py          # For testing your app

├── migrations/       # Stores DB migration files

│   └── __init__.py

└── __init__.py       # Tells Python this is a module



Then  the steps are:
> Step 1. In mysite setting.py in INSTALLED APPS add 'blog',

> Step 2. Replace code in  view.py in blogs folder with the given code 

> from django import httpResponse  
def home(request):  
return HttpResponse("Hello, this is the blog homepage!")


> Step 3. Create url.py in blogs folder 

>from django.urls import path     
from . import views     
urlpatterns = [
    path('', views.home, name='home'),    
]


> UPDATE MY SITE URLS  

> Add this Code:      
from django.urls import path, include  #inculde is needed 
    path('', include('blog.urls')),  #link to the blog app 

>FINALLY    
Running this->  python manage.py runserver 9000 #port of my choice 



> # REVIEW of the work that i did uptill now 

>Created a Django project ✅    
Made a new app ✅   
Wrote your first view ✅    
Connected it via URLs ✅    
Ran the local server ✅


> Then I make html templates and CSS/style files  and connect with the django app 


> # DAY 2: static templates and how they are connected 

Templates: How home inherits the property of base.html 
>{% extends 'blog/base.html'%}

## 🔹 Template Structure Overview

| **File**        | **Purpose**                                                        |
|------------------|---------------------------------------------------------------------|
| `base.html`      | Master layout (navbar, header/footer, CSS linking)                 |
| `home.html`      | Extends `base.html`, adds homepage-specific content                |
| `style.css`      | Static CSS file used to style HTML templates                       |
| `urls.py`        | Maps views to URLs (e.g., `'' -> home view -> home.html`)          |
| `views.py`       | Handles logic and renders `home.html` template                     |
| `settings.py`    | Tells Django where to find static and template files               |

---

## 🔹 Static Files: Connecting `style.css`

<Step 1: In `settings.py`>
```python
STATIC_URL = '/static/'

<Step 2: In base.html>

django
Copy
Edit
{% load static %}
<link rel="stylesheet" href="{% static 'blog/style.css' %}">
<Step 3: Project Directory Structure>

cpp
Copy
Edit
blog/
├── static/
│   └── blog/
│       └── style.css

🔹 Recap: How Everything Connects
✅ home.html inherits layout from base.html>
✅ base.html links style.css from the static folder>
✅ urls.py maps the homepage ('') to the view>
✅ views.py renders home.html>
✅ settings.py ensures Django can find templates and static files>

git add notes.md
