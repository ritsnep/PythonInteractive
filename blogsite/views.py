
from django.shortcuts import render,HttpResponse
from .models import Post

# # Create your views here.

def bloghome(request):
    allPosts=Post.objects.all()
    context={'allPosts':allPosts}
    return render(request,'blogsite/bloghome.html',context)

# def blog(request):
#     if request.method=='POST':
#         name =request.POST['name']
#         email =request.POST['email']
#         phone =request.POST['phone']
#         content =request.POST['content']
#         if len(name)<2 or len(email)<2 or len(phone)<2 or len(content)<4 :
#             messages.error(request, "Please Fill the Form")
#         else:
#             contact =Contact(name=name,email=email,phone=phone,content=content)
#             contact.save()
#             messages.success(request, 'YOur message has been Received')
#         # print(name,phone,email,content)
            
    # return render(request,"home/contact.html")


def blogpost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    context={'post':post}
    return render(request,"blogsite/blogpost.html",context)

