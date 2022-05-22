from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    #path('index', views.index, name='index'),
    path('', views.view_merits, name='view_merits'),
    #path('', views.view_home, name='view_home'),
    #path('index', views.view_home, name='view_home'),
    path('index', views.view_merits, name='view_merits'),
    path('view_offerings', views.view_offerings, name='view_offerings'),

    path('view_merits_detail/<int:id>/',
         views.view_merits_detail, name='view_merits_detail'),
    path('view_merits', views.view_merits, name='view_merits'),
    path('view_home', views.view_home, name='view_home'),
    path('view_add_counter/<int:id>/',
         views.view_add_counter, name='view_add_counter'),

]
