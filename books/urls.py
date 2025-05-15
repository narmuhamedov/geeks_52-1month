from django.urls import path
from . import views

urlpatterns = [
  #Пишем название класса и обязательно добавляем .as_view()
  path ('book_list/', views.BookListView.as_view(), name='book_list'),
  path ('book_list/<int:id>/', views.BookDetailView.as_view(), name='book_detail'),
  path ('book_list/<int:id>/delete/', views.DeleteBookView.as_view(), name='delete_book'),
  path ('book_list/<int:id>/update/', views.UpdateBookView.as_view(), name='update_book'),
  path ('create_book/', views.CreateBookView.as_view(), name='create_book'),
  path ('search/', views.SearchBookView.as_view(), name='search'),
]