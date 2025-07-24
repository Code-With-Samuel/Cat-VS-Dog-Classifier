from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='showcase_home'),
    path('features/', views.features, name='showcase_features'),
    path('demo/', views.demo, name='showcase_demo'),
    path('about/', views.about, name='showcase_about'),
]
