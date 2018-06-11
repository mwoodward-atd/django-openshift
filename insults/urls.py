from django.urls import path

from . import views

app_name = 'insults'


urlpatterns = [
    path('', views.insult, name='insult')
]
