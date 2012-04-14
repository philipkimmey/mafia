from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from django.contrib.auth.views import login

from index.forms import RegistrationForm

def login_page(request):
    login(request)
    return HttpResponseRedirect('/')

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
  
@csrf_exempt
def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
        return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()

    variables = RequestContext(request, {
        'form': form
    })
    
    return render_to_response(
        'registration/register.html', variables
    )
    
def index(request):
    return render(request, 'index.html', {})
