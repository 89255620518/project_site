from django.urls import path
from . import views

urlpatterns = [
    # Отслеживаем переход на главную страницу
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create')
]

