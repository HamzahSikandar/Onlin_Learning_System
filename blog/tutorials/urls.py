from tutorials import views
from django.urls import path,include
urlpatterns = [
    path('',views.tutorial,name='about'),
    path('<int:sno>/',views.title,name='title'),
    path('contact/<str:slug>',views.Contentpage,name='contentpage')
]