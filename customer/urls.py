from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from customer import views
from customer.views import *

urlpatterns = [
   # path('customersignup', views.customer_signup_view,name='customersignup'),
    path('customer-dashboard', views.customer_dashboard_view,name='customer-dashboard'),
    #path('customerlogin', LoginView.as_view(template_name='medical/adminlogin.html'),name='customerlogin'),
    path('eng',views.eng.as_view(),name="eng"),
    path('logout/', LogoutUser),
    path('loginuser/',LoginUser),
    path('homepage', HomePage),
    path('clicklogin', clicklogin),
    path('register_user/',RegisterUser),
    path('click_user', ClickRegister),
    #path('register_user', RegisterUser),
    
]