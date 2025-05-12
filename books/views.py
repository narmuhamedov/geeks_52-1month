from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.http import HttpResponse


#CRUD - Create, Read, Update, Delete


#update book
def update_book_view(request,id):
    book_id = get_object_or_404(models.Book, id=id)
    if request.method == "POST":
        form  = forms.BookForm(request.POST, instance=book_id)
        if form.is_valid():
            form.save()
            return redirect('book_list')
            #return HttpResponse('Книга успешно обновлена')
    else:
        form = forms.BookForm(instance=book_id)
    return render(request, template_name='books/update_book.html', context={
        'form': form,
        'book_id': book_id,
        })


# Delete book
def delete_book_view(request, id):
    book_id = get_object_or_404(models.Book, id=id)
    book_id.delete()
    return redirect('book_list')
    #return HttpResponse('Книга успешно удалена')



#create_book
def create_book_view(request):
    if request.method == 'POST':
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
            #return HttpResponse('Книга успешно добавлена')
    else:
        form = forms.BookForm()
    return render(request, template_name='books/create_book.html', context={'form': form})





#read 
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
