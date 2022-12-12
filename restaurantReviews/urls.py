from unicodedata import name
from django.urls import path
from .views import indexPageView, addReviewView, editReviewView, deleteReviewView, addReviewerView, createRestaurantView
from .views import showSingleReviewerPageView, updateReviewersPageView

urlpatterns = [
    path('', indexPageView, name="index"),
    path('create/', addReviewView, name="create"),
    path('update/<int:reviewID>/', editReviewView, name="update"),
    path('delete/<int:reviewID>/', deleteReviewView, name="delete"),



    path('addReviewer/', addReviewerView, name="addReviewer"),

    path('createRestaurant/', createRestaurantView, name="createRestaurantView"),

    path("showReviewers/<int:id>/", showSingleReviewerPageView, name="showSingleReviewer"),
    path("updateReviewers/", updateReviewersPageView, name="updateCust"),

]