from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import dest

# Create your views here.
def demo(request):
    #name="india"
    obj=place.objects.all()
    obt=dest.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obt})
#def addition(request):
    #x=int(request.GET['num1'])
   # y=int(request.GET['num2'])
    #res=x+y
    #fun=x-y
    #fun1=x*y
    #fun2=x/y
    #return render(request,"result.html",{'result':res,'result1':fun,'result2':fun1,'result3':fun2})



#def about(request):
 #   return render(request,"result.html")
#def contact(request):
    #return HttpResponse("hello am contact")