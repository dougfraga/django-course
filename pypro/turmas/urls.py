from django.urls import path

from pypro.turmas import views


app_name = 'turmas'
urlpatterns = [
    path('', views.index, name='index'),
]
