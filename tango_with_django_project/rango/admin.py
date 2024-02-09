from django.contrib import admin
from rango.models import Category, Page

# New class to automatically fill n slug field when a new category is created
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# New class to customise the admin interface
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

# Update the registration to include this customised interface
admin.site.register(Category, CategoryAdmin)

# Register Category and Page models with the admin interface
admin.site.register(Page, PageAdmin)

