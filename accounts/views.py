from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages




def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned.data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username , password=password)
            login(request, user)
            return redirect('/login')
        
        
    else:
        form = UserCreationForm
        
    context = {
        'form' : form ,
    }
    return render(request, 'signup.html' , context)



def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("تم انشاء الحساب بنجاح"))
            return redirect('login')
    else:
        form = UserCreationForm()
            
            
    return render(request, 'signup.html', {
        'form':form,
        })
