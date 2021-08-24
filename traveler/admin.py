from django.contrib import admin
from django.core.exceptions import ImproperlyConfigured
from traveler import models
from django.utils.html import format_html

class PlaceAdminPanel(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" height="40px" width="40px style="border-radius:40px" />'.format(object.image_main.url))
    thumbnail.short_description="place"
    list_display=('id','thumbnail','name','description','price')
    list_display_links=('id','thumbnail','name')
    list_editable=('description','price')
    search_fields=('id','name')

# Register your models here.
admin.site.register(models.Place,PlaceAdminPanel)
