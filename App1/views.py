
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse


# Create your views here.

def index(request):
    return HttpResponse('Hello World')

def about(request):
    return HttpResponse('This is about page')

def add(request,a,b):
    return HttpResponse(a+b)

def intro(request,name,age):
    mydict={
        "name":name,
        "age":age
    }
    return JsonResponse(mydict)

def home(request):
    return render(request,'home.html')

def second(request):
    return render(request,'second.html')

def third(request):
    var="hello World"
    greeting="How are you"
    fruits=['apple','banana','litchi']
    num1,num2 =7,9
    ans= num1 > num2
    mydict ={
        "var":var,
        "msg":greeting,
        "myfruits":fruits,
        "num1":num1,
        "num2":num2,
        "ans":ans

    }
    return render(request,'third.html',context=mydict)

def image(request):
    return render(request,'image.html')

def myform(request):
    return render(request,'myform.html')
