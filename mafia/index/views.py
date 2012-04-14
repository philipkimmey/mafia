from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

def logout_page(request):
    return HttpResponseRedirect('/')
    
def register_page(request):
    return HttpResponseRedirect('/')
    
def index(request):
    return render(request, 'index.html', {})
