from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render , redirect
from .models import Userprofile

def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            Userprofile.objects.create(user=user)
            
            return redirect('/login/')
    else:
            
        form = UserCreationForm()
    
    return render(request, 'userprofile/registrar.html', {
        'form':form
        })