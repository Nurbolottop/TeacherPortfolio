from django.db import models
from django_resized.forms import ResizedImageField 
from ckeditor.fields import RichTextField
# Create your models here.
class Settings(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to="user_image/",
        verbose_name="Логотип",
        blank = True, null = True
    )

    class Meta:
        verbose_name = "1) Сайттын параметрлери"
        verbose_name_plural = "1) Сайттын параметрлери"
        