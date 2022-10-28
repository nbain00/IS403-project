from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Home page view
def indexPageView(request) :
    return HttpResponse('Welcome to Restaurant Reviews')

# View filtered database
def filterDatabaseView(request) :
    return HttpResponse('This is the page to view the data')

# Add review
def addReviewView(request) :
    return HttpResponse('This is the page to add a review')

# Edit a review
def editReviewView(request) :
    return HttpResponse('This is the page to edit a review')

# Delete a review
def deleteReviewView(request) :
    return HttpResponse('This is the page to delete a review')
