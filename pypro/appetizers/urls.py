from django.urls import path

from pypro.appetizers.views import video, index

app_name = 'appetizers'
urlpatterns = [
    path('<slug:slug>', video, name='video'),
    path('', index, name='index'),
]
