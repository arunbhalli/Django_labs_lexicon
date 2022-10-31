from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
  return HttpResponse('<em>Hello world!</em>')

def help(request):
  my_help = {'help_me':"I am from help page "}
  return render(request,'help.html',context=my_help)