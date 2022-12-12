from unicodedata import name
from django.urls import path

from .views import indexPageView, addReviewView, editReviewView, deleteReviewView, restaurantDetailsView, updateRestaurantView
from .views import addReviewerView, createRestaurantView
from .views import showSingleReviewerPageView, updateReviewersPageView, showAllReviewersPageView
from .views import deleteReviewerView


urlpatterns = [
    path('', indexPageView, name="index"),
    path('create/', addReviewView, name="create"),
    path('update/<int:reviewID>/', editReviewView, name="update"),
    path('restDetails/<int:restID>/', restaurantDetailsView, name='restaurantDetails'),
    path('updateRestaurant/<int:restID>/', updateRestaurantView, name='updateRestaurant'),
    path('delete/<int:reviewID>/', deleteReviewView, name="delete"),
    path('addReviewer/', addReviewerView, name="addReviewer"),
    path('createRestaurant/', createRestaurantView, name="createRestaurantView"),
    path("showSingleReviewer/<int:id>/", showSingleReviewerPageView, name="showSingleReviewer"),
    path("updateReviewers/", updateReviewersPageView, name="updateCust"),
    path("showAllReviewers/", showAllReviewersPageView, name="allReviewers"),
    path('deleteReviewer/<int:reviewerID>/', deleteReviewerView, name="deleteReviewer"),
]