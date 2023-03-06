from django.contrib import admin
from .models import *
from django.http import HttpResponse
import csv

def export_selected_users_to_excel(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Surname', 'Email', 'Phone No', 'Website', 'Company Name', 'Business Details'])

    for user in queryset:
        writer.writerow([user.name, user.sname, user.email, user.phone_no, user.website, user.company_name, user.business_details])

    return response

export_selected_users_to_excel.short_description = "Export selected users to Excel"


class userinfoAdmin(admin.ModelAdmin):
    list_filter = ['gid', 'created','group_name']

    list_display = ('name','sname','email','gid','mail_sent','created')
    icon_name = 'account_box'
    actions = [export_selected_users_to_excel]

class ExcelAdmin(admin.ModelAdmin):
    list_display=('file','gid','date')
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