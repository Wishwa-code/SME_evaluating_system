from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('daily_amounts/', views.handle_daily_amounts, name='handle_daily_amounts'),
    path('employees/', views.handle_employees, name='handle_employees'),
    path('styles/', views.handle_styles, name='handle_styles'),
]