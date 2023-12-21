from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('compra/', views.purchase, name='purchase'),
    path('status/', views.status, name='status'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),

]
