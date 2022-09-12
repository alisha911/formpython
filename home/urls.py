from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('',views.form,name="form"),
   path('edit',views.edit,name="edit"),
   path('show',views.show,name="show"),
   path('delete',views.delete,name="delete"),
]