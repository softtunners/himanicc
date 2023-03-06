from dataclasses import field
import email
from django import forms
from .models import *



class ContactForm(forms.ModelForm):
    services={
        ('----','-----'),
        ('Brand Guideline','Brand Guideline'),
        ('Brand Audit','Brand Audit'),
        ('Brand Stories','Brand Stories'),
        ('Brand Design','Brand Design'),
        ('Direct Mail Services Design','Direct Mail Services Design'),
        ('Corporate Identity','Corporate Identity'),
        ('Merchandising Services Design','Merchandising Services Design'),
        ('Product Concept & Design','Product Concept & Design'),
        ('Stall Design & Mall Activity','Stall Design & Mall Activity'),
        ('Signage & Display Design','Signage & Display Design'),
        ('3D Advertising Video','3D Advertising Video'),
        ('Market Research','Market Research')
        

    }
    service =forms.ChoiceField(  required=False ,initial='----',choices=services ,widget=forms.Select(attrs={'class': 'form-control'}))

    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control','placeHolder':" Email"}))
    number = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeHolder':"Number"}))
    fname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeHolder':"First Name"}))
    comment=forms.CharField(required=False ,widget=forms.Textarea(attrs={'class':'form-control','placeHolder':"Tell us more about your project, needs, and timeline."}))
    website=forms.CharField(required=False ,widget=forms.TextInput(attrs={'class':'form-control','placeHolder':"Business Name Or URL"}))

    class Meta:
        model= Contact
        exclude=['date']
  

class CandidateForm(forms.ModelForm):
    job_title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeHolder':"Position/Job Title"}))
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeHolder':"Full Name"}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeHolder':"Email"}))
    phone_no=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeHolder':"Phone Number"}))
    additional_info=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeHolder':"Additional Information"}))
    resume=forms.FileField()
    class Meta:
        model= Candidates
        exclude=['date']
