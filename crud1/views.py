from django.shortcuts import render,HttpResponseRedirect

from .forms import studentModelForm
from .models import student
from django.http import HttpResponse

# Create your views here.
def home(req):
    if req.method=="POST":
        fm=studentModelForm(req.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        fm=studentModelForm()
    data=student.objects.all()  #equivalent to fatchall()
    return render(req,'crud1/base.html',{'fm':fm,'dat':data})


def delete_data(req,id):
    if req.method=="POST":
        data=student.objects.get(pk=id)
        data.delete()
        return HttpResponseRedirect('/')  #home() calling
    


def update_data(req,id):
    if req.method=="POST":
        data=student.objects.get(pk=id)
        fm=studentModelForm(req.POST,instance=data)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
            
    else:
        data=student.objects.get(pk=id)
        fm=studentModelForm(instance=data)
        return render(req,'crud1/update.html',{'fm':fm,'id1':id})
        