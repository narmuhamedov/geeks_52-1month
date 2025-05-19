from django.shortcuts import redirect
from django.views import generic
from django.http import HttpResponse
from . import models, forms

class RezkaListView(generic.ListView):
    template_name = 'parser_library/parser_book_list.html'
    context_object_name = 'rezka'
    model = models.Parser_Rezka

    def get_queryset(self):
        return self.model.objects.all()

#Общая форма для парсинга не зависимо какой сайт мы парсим
class ParserForm(generic.FormView):
    template_name = 'parser_library/parser_form.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('<h1>Парсинг успешно завершен!!!</h1>')
        else:
            return super(ParserForm, self).post(request, *args, **kwargs)

