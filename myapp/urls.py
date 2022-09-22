
from django.urls import path
from myapp import views
urlpatterns = [
    path('', views.index),
    path('cat/', views.cat),
    path('random/', views.random),
    path("random/1/", views.one),
    path("random/10/", views.than),
    path('random/100/', views.Hundred)
]
