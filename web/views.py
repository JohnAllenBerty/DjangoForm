from django.shortcuts import render,redirect
from .models import TableName

# Create your views here.
def home(request):
    return render(request, 'index.html')

def add(request):
    name = request.GET['name']
    address = request.GET['address']

    
    obj = TableName(name= name, address=address)
    obj.save()
    return redirect ('/')

def search(request):
    x = request.GET['search']
    con = TableName.objects.filter(name = x)
    context = {
        'key' : con
    }
    return render(request,'display.html',context)

def display(request):
    con = TableName.objects.all()
    context = {
        'key' : con
    }
    return render(request,'display.html',context)

def back(request):
    return render(request,'index.html')

def update(request):
     x = request.GET['search']
     y = request.GET['update']
     con = TableName.objects.filter(name = x).update(name = y)
     contexts = {
         'keys' : con
     }
    #  return redirect('/')
     return render(request,'display.html',contexts)

def delete(request):
        x = request.GET['delete']
       
        con = TableName.objects.filter(name = x).delete()
        contexts = {
             'keys' : con
         }
        return render(request,'display.html',contexts)