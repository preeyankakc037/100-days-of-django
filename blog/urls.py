from django.urls import path
from . import view

urlpatterns = [
 path('', view.post_list, name='home'),  # use post_list as the home page
    
]
