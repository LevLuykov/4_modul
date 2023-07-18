from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('start', index),
    path('lesson_4', index)
]
