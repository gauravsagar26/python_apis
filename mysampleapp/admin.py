from django.contrib import admin
from .models import UserPost
# Register your models here.


# Register your models here.
@admin.register(UserPost)
class DataAdmin(admin.ModelAdmin):
    pass