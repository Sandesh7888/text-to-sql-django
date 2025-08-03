
from django.contrib import admin
from django.urls import path
from Text_to_SQL_App import views
from django.contrib.auth.views import LogoutView,LoginView
from django.urls import path,include
from Text_to_SQL_App.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    #path('clock', views.clock,name='clock'),
    path('customer/',include('customer.urls')),
    path('',views.home_view,name=''),
    path('logout', LogoutView.as_view(template_name='text/logout.html'),name='logout'),
    path('aboutus/', views.aboutus_view),
    #path('contactus', views.aboutus_view),
    #path('afterlogin', views.afterlogin_view,name='afterlogin'),
   
   # path('adminlogin', LoginView.as_view(template_name='medical/adminlogin.html'),name='adminlogin'),
    path('logout/', LogoutUser),
    path('loginuser/',LoginUser),
    path('homepage', HomePage),
    path('clicklogin', clicklogin),
    path('register_user/',RegisterUser),
    path('click_user', ClickRegister),


]
