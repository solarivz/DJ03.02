from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),                    # Главная страница
    path('new/', views.new, name='new'),                  # Вторая страница
    path('about/', views.about, name='about'),              # О нас
    path('services/', views.services, name='services'),     # Услуги
    path('contact/', views.contact, name='contact'),        # Контакты
]