from django.contrib import admin
from .models import Article, Category,Book,SubCategory,CommentStatus,Comment,Feedback,FeedbackCategories
# Register your models here.


class Articls_Admin(admin.ModelAdmin):
    list_filter = ("english_title", "publish_time","arabic_title",)
    list_display = ('english_title', "publish_time","id",)
    search_fields = ['english_title']

class Categories_Admin(admin.ModelAdmin):
    prepopulated_fields = {'Category_slug': ('Category_English_name',), }
    list_filter = ("Category_English_name", "created",)
    list_display = ('Category_English_name', "created","id",)
    search_fields = ['Category_English_name']


class SubCategories_Admin(admin.ModelAdmin):
    prepopulated_fields = {'SubCategory_slug': ('SubCategory_English_name',), }
    list_filter = ("SubCategory_English_name", "created",)
    list_display = ('SubCategory_English_name', "created","id",)
    search_fields = ['SubCategory_English_name']

class Book_Admin(admin.ModelAdmin):
    list_filter = ("title", "created",)
    list_display = ('title', "created","id",)




class Comment_admin(admin.ModelAdmin):
    list_filter = ("status",)
    list_display = ('user',"article","status")



class CommentStatus_admin(admin.ModelAdmin):
    list_filter = ("status_en",)
    list_display = ('status_en',"id",)


class CommentStatus_admin(admin.ModelAdmin):
    list_filter = ("status_en",)
    list_display = ('status_en',"id",)


class Feedback_admin(admin.ModelAdmin):
    list_filter = ("title",)
    list_display = ('title',"id",)

class FeedbackCategories_admin(admin.ModelAdmin):
    list_filter = ("category_en",)
    list_display = ('category_en',"id",)


admin.site.register(Feedback,Feedback_admin)
admin.site.register(FeedbackCategories,FeedbackCategories_admin)

admin.site.register(Comment,Comment_admin)
admin.site.register(CommentStatus,CommentStatus_admin)
admin.site.register(Book,Book_Admin)
admin.site.register(Article,Articls_Admin)
admin.site.register(Category,Categories_Admin)
admin.site.register(SubCategory,SubCategories_Admin)

