
from django.db import models
from django.utils.timezone import now
from django.db import models
from django.utils.html import format_html
from ckeditor.fields import RichTextField
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.
# category


class IpModel(models.Model):
    ip = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateTimeField(default=now)

    def __str__(self):
        return self.ip
    class Meta:
        verbose_name = "Ip Add"
        verbose_name_plural = "Ip Add"

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.cat_title

    def get_absolute_url(self):
        return reverse('add_post')


    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Category"



class Post(models.Model):

    title = models.CharField(max_length=100)
    post_id = models.AutoField(primary_key=True)
    thumbnail = models.ImageField(upload_to='blog/', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    discription = models.CharField(max_length=200, blank=False, null=True)
    writer_name = models.CharField(max_length=50)
    content = RichTextField()
    post_date = models.DateField()
    tags = TaggableManager(blank=True)
    like_post = models.ManyToManyField(
        IpModel, related_name="post_like", blank=True)
    post_now = models.BooleanField(default=False)

    def image_tag(self):

        return format_html('<img src="/media/{}" style="width:40px;height:40px;"'.format(self.thumbnail))

    def like_count(self):
        return self.like_post.count()

    class Meta:
        ordering = ['-post_date', ]
        verbose_name = "All Blogs"
        verbose_name_plural = "All Blogs"

    def get_absolute_url(self):
        return reverse("blog",  kwargs={'pk': self.post_id})

    @property
    def get_comments(self):
        return self.comment_content.all()
    

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Contact Page.


class Contact(models.Model):
    fname = models.CharField(max_length=50)
    number = models.IntegerField()
    email = models.EmailField()
    website = models.CharField(max_length=1000)
    service = models.CharField(max_length=50)
    comment = models.TextField()
    date = models.DateTimeField(default=now)
    class Meta:
        verbose_name = "Contact Forms"
        verbose_name_plural = "Contact Forms"


def get_uplaod_file_name(name, filename):
    
        return f'scrapbook/{name}/{filename}'


def get_uplaod_file(name, filename):
        return f'scrapbook/{name}/img/{filename}'


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ScrapBook Page


class Scrapbook(models.Model):
    name = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to=get_uplaod_file_name)
    description = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.name


class ScrapBookImg(models.Model):
    name = models.ForeignKey(Scrapbook, on_delete=models.CASCADE)
    img = models.ImageField(upload_to=get_uplaod_file)
    date = models.DateTimeField(default=now)

    def __str__(self):
        return f'{self.name}'


class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True, default=None)
    timestamp = models.DateTimeField(default=now)
    post = models.ForeignKey(
        Post, related_name='comment_content', on_delete=models.CASCADE)
   # parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    content = models.TextField()
    name = models.CharField(max_length=50)
    email = models.EmailField()
    class Meta:
        verbose_name = "Blog Comments"
        verbose_name_plural = "Blog Comments"


class SubcribeUsers(models.Model):
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(default=now)

    def __str__(self):
        return self.email 

    class Meta:
        verbose_name = "Subscribed Users"
        verbose_name_plural = "Subscribed Users"

class JobsPositions(models.Model):
    job_title = models.CharField(max_length=100)
    location = models.CharField(default="Mumbai",max_length=50)
    expirydate = models.DateField(null=False,default=now)

    description = RichTextField()
    class Meta:
        verbose_name = "Job Requirements"
        verbose_name_plural = "Job Requirements"

class Candidates(models.Model):
    job_title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.PositiveIntegerField(max_length=13)
    additional_info = models.TextField(null=True,blank=True)
    resume = models.FileField(upload_to="resume/")

    date = models.DateTimeField(default=now)

    class Meta:
        verbose_name = "Job Enquires"
        verbose_name_plural = "job Enquires"
