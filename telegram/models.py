from django.db import models

from Register_Login.models import Profile

# Create your models here.


class Category(models.Model):
    Category_English_name = models.CharField(max_length=250,unique = True,)
    Category_Arabic_name = models.CharField(max_length=250,unique = True,)
    Category_slug = models.SlugField(unique=True, db_index=True,blank=True,null = True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.Category_English_name)
        
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories"

class SubCategory(models.Model):
    SubCategory_English_name = models.CharField(max_length=250,unique = True,)
    SubCategory_Arabic_name = models.CharField(max_length=250,unique = True,)
    SubCategory_slug = models.SlugField(unique=True, db_index=True,blank=True,null = True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.SubCategory_English_name)
        
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "SubCategory"

class Article(models.Model):
    english_title =  models.CharField(max_length=100,blank= True, null = True)
    arabic_title = models.CharField(max_length=100 , blank= True, null = True)
    publish_time = models.DateTimeField(auto_now_add=True)
    visited_times = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null = True,)
    subcategory  =  models.ForeignKey(SubCategory, on_delete=models.CASCADE,blank=True,null = True,)
    img = models.ImageField(
        upload_to="Articles", blank=True,null = True )
    img_description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    reviewer_id = models.ForeignKey(Profile, on_delete=models.CASCADE,blank=True,null = True,)

    def __str__(self):
        return str(self.english_title)
        

    class Meta:
        verbose_name_plural = "Articles"




class Book(models.Model):
    title =  models.CharField(max_length=100,blank= True, null = True)
    image = models.ImageField(
        upload_to="Books", blank=True,null = True )
    description = models.TextField(blank=True)
    downloading_link =  models.CharField(max_length=100,blank= True, null = True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
        

    class Meta:
        verbose_name_plural = "Books"

class CommentStatus(models.Model):
    status_en = models.CharField(max_length=100,blank= True, null = True)
    status_ar = models.CharField(max_length=100,blank= True, null = True)
    def __str__(self):
        return str(self.status_en)
        
    class Meta:
        verbose_name_plural = "Comment Status"

class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE,blank=True,null = True,)
    status = models.ForeignKey(CommentStatus, on_delete=models.CASCADE,blank=True,null = True,)
    article = models.ForeignKey(Article, on_delete=models.CASCADE,blank=True,null = True,)
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.email)
        
    class Meta:
        verbose_name_plural = "Comments"



class FeedbackCategories(models.Model):
    category_en = models.CharField(max_length=50, null=True)
    category_ar = models.CharField(max_length=50, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.category_en)
        
    class Meta:
        verbose_name_plural = "FeedbackCategories"


class Feedback(models.Model):
    category = models.ForeignKey(FeedbackCategories, on_delete=models.CASCADE,blank=True,null = True,)
    title = models.CharField(max_length=50, null=True)
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
        
    class Meta:
        verbose_name_plural = "Feedbacks"