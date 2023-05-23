from django.shortcuts import render
from devi.models import *
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.
class Home(TemplateView):
    template_name='devi/home.html'



class SchoolList(ListView):
    model=School
    context_object_name='schools'

class SchoolDetail(DetailView):
    model=School
    context_object_name='sclobject'



class SchoolCreate(CreateView):
    model=School
    fields='__all__'


class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'

class SchoolDelete(DeleteView):
    model=School
    context_object_name='schoolobject'
    success_url=reverse_lazy('SchoolList')