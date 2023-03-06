from django.contrib import admin
from .models import *


class userinfoAdmin(admin.ModelAdmin):
    list_display = ('name','sname','email','mail_sent','created')
    icon_name = 'account_box'

class ExcelAdmin(admin.ModelAdmin):
    list_display=('file','date')
    icon_name = 'file_upload'

class GroupsAdmin(admin.ModelAdmin):
    list_display=('id','group_name')
    icon_name="group_add"

class EmailContent(admin.ModelAdmin):
    list_display=('group_name','subject',)
    icon_name = 'email'

# Register your models here.
admin.site.register(Groups,GroupsAdmin)
admin.site.register(userinfo,userinfoAdmin)
admin.site.register(Excel_file,ExcelAdmin)
admin.site.register(EMail_container,EmailContent)