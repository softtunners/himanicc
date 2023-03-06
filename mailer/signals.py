from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.db.models.signals import post_save
from django.dispatch import receiver
from mailer.models import *
import pandas as pd
from django.shortcuts import get_object_or_404

@receiver(post_save,sender=Excel_file)
def extract_data(sender,instance,created,**kwargs):
    # instance.save()
    file = instance.file
    try:
        df = pd.read_excel(f'media/{file}')
    except:
         pass
    
    try:
        df = pd.read_csv(f'media/{file}')
    except:
         pass
    

    print(df.head(0))
    for i in range(len(df)):
        gid_value = instance.gid
        excel_file_instance = Excel_file.objects.get(gid=gid_value)
        user = userinfo.objects.create(gid=excel_file_instance, group_name=instance.group_name, name=df['Name'][i], sname=df['Surname'][i], email=df['Email'][i], website=df['Website'][i], company_name=df['Company Name'][i], business_details=df['Business Details'][i], phone_no=df['Phone No'][i])
        user.save()

@receiver(post_save, sender=userinfo)
def send_email_to_new_user(sender, instance, created, **kwargs):
    if not instance.mail_sent:
            # Render email template
            # Send email using SMTP server
            mail_content = get_object_or_404(EMail_container,group_name=instance.group_name)
            print(mail_content,instance.email)
            subject = mail_content.subject
            from_email = 'hrithikhadawale73@gmail.com'
            html_message = mail_content.message
            plain_message = strip_tags(html_message)
            recipient_list = [instance.email,]
            send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message, fail_silently=False)
            # Update mail_sent flag
            instance.mail_sent = True
            instance.save()
