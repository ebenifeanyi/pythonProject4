from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.models import User
from .models import Profile


# Create your views here

def home(request):
    u = User.objects.get(username='toshiba')
    p = Profile.objects.get(acc=u)
    return render(request, 'main/index.html', {'p': p})


def profiles(request):
    p = Profile.objects.all()
    return render(request, 'main/user_list.html', {'p': p})


def createacct(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            e = form.cleaned_data['email']
            p = form.cleaned_data['password']
            p2 = form.cleaned_data['password2']
            User.objects.create_user(u, e, p)

            return HttpResponse('successful!')
        # else:
        # print(form.errors['username'])
        #    return render(request, 'main/create.html', {'form': form})
    form = RegisterForm()
    return render(request, 'main/create.html', {'form': form})


def profile_create(request):
    if request.method == 'POST':
        user = request.user
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            newp = Profile(acc=user, firstname=form.cleaned_data['firstname'], lastname=form.cleaned_data['lastname'],
                           location=form.cleaned_data['location'], bio=form.cleaned_data['bio'],
                           pic=request.FILES['pic'])
            newp.save()
            return HttpResponse('success')
        else:
            return HttpResponse(form.error_message)
    form = ProfileForm()
    return render(request, 'main/profile_create.html', {'form': form})


def profile_detail(request, pk):
    p = Profile.objects.get(pk=pk)
    return render(request, 'main/pro.html', {'im': p})


def add_friend(request, pk):
    p = Profile.objects.get(pk=pk)
    u = request.user

    p.friends.add(u)
    p.save()
    return redirect('home')


def view_friends(request, pk):
    p = Profile.objects.get(pk=pk)
    friends = p.friends.all()
    return render(request, 'main/friends_list.html', {'im': friends})
