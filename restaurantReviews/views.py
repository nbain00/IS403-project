from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Type, Restaurant, Reviewer, Review
from .forms import TypeForm, RestaurantForm, ReviewerForm, ReviewForm
# Create your views here.
# Home page view
def indexPageView(request) :
    restData = Restaurant.objects.all()
    reviewData = Review.objects.all()

    context = {
        'rest' : restData,
        'review' : reviewData
    }
    return render(request, 'restaurantReviews/index.html')

# Add review
def addReviewView(request) :
    data = Review.objects.all()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ReviewForm()
    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'restaurantReviews/create.html', context)

# Edit a review
def editReviewView(request) :
    return render(request, 'restaurantReviews/update.html')

# Delete a review
def deleteReviewView(request) :
    return render(request, 'restaurantReviews/delete.html')

# Add a Reviewer
def addReviewerView(request) :
    data = Reviewer.objects.all()
    if request.method == 'POST':
        form = ReviewerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ReviewerForm()
    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'restaurantReviews/addReviewer.html', context)