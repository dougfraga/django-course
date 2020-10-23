from django.urls import path

from pypro.modules import views


app_name = 'modules'
urlpatterns = [
    path('<slug:slug>', views.detail, name='detail'),
    path('lessons/<slug:slug>', views.lesson, name='lesson'),
]
