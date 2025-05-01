from django.urls import path
from . import views

urlpatterns = [
  path ('', views.fist_page_view, name='index'),
]