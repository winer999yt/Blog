from tkinter.font import names

from django.contrib import admin
from django.urls import path

from main.views import RegisterView, LoginView, logout_view, BlogView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BlogView.as_view(), name='articles'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
]
