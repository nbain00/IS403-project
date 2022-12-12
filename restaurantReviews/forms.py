from django import forms
from .models import Restaurant, Reviewer, Review
 #hiii


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'

class ReviewerForm(forms.ModelForm):
    class Meta:
        model = Reviewer
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'