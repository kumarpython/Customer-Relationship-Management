from django.contrib import admin
from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ['fname','email','dob','created']
    list_filter = ['gender','source','country','agent','status']

