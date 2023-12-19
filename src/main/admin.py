from django.contrib import admin

from src.main.models import Dog


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name',)
