from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_view, name='predict'),  # Root URL shows upload form
    path('predict/', views.predict_view, name='predict'),
]