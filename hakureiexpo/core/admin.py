from django.contrib import admin

from .models import Submission, Circle, User

# Register your models here.

admin.site.register(User)
admin.site.register(Circle)
admin.site.register(Submission)
