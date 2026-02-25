from django.urls import path
from app.views import index, outra
urlpatterns = [
    path('', index, name='index'),
    path('outra', outra, name='outra'),
]
