from . import views
from django.urls import path,include
urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.handlesignup,name='handlesignup'),
    path('login/',views.handlelogin,name='handlelogin'),
    path('logout/',views.handlelogout,name='handlelogout'),
    path('contact/',views.contact,name='contact'),
    path('search/',views.search,name='search'),
    

   
]