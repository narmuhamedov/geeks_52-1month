from django.shortcuts import render, get_object_or_404
from . import models

def books_list_view(request):
    if request.method == 'GET':
        #Запрос из базы данных переменная book запрашивает данные у БД
        book = models.Book.objects.all().order_by('-id')
        context = {
            'book': book,
        }
        return render(request,
                      template_name='books/book_list.html',
                      context=context
                      )

# получение id и вывод detail
def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Book, id=id)
        context = {
            'book_id':book_id,
        }
        return render(request, 
                      template_name='books/book_detail.html',
                      context=context
                      )
