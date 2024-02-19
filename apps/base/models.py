from django.db import models

from django_resized.forms import ResizedImageField 
from ckeditor.fields import RichTextField
# Create your models here.
class User(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to="user_image/",
        verbose_name="Cуроту",
        blank = True, null = True
    )
    name = models.CharField(
        max_length = 255,
        verbose_name = "Аты жону"
    )
    descriptions = RichTextField(
        verbose_name="Кыскача маалымат",
        blank=True,null=True
    )
    resume = models.ImageField(
        upload_to="resume/",
        verbose_name="Резюме"
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "1) Мугали жонундо кыскача маалыматтар"
        verbose_name = "1) Мугали жонундо кыскача маалымат"
    

class Header(models.Model):
    header_one = models.FileField(
        upload_to="header",
        verbose_name="Биринчи"
    )
    header_two = models.FileField(
        upload_to="header",
        verbose_name="Экинчи"
    )
    header_three = models.FileField(
        upload_to="header",
        verbose_name="Учунчу"
    )
    header_four = models.FileField(
        upload_to="header",
        verbose_name="Тортунчу"
    )      
    header_five = models.FileField(
        upload_to="header",
        verbose_name="Бешинчи"
    )
    header_six = models.FileField(
        upload_to="header",
        verbose_name="Шесть"
    )
    header_seven = models.FileField(
        upload_to="header",
        verbose_name="Семь"
    )

    class Meta:
        verbose_name_plural = "1) Документтер"
        verbose_name = "1) Документ"
    