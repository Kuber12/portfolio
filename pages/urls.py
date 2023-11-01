from django.urls import path
from pages import views

urlpatterns = [
    path("", views.index, name='index'),
    path("contact", views.contact, name='contact'),
    path('download_pdf', views.download_pdf, name='download_pdf'),
]