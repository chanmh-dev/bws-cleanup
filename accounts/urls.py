from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.view_login, name='view_login'),
    path('logout/', views.view_logout, name='view_logout'),
    path('signup/', views.view_signup, name='view_signup'),
    path('login_counter/', views.view_login_counter, name='view_login_counter'),
]
