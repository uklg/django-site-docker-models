from django.contrib import admin

# Register your models here.

from pages.models import Customer

class CustomerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Customer,CustomerAdmin)
    
