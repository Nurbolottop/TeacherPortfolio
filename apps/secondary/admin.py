from django.contrib import admin
from apps.secondary import models as secondarys

# Register your models here.
class SettingsFilterAdmin(admin.ModelAdmin):
    # list_filter = ('iamge', )
    # list_display = ('iamge', )
    search_fields = ('iamge', )

admin.site.register(secondarys.Settings, SettingsFilterAdmin)