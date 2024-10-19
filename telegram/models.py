from django.db import models

# Create your models here.


class Category(models.Model):
    Category_English_name = models.CharField(max_length=250,unique = True,)
    Category_Arabic_name = models.CharField(max_length=250,unique = True,)
    Category_slug = models.SlugField(unique=True, db_index=True,blank=True,null = True)
    image = models.ImageField(
        upload_to="Categories", blank=True,null = True )
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.Category_English_name)
        
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories"


class Article(models.Model):
    english_title =  models.CharField(max_length=100,blank= True, null = True)
    arabic_title = models.CharField(max_length=100 , blank= True, null = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null = True,)
    subcategory  = models.CharField(max_length=100,blank= True, null = True)
    imgSrc = models.ImageField(
        upload_to="Categories", blank=True,null = True )
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.english_title)
        

    class Meta:
        verbose_name_plural = "Articles"