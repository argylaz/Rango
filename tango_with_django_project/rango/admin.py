from django.contrib import admin
from rango.models import Category, Page

# Registering the Category and Page models with the admin interface
admin.site.register(Category)

# New class to customise the admin interface
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

# Register new class to update interface
admin.site.register(Page, PageAdmin)

