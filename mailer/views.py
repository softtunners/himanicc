from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.

def mailformats(request):
    all_mail_formate_list = EMail_container.objects.all()
    return render(request,'html/allmailformates.html',{'all_mail_formate_list':all_mail_formate_list})

def mailcontent(request,pk):
    mail = get_object_or_404(EMail_container,id=pk)
    return render(request,'html/mailer.html',{'mail':mail})