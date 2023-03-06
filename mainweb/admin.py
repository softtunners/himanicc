from django.contrib import admin
from .models import *
# Register your models here.



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_title',)
    icon_name = 'apps'

# class CommentAdmin(admin.ModelAdmin):
#     list_display =('post','username')
class ContactAdmin(admin.ModelAdmin):
    list_display=("fname","email","number","date")
    icon_name='contact_phone'


class SubcribeUsersAdmin(admin.ModelAdmin):
    list_display=("email","date")
    icon_name='contact_mail'

class ScrapBookImgAdmin(admin.ModelAdmin):
    list_display=("name",'date',)
    icon_name='images'

class IpModelAdmin(admin.ModelAdmin):
    list_display=("ip","date")
    icon_name='person'


class BlogCommentAdmin(admin.ModelAdmin):
    list_display=("name","email","timestamp")
    icon_name='send'

class PostAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','post_date',)
    search_fields = ('tags',)
    list_filter= ('category','title',)
    list_per_page = 8
    icon_name='add_to_photos'

class JobsPositionsAdmin(admin.ModelAdmin):
    list_display=("job_title","location")
    icon_name='mail'

class CandidatesAdmin(admin.ModelAdmin):
    list_display=("job_title","name","email")
    icon_name='person'

admin.site.register(Scrapbook)
admin.site.register(ScrapBookImg,ScrapBookImgAdmin)
admin.site.register(JobsPositions,JobsPositionsAdmin)
admin.site.register(Candidates,CandidatesAdmin)


admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(IpModel,IpModelAdmin)
admin.site.register(BlogComment,BlogCommentAdmin)
admin.site.register(SubcribeUsers,SubcribeUsersAdmin)

