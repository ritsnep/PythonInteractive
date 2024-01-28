
from django.shortcuts import render,HttpResponse

# # Create your views here.

def bloghome(request):
    return render(request,'blogsite/bloghome.html')

def blogpost(request):
    return render(request,"blogsite/blogpost.html")
