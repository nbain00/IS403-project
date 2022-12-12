from django.contrib import admin
from .models import Restaurant, Reviewer, Review

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Reviewer)
admin.site.register(Review)
