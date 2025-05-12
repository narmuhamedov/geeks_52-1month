from django.urls import path
from . import views

urlpatterns = [
  path ('book_list/', views.books_list_view, name='book_list'),
  path ('book_list/<int:id>/', views.book_detail_view, name='book_detail'),
  path ('book_list/<int:id>/delete/', views.delete_book_view, name='delete_book'),
  path ('book_list/<int:id>/update/', views.update_book_view, name='update_book'),
  path ('create_book/', views.create_book_view, name='create_book'),
]