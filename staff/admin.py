from django.contrib import admin
from .models import Staff

class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone')  # Remove any ellipsis and make sure these are valid fields

admin.site.register(Staff, StaffAdmin)
