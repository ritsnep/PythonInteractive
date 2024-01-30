
from django.shortcuts import render,HttpResponse
from.models import Contact
from django.contrib import messages
from blogsite.models import Post
# Create your views here.
def home(request):
    return render(request,'home/home.html')

def contact(request):
    if request.method=='POST':
        name =request.POST['name']
        email =request.POST['email']
        phone =request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<2 or len(phone)<2 or len(content)<4 :
            messages.error(request, "Please Fill the Form")
        else:
            contact =Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request, 'YOur message has been Received')
        # print(name,phone,email,content)
            
    return render(request,"home/contact.html")

def about(request):
    return render(request,"home/about.html")


def search (request):
    query=request.GET['query']
    allPosts=Post.objects.filter(title__icontains=query)
    context={'allPosts':allPosts}
    return render(request,"home/search.html",context)