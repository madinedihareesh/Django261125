from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from .models import Post

# Create your views here.
# posts=[
#     {
#         'id':1,
#         'title':'HTML',
#         'dis':'It is used to create the structure of webpage'
#     },{
#         'id':2,
#         'title':'CSS',
#         'dis':'It is used to style the webpage'
#     },{
#         'id':3,
#         'title':'JavaScript',
#         'dis':'It is used to provide actions for webpage'
#     }
# ]

def index(request):
    Posts = Post.objects.all()
    print(Posts)
    return render(request,'posts/index.html',{'posts':Posts})

def detail(request,id):
    post_selected=None
    for post in posts:
        if post['id']==id:
            post_selected=post
            break
    return render(request,'posts/detail.html',{'post_selected':post_selected})


def base(request):
    return render(request,'base.html')




