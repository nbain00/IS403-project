from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant, Review

# Create your views here.
# Home page view
def indexPageView(request) :
    restData = Restaurant.objects.all()
    reviewData = Review.objects.all()

    context = {
        'rest' : restData,
        'review' : reviewData
    }

    return render(request, 'restaurantReviews/index.html', context)

# Add review
def addReviewView(request) :
    return render(request, 'restaurantReviews/create.html')

# Edit a review
def editReviewView(request, reviewID) :
    return render(request, 'restaurantReviews/update.html')

# Delete a review
def deleteReviewView(request, reviewID) :
    data = Review.objects.get(id=reviewID)

    data.delete()   

    return indexPageView(request)

def restaurantDetailsView(request, restID) :
    data = Restaurant.objects.get(id=restID)

    context = {
        'rest' : data
    }

    return render(request, 'restaurantReviews/restaurantDetails.html', context)

def updateRestaurantView(request, restID) :
    data = Restaurant.objects.get(id=restID)

    context = {
        'rest' : data
    }
    
    return render(request, 'restaurantReviews/updateRestaurant.html', context)
