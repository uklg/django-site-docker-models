from django.contrib import admin

# Register your models here.

from pages.models import Customer, Town

class CustomerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Customer,CustomerAdmin)




class TownAdmin(admin.ModelAdmin):
    pass


admin.site.register(Town,TownAdmin)
