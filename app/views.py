from django.shortcuts import render

# Create your views here.
from django.views.generic import View,TemplateView
from app.form import *
from django.http import HttpResponse
class Data_render(View):
    def get(self,request):
        d={'name':'ASHU'}
        return render(request,'data_render.html',d)
    
#insert_fbv

def insert_fbv(request):
    SFO= StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('Data inserted')
    return render(request,'insert_fbv.html',d)
#Cbv_insert
class Cbv_insert(View):
    def get(self,request):
        SFO=StudentForm()
        d={'SFO':SFO}
        return render(request,'Cbv_insert.html',d)
    def post(self,request):
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('Cbv_insert')



class Temp(TemplateView):
    template_name='temp.html'
