from django.contrib import admin
from .models import Restaurant, Reviewer, Type, Review

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Reviewer)
admin.site.register(Type)
admin.site.register(Review)
