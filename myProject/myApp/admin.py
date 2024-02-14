from django.contrib import admin

from myApp.models import *


class custom_User_Display(admin.ModelAdmin):

    list_display=['display_name','user_type']

admin.site.register(customUser,custom_User_Display)
admin.site.register(JobModel)


# Register your models here.
