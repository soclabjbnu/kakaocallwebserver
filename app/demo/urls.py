from django.urls import path

from . import views

app_name = 'demo'

urlpatterns = [
    path('demo/', views.demo, name='demo'),
    path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('policy/', views.policy, name='policy'),
    path('input_data/', views.input_data, name='input_data'),
]

