from django.contrib import admin
from .models import Article, Category
# Register your models here.


class Articls_Admin(admin.ModelAdmin):
    list_filter = ("english_title", "created",)
    list_display = ('english_title', "created","id",)
    search_fields = ['english_title']

class Categories_Admin(admin.ModelAdmin):
    prepopulated_fields = {'Category_slug': ('Category_English_name',), }
    list_filter = ("Category_English_name", "created",)
    list_display = ('Category_English_name', "created","id",)
    search_fields = ['Category_English_name']


admin.site.register(Article,Articls_Admin)
admin.site.register(Category,Categories_Admin)

