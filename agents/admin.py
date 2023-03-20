from django.contrib import admin
from .models import Agent


@admin.register(Agent)
class LeadAdmin(admin.ModelAdmin):
    list_display = ['fname','email','dob','city', 'country']
    list_filter = ['gender','country']
# Register your models here.
