from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.http import HttpResponse
from django.views import generic
from django.db.models import F

#CRUD - Create, Read, Update, Delete

#search
class SearchBookView(generic.ListView):
    template_name = 'books/book_list.html'
    context_object_name = 'book'
    paginate_by = 5
    model = models.Book

    def get_queryset(self):
        return self.model.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context




#update book
class UpdateBookView(generic.UpdateView):
    template_name = 'books/update_book.html'
    form_class = forms.BookForm
    success_url = '/book_list/'

    def get_object(self,  **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book_id)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateBookView, self).form_valid(form=form)







# def update_book_view(request,id):
#     book_id = get_object_or_404(models.Book, id=id)
#     if request.method == "POST":
#         form  = forms.BookForm(request.POST, instance=book_id)
#         if form.is_valid():
#             form.save()
#             return redirect('book_list')
#             #return HttpResponse('Книга успешно обновлена')
#     else:
#         form = forms.BookForm(instance=book_id)
#     return render(request, template_name='books/update_book.html', context={
#         'form': form,
#         'book_id': book_id,
#         })


# Delete book
class DeleteBookView(generic.DeleteView):
    template_name = 'books/confirm_delete.html'
    success_url = '/book_list/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book_id)



# def delete_book_view(request, id):
#     book_id = get_object_or_404(models.Book, id=id)
#     book_id.delete()
#     return redirect('book_list')
#     #return HttpResponse('Книга успешно удалена')



#create_book
class CreateBookView(generic.CreateView):
    template_name = 'books/create_book.html'
    form_class = forms.BookForm
    success_url = '/book_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateBookView, self).form_valid(form=form)


# def create_book_view(request):
#     if request.method == 'POST':
#         form = forms.BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('book_list')
#             #return HttpResponse('Книга успешно добавлена')
#     else:
#         form = forms.BookForm()
#     return render(request, template_name='books/create_book.html', context={'form': form})





#read
class BookListView(generic.ListView):
    template_name =  'books/book_list.html'
    #если вы не хотите указывать свой контекст, то можно использовать стандартный object_list
    context_object_name = 'book'
    model = models.Book

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')




# def books_list_view(request):
#     if request.method == 'GET':
#         #Запрос из базы данных переменная book запрашивает данные у БД
#         book = models.Book.objects.all().order_by('-id')
#         context = {
#             'book': book,
#         }
#         return render(request,
#                       template_name='books/book_list.html',
#                       context=context
#                       )

# получение id и вывод detail
class BookDetailView(generic.DetailView):
    template_name = 'books/book_detail.html'
    model = models.Book
    pk_url_kwarg = 'id'  # если в URL параметр называется 'id'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        book = self.object
        viewed_books = request.session.get("viewed_books", [])
        if book.id not in viewed_books:
            book.views = F("views") + 1
            book.save()
            book.refresh_from_db()

            viewed_books.append(book.id)
            request.session["viewed_books"] = viewed_books
        return response





# def book_detail_view(request, id):
#     if request.method == 'GET':
#         book_id = get_object_or_404(models.Book, id=id)
#         context = {
#             'book_id':book_id,
#         }
#         return render(request, 
#                       template_name='books/book_detail.html',
#                       context=context
#                       )
