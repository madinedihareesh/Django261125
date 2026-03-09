from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
posts=[
    {
        'id':1,
        'title':'HTML',
        'dis':'It is used to create the structure of webpage'
    },{
        'id':2,
        'title':'CSS',
        'dis':'It is used to style the webpage'
    },{
        'id':3,
        'title':'JavaScript',
        'dis':'It is used to provide actions for webpage'
    }
]
def index(request):
    return render(request,'index.html',{'posts':posts})

def detail(request,id):
    html=''
    for post in posts:
        if post['id']==id:
            html+=f'''<h3>{post['id']}-{post['title']}</h3>
                 <p>{post['dis']}</p>
                 <a href='/posts/index/'>Home</a>   '''
            return HttpResponse(html)
    else:
        return HttpResponseNotFound('NO post found with this input')

def youtube(request):
    url=reverse("index")
    print(url)
    return HttpResponseRedirect(url)




