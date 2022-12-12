from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Type, Restaurant, Reviewer, Review
from .forms import TypeForm, RestaurantForm, ReviewerForm, ReviewForm

# Create your views here.
# Home page view
def indexPageView(request) :
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
    return render(request, 'restaurantReviews/index.html', context)

# Add review
def addReviewView(request) :
    return render(request, 'restaurantReviews/create.html')

# Edit a review
def editReviewView(request) :
    return render(request, 'restaurantReviews/update.html')

# Delete a review
def deleteReviewView(request) :
    return render(request, 'restaurantReviews/delete.html')