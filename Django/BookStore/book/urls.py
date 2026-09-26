from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name="book-home"),
    path('about/',views.about,name="book-about"),
    path('book/<int:book_id>/',views.book_details,name="book-details")
]
