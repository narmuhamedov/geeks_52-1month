from django.urls import path
from . import views


urlpatterns = [
    path('parser_form/', views.ParserForm.as_view(), name='parser_form'),
    path('rezka_list/', views.RezkaListView.as_view(), name='rezka_list')
]