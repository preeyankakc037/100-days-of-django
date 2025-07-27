from django.db import models
#imports Django built-in tools to create database models,
#thinking of it like importing LEGO Blocks so we can start building our projects 



# setting up database structure model to store blog posts

class Post(models.Model): #creating a new table in the database named Post
 
 title=models.CharField(max_length=200) #this creates a column named title in your database
 description=models.TextField() #A long field for blog summary 
 created_at=models.DateTimeField(auto_now_add=True)

 def __str__(self):
    return self.title

# each blogs will have a title, a description and and datestamp at which it was created 