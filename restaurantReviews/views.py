from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Home page view
def indexPageView(request) :
    return render(request, 'restaurantReviews/index.html')

# View filtered database
def filterDatabaseView(request) :
    return render(request, 'restaurantReviews/index.html')

# Add review
def addReviewView(request) :
    return render(request, 'restaurantReviews/create.html')

# Edit a review
def editReviewView(request) :
    return render(request, 'restaurantReviews/update.html')

# Delete a review
def deleteReviewView(request) :
    return render(request, 'restaurantReviews/delete.html')