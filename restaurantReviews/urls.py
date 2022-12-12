from unicodedata import name
from django.urls import path

from .views import indexPageView, addReviewView, editReviewView, deleteReviewView, restaurantDetailsView, updateRestaurantView
from .views import addReviewerView, createRestaurantView
from .views import showSingleReviewerPageView, updateReviewersPageView


urlpatterns = [
    path('', indexPageView, name="index"),
    path('create/', addReviewView, name="create"),
    path('update/<int:reviewID>/', editReviewView, name="update"),
    path('restDetails/<int:restID>/', restaurantDetailsView, name='restaurantDetails'),
    path('updateRestaurant/<int:restID>/', updateRestaurantView, name='updateRestaurant'),
    path('delete/<int:reviewID>/', deleteReviewView, name="delete"),
    path('addReviewer/', addReviewerView, name="addReviewer"),
    path('createRestaurant/', createRestaurantView, name="createRestaurantView"),

    path("showReviewers/<int:id>/", showSingleReviewerPageView, name="showSingleReviewer"),
    path("updateReviewers/", updateReviewersPageView, name="updateCust"),

]