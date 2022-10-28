from unicodedata import name
from django.urls import path
from .views import indexPageView, filterDatabaseView, addReviewView, editReviewView, deleteReviewView

urlpatterns = [
    path('', indexPageView, name="index"),
    path('read/', filterDatabaseView, name="read"),
    path('create/', addReviewView, name="create"),
    path('update/', editReviewView, name="update"),
    path('delete/', deleteReviewView, name="delete"),
]