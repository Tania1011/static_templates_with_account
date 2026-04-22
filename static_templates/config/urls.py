from django.contrib import admin
from django.urls import path, include
from stat_pgs_tmplate import views  


urlpatterns = [

    path('admin/', admin.site.urls),
    path('home/', views.home, name="home"),  
    path('contact/', views.contact, name="contact"),         
    path('', include('accounts.urls')),
    path('page1/', views.p1, name='page1'),
    path('page2/', views.p2, name='page2'),
]
