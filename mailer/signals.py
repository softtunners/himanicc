from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.db.models.signals import post_save
from django.dispatch import receiver
from mailer.models import *
import pandas as pd
from django.shortcuts import get_object_or_404
from django.template.loader import get_template

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
    
    for i in range(len(df)):
        gid_value = instance.gid
        excel_file_instance = Excel_file.objects.get(gid=gid_value)
        user = userinfo.objects.create(gid=excel_file_instance, group_name=instance.group_name, name=df['Name'][i], sname=df['Surname'][i], email=df['Email'][i], website=df['Website'][i], company_name=df['Company Name'][i], business_details=df['Business Details'][i], phone_no=df['Phone No'][i])
        user.save()

@receiver(post_save, sender=userinfo)
def send_email_to_new_user(sender, instance, created, **kwargs):
    if not instance.mail_sent:
            #  Render email template
            # Send email using SMTP server
            mail_content = get_object_or_404(EMail_container,group_name=instance.group_name)
            print(mail_content,instance.email)

            # htmly     = get_template('html/email.html')
            subject ="Testing Email"
            html_message = """
    
    <!DOCTYPE html>
<html lang="en">


<div style="margin: 20px auto;
text-align: center; margin: 0 auto; width: 650px; font-family: 'Public Sans', sans-serif; background-color: #e2e2e2; display: block;
        
">
    <table align="center" border="0" cellpadding="0" cellspacing="0"
        style="background-color: white; width: 100%; box-shadow: 0px 0px 14px -4px rgba(0, 0, 0, 0.2705882353);-webkit-box-shadow: 0px 0px 14px -4px rgba(0, 0, 0, 0.2705882353);">
        <tbody>
            <tr>
                <td>
                    <table class="header-table" align="center" border="0" cellpadding="0" cellspacing="0" width="100%">
                        <tr class="header"
                            style="background-color: #f7f7f7;display: flex;align-items: center;justify-content: space-between;width: 100%;">
                            <td class="header-logo" style="padding: 10px 32px;">
                                <a href="../front-end/index.html" style="display: block; text-align: left;">
                                    <img src="https://themes.pixelstrap.com/fastkart/email-templete/images/logo.png" class="main-logo" alt="logo">
                                </a>
                            </td>
                        </tr>
                    </table>

                    <table class="contant-table" style="margin-bottom: -6px;" align="center" border="0" cellpadding="0"
                        cellspacing="0" width="100%">
                        <thead>
                            <tr>
                                <td>
                                    <img src="https://themes.pixelstrap.com/fastkart/email-templete/images/welcome-poster.jpg" alt="">
                                </td>
                            </tr>
                        </thead>
                    </table>

                    <table class="contant-table" style="margin-top: 40px;" align="center" border="0" cellpadding="0"
                        cellspacing="0" width="100%">
                        <thead>
                            <tr style="display: block;">
                                <td style="display: block;">
                                    <h3
                                        style="font-weight: 700; font-size: 20px; margin: 0; text-transform: uppercase;">
                                      Take your business to the next level We have INNOVATIVE IDEAS & SOLUTIONS to market your Business.</h3>
                                </td>

                                <td>
                                    <p
                                        style="font-size: 14px;font-weight: 600;width: 82%;margin: 8px auto 0;line-height: 1.5;color: #939393;font-family: 'Nunito Sans', sans-serif;">
                                        "a brand and communication professionals are always getting pulled in many directions. Sales wants something new, while product team wants all the features to be highlighted. Boss is pointing “something is missing here” and asking for change. If you are facing the above situations, we are here to help you out."
                                    </p>
                                </td>
                            </tr>
                        </thead>
                    </table>

                    <table class="button-table" style="margin: 34px 0;" align="center" border="0" cellpadding="0"
                        cellspacing="0" width="100%">
                        <thead>
                            <tr style="display: block;">
                                <td style="display: block;">
                                    <button class="password-button" style="padding:10px; background:white;color:black;"><a href="https://himanicc.com/" style="color:black;font-weight:bold">More Information</a></button>
                                </td>
                            </tr>
                        </thead>
                    </table>

                    <table class="contant-table" align="center" border="0" cellpadding="0" cellspacing="0" width="100%">
                        <thead>
                            <tr style="display: block;">
                                <td style="display: block;">
                                    <p
                                        style="font-size: 14px; font-weight: 600; width: 82%; margin: 0 auto; line-height: 1.5; color: #939393; font-family: 'Nunito Sans', sans-serif;">
                                       
                                            "We provide One-stop solutions for Business Owners & Entrepreneurs who wish to promote their businesses / Services in the market. We will help them with all types of Brand Design Work | Go2 Market Strategy | Digital Marketing | Brand Awareness Strategy's | Advertising Commercials | Customise Software | Webdesign & WebApplication." </p>
                                    <a class="theme-color" href="https://himanicc.com/">More Info</a> 
                                </td> 
                            </tr>
                        </thead>
                    </table>

                    <table class="text-center footer-table" align="center" border="0" cellpadding="0" cellspacing="0"
                        width="100%"
                        style="background-color: #282834; color: white; padding: 24px; overflow: hidden; z-index: 0; margin-top: 30px;">
                        <tr>
                            <td>
                                <table border="0" cellpadding="0" cellspacing="0" class="footer-social-icon text-center"
                                    align="center" style="margin: 8px auto 11px;">
                                    <tr>
                                        <td style="display:flex;">
                                            <img src="https://himanicc.com/assets/img/hcc-logo-final-96x96.png"  style="width:10% ;margin:5px;" alt="">
                                            <h4 style="font-size: 15px; font-weight: 700; margin: 0;color:white;" <span
                                                    class="theme-color">Prashant Chavan  Brand Design & Consultant  <br>+91 9769210723 ‌ prashant@himanicc.com</span></h4>
                                        </td>
                                    </tr>
                                </table>
                               
                                
                                
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </tbody>
    </table>
</div>

</html>
    """
            from_email = 'hrithikhadawale73@gmail.com'
            plain_message = strip_tags(html_message)
            recipient_list = [instance.email,]
            send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message, fail_silently=False)
            # Update mail_sent flag
            instance.mail_sent = True
            instance.save()

