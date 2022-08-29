
from django.contrib import admin
from django.urls import path
from poll.views import register,login,logout,add_poll,home,profile,addpolledit,delete
urlpatterns = [
    # for poll app
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('signup/',register,name='register'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('profile/',profile,name='profile'),
    path('add_poll/',add_poll,name='add_poll'),
    path('addpoll/<int:pk>/',addpolledit,name='addpolledit'),
    path('profile/<int:pk>',delete,name='delete'),

]
