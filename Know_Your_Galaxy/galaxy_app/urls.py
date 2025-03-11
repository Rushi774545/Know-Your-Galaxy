from django.contrib import admin
from django.urls import path , include
from galaxy_app import views

urlpatterns = [
    path("", views.index , name='home'),
    path("playgames", views.playGames , name='playgames'),
    path("books",views.books,name='books'),
    path("spaceworks" ,views.spaceworks,name="spaceworks"),
    path("Review" ,views.review,name="review")

]