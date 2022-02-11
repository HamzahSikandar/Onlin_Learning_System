from django.contrib import admin
from django.urls import path,include
from django.conf import settings 
from django.conf.urls.static import static

admin.site.site_header='MyAcademy Admin'
admin.site.site_title='MyAcademy Admin Panel'
admin.site.index_title='Welcome to MyAcademy Admin Panel'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('blog/',include('bloging.urls')),
    path('tutorial/',include('tutorials.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
