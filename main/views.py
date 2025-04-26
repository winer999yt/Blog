from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .models import Article


class BlogView(View):
    def get(self, request):
        articles = Article.objects.all().order_by('-created_at')
        return render(request, 'articles.html', {'articles': articles})

    def post(self, request):
        if request.user.is_authenticated:
            Article.objects.create(
                title=request.POST.get('title'),


            )
            return redirect('index')
        return redirect('login')

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        return render(request, 'register.html', {'form': form})


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password1')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Username or password is incorrect'})


def logout_view(request):
    logout(request)
    return redirect('/login/')

