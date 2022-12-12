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
    return render(request, 'restaurantReviews/index.html', context)

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
    form = RestaurantForm(instance=data)

    context = {
        'form' : form,
        'rest' : data
    }
    
    return render(request, 'restaurantReviews/updateRestaurant.html', context)




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


def createRestaurantView(request) :
    data = Restaurant.objects.all()
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
      form = RestaurantForm()
    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'restaurantReviews/addRestaurant.html', context)

def showSingleReviewerPageView(request, cust_id) :
    data = Reviewer.objects.get(id = cust_id)
    destinations =data.destinations.all()
    context = {
        "record" : data,
        "dest" : destinations
    }
    return render(request, 'restaurantReviews/editReviewer.html', context)

def updateReviewersPageView(request) :
    if request.method == 'POST':
        id = request.POST['id']
        
        reviewer = Reviewer.objects.get(id=id)

        reviewer.first_name = request.POST['first_name']
        reviewer.last_name = request.POST['last_name']

        reviewer.save()

    return indexPageView(request)
