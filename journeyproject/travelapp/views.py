from django.http import HttpResponse
from django.shortcuts import render
from . models import Place,People
# # Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1=People.objects.all()
    return render(request,"index.html",{'result':obj,'team':obj1})
# def result(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res1=x+y
#     res2=x-y
#     res3=x*y
#     res4=x/y
#     return render(request,"result1.html",{"add":res1,"sub":res2,"mul":res3,"div":res4})