from django.urls import path
from myform import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.submit, name='submit'),
]
