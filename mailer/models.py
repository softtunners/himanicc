from django.db import models
from ckeditor.fields import RichTextField
import uuid

# Create your models here.

class Groups(models.Model):
    group_name = models.CharField(max_length=25)
    def __str__(self) -> str:
        return self.group_name
    class Meta:
        verbose_name = "All Groups List"
        verbose_name_plural = "All Groups List" 


    


class Excel_file(models.Model):
    group_name = models.ForeignKey(Groups,on_delete=models.CASCADE)
    gid = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    file= models.FileField(upload_to='excel_file/')
    date = models.DateField(auto_now=True)

class userinfo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    gid = models.ForeignKey(Excel_file,on_delete=models.CASCADE)
    group_name = models.ForeignKey(Groups,on_delete=models.CASCADE)    
    name =models.CharField(max_length=25)
    sname = models.CharField(max_length=25)
    email = models.EmailField()
    phone_no = models.IntegerField()
    website = models.URLField()
    company_name = models.CharField(max_length=25)
    business_details = models.TextField()
    mail_sent = models.BooleanField(default=False)
    class Meta:
        verbose_name = "All Users"
        verbose_name_plural = "All Users" 
        
class EMail_container(models.Model):
    group_name=models.ForeignKey(Groups,on_delete=models.CASCADE)
    subject =models.TextField()
    message = RichTextField()

    def __str__(self) -> str:
        return self.subject + ' - ' + str(self.group_name.group_name) 
    class Meta:
        verbose_name = "Email Content"
        verbose_name_plural = "Email Content"  
