
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render , get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
import datetime
from django.contrib.auth.models import User
from datetime import date
from taggit.models import Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import *
# Create your views here.
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_prev_next(id):
    b = get_object_or_404(Post, post_id=id)

    posts = Post.objects.alias().filter(post_now=True)

    for i in range(len(posts)):
        try:
            if b==posts[0]:
                next = posts[i+1]
                prev=None
                break
            elif b==posts.reverse()[0]:
                prev=posts.reverse()[i+1]
                next=None
                break
            else:
                if b==posts[i]:
                    next = posts[i+1]
                    prev = posts[i-1]
                    break
        except :
            prev=None
            next=None
    return prev, next



def home(request):
    allblogs = Post.objects.filter(post_now=True).reverse()[:4]
    blogs=[]
    form = ContactForm
    for p in allblogs :
        if p.post_date <= date.today():
                blogs.append(p)

    ip_count = 2827 + int(IpModel.objects.all().count()) 
    contact = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Submitted Successfully!')

            return HttpResponseRedirect(reverse('home'))
        print(form.errors)
        messages.error(request,f'Not Submitted {form.errors}!')
    return render(request, "html/index.html" ,{'blogs':blogs,'contact':contact,'form':form,'ip_count':ip_count})


def contact(request):
    form = ContactForm()

    if request.method == "POST":
        name=request.POST.get('fname')
        email=request.POST.get('email')
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Submitted Successfully!')
            return HttpResponseRedirect(reverse("contact"))

        else:
            messages.error(request,f'Not Submitted {form.errors}!')

    return render(request, "html/contact.html",{'form':form})


def blogMain(request):

    try:
            categoryName = request.GET.get('categoryName')
            year = request.GET.get('year')
            tag = request.GET.get('tag')
            print('tag:',tag)
            if tag !=None:
                tag = get_object_or_404(Tag, slug=tag)

                allblogs = Post.objects.filter(post_now=True).filter(tags=tag)
                blogs=[]

                for p in allblogs :
                        if p.post_date <= date.today():
                            blogs.append(p)



            elif categoryName !="":
                if year !="":
                    cat = get_object_or_404(Category,cat_title=categoryName)
                    allblogs = Post.objects.filter(category=cat.cat_id).filter(post_now=True)
                    blogs=[]
                    for p in allblogs :
                            if p.post_date <= date.today():

                                if p.post_date.year==int(year):
                                    blogs.append(p)
                else:
                    cat = get_object_or_404(Category,cat_title=categoryName)
                    blogs = Post.objects.filter(category=cat.cat_id)
            elif year!="":
                allblogs = Post.objects.filter(post_now=True)
                blogs=[]
                for p in allblogs :
                    if p.post_date <= date.today():

                        if p.post_date.year==int(year):
                                    blogs.append(p)
            else:
                    allblogs = Post.objects.filter(post_now=True)
                    blogs=[]

                    for p in allblogs :
                        if p.post_date <= date.today():
                            blogs.append(p)

    except Exception as e:
        allposts= Post.objects.filter(post_now=True)
        blogs=[]
        for p in allposts:
                if p.post_date <= date.today():
                    blogs.append(p)
    finally:
        post_year=[]
        post_for_yr= Post.objects.all()
        for p in post_for_yr:

                    if p.post_date.year in post_year:
                        pass
                    else:
                        post_year.append(p.post_date.year)
        tags = Tag.objects.all()
        categories = Category.objects.all()

        page = request.GET.get('page', 1)

        paginator = Paginator(blogs, 2)
        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)

        context={
            'blogs':blogs,
            'tags' : tags,
            'categories':categories,
            'post_year':post_year

        }
        return render(request, "html/blog.html",context)


def blog(request,pk):
    blog = get_object_or_404(Post,post_id =pk)
    ip = get_client_ip(request)

    if not IpModel.objects.filter(ip=ip).exists():
            IpModel.objects.create(ip=ip)
    liked = False

    if blog.like_post.filter(id=IpModel.objects.get(ip=ip).id).exists():
                        liked=True

    comments =reversed(BlogComment.objects.filter(post=blog))
    count_comments = (BlogComment.objects.filter(post=blog).count())
    categories = Category.objects.all()
    post_year=[]
    post_for_yr= Post.objects.all()
    for p in post_for_yr:

                    if p.post_date.year in post_year:
                        pass
                    else:
                        post_year.append(p.post_date.year)

    allblogs = Post.objects.filter(post_now=True).reverse()[:3]
    recent_blogs=[]
    tags = Tag.objects.all()

    for p in allblogs :
        if p.post_date <= date.today():
                recent_blogs.append(p)

    prev, next = get_prev_next(blog.post_id)
    print(prev,next)
    context={
        'blog':blog,
        'categories':categories,
        'post_year':post_year,
        'recent_blogs':recent_blogs,
           'tags':tags,
           'prev':prev,
           'next':next,
           'liked':liked,
           'comments':comments,
           'count_comments':count_comments
    }
    return render(request,  "html/Blog-Page.html",context)


def about(request):
    return render(request, "html/about.html")


def service(request):
    return render(request, "html/services.html")


def scrapbook(request):
    models = Scrapbook.objects.all()
    return render(request, "html/scrapbook.html",{'models':models})


def Gallery(request,pk):
    book = Scrapbook.objects.get(id=pk)
    imgs = ScrapBookImg.objects.filter(name=book.id)

    return render(request, "html/Gallery.html",{'img_gallery':imgs,'book':book})





def comment(request,pk):
    name = request.GET.get('name')
    email = request.GET.get('email')
    content = request.GET.get('comment')
    blog = get_object_or_404(Post,post_id=pk)
    comment = BlogComment(name=name,email=email,content=content,post=blog)
    comment.save()
    messages.success(request,"Comment Successfully submited")
    return HttpResponseRedirect(reverse('blog',args=[blog.post_id]))


def subscribe(request):
    email = request.GET.get('email')
    print(email)
    try :
                memail =SubcribeUsers.objects.get(email=email)
                messages.error(request,'Email Already Register ')

                return HttpResponseRedirect(reverse('blogs'))

    except Exception as e:
                    form = SubcribeUsers(email=email)
                    form.save()
                    messages.success(request,'Thank For Subscribe. You will recive all quotes on mail.')
                    return HttpResponseRedirect(reverse('blogs'))

def service(request):
    return render(request,"html/services.html")



def blogsettingsview(request):
    # try:
        posts=Post.objects.all()
        ip_count = IpModel.objects.all().count()
        context={
            'posts':posts,
            'ip_count':ip_count
        }

        return render(request,'html/preview-blog.html',context,)



def LikeView(request,pk):

        # if User.is_authenticated:
        #     post = get_object_or_404(Post,post_id=request.POST.get('post_id'))
        #     if post.like_post.filter(id=request.user.id).exists():
        #         post.like_post.remove(request.user)
        #     else:
        #         post.like_post.add(request.user)
        #     return HttpResponseRedirect(reverse('blog',args=[pk]))
            post = get_object_or_404(Post,post_id=pk)
            print(post)
            ip = get_client_ip(request)
            if not IpModel.objects.filter(ip=ip).exists():
                IpModel.objects.create(ip=ip)
            if post.like_post.filter(id=IpModel.objects.get(ip=ip).id).exists():
                post.like_post.remove(IpModel.objects.get(ip=ip))
            else:
                post.like_post.add(IpModel.objects.get(ip=ip))
            return HttpResponseRedirect(reverse('blog',args=[post.post_id]))





def prashant(request):
    return render(request,'html/prashant-chavan.html')


def carrier(request):
    jobs=JobsPositions.objects.all()
    today =  date.today()
    candidateform = CandidateForm()
    if request.method == "POST":
        name=request.POST.get("name")
        position=request.POST.get("job_title")

        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            x =f'{name} Your Application Submitted Successfully!'
            messages.success(request,x)

            return HttpResponseRedirect(reverse('career'))
        else:
            x =f'{name} Please Fill Correct Information'

            messages.error(request,x)

    return render(request, "html/carrier.html",{'jobs':jobs,'candidateform':candidateform,'today':today})



