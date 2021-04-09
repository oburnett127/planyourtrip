from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/<int:id_num>', views.home, name='home'),
    path('cities/', views.cities, name='cities_page'),
]
