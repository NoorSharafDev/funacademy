from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# use TemplateView and template_name to render a file from templates directory

class Home(TemplateView):
    template_name = 'index.html'


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid Sign up hahahaha'
    form = UserCreationForm()
    context = {'form':form, 'error_message':error_message}
    return render(request,'registration/signup.html',context)







