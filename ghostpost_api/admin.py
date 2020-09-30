from django.contrib import admin
from . import models
# Register your models here.
class BoastsRoastAdmin(admin.ModelAdmin):
    list_display = ('id','post_body')
admin.site.register(models.BoastsRoastsModel,BoastsRoastAdmin)