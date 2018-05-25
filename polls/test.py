from django.urls import path
from . import views
urlpatterns = [
    path('', views.pol, name = 'pol'),
]