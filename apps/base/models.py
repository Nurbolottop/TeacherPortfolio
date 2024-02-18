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
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "1) Мугали жонундо кыскача маалыматтар"
        verbose_name = "1) Мугали жонундо кыскача маалымат"
    
    
