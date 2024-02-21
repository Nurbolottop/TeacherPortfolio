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
    resume = models.FileField(
        upload_to="resume/",
        verbose_name="Резюме"
    )
    name = models.CharField(
        max_length = 255,
        verbose_name = "Аты жону"
    )
    phone = models.CharField(
        max_length = 255,
        verbose_name = "Телефонный номер"
    )
    email = models.EmailField(
        verbose_name = "Почта"
    )
    locations = models.CharField(
        max_length = 255,
        verbose_name = "Адресс"
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
    

class Header(models.Model):
    header_one = models.FileField(
        upload_to="header/",
        verbose_name="Мугалим жөнүндө жалпы маалымат ",
        blank = True,null = True
    )
    header_two = models.URLField(
        verbose_name="Мугалимдин ишмердүүлүгү (презентация)",
        blank = True,null = True
    )
    header_three = models.FileField(
        upload_to="header/",
        verbose_name="Укуктук ченемдик актылар",
        blank = True,null = True
    )
    header_four = models.FileField(
        upload_to="header/",
        verbose_name="Билим берүү стандарты",
        blank = True,null = True
    )      
    header_five = models.FileField(
        upload_to="header/",
        verbose_name="Өнүктүрүү планы",
        blank = True,null = True
    )
    header_six = models.FileField(
        upload_to="header/",
        verbose_name="Корсотмо куралдар",
        blank = True,null = True
    )
    header_seven = models.FileField(
        upload_to="header/",
        verbose_name="Брейринг иштелмелери",
        blank = True,null = True
    )
    
    class Meta:
        verbose_name_plural = "1) Документтер"
        verbose_name = "1) Документ"
    