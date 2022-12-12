from django import forms
from .models import Type, Restaurant, Reviewer, Review
 #hiii
class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = '__all__'

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