from django.contrib import admin

# Register your models here.

from pages.models import Customer, Town, Knowledge, Category

class CustomerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Customer,CustomerAdmin)




class TownAdmin(admin.ModelAdmin):
    pass


admin.site.register(Town,TownAdmin)


class KnowledgeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Knowledge,KnowledgeAdmin)


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category,CategoryAdmin)
