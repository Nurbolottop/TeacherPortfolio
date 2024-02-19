from django.contrib import admin
from django.contrib.auth.models import User, Group
from apps.base import models as bases

# Register your models here.
class UserFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', )
    search_fields = ('name', )

class HeaderFilterAdmin(admin.ModelAdmin):
    list_filter = ('header_one', )
    list_display = ('header_one', )
    search_fields = ('header_one', )

admin.site.register(bases.Header, HeaderFilterAdmin)
admin.site.register(bases.User, UserFilterAdmin)


admin.site.unregister(User)
admin.site.unregister(Group)
