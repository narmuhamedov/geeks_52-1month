from django.shortcuts import render

def fist_page_view(request):
  if request.method == 'GET':

    context = {
      'emoji': "🥺",
      'text': 'Привет это мой первый урок на Django',
      'run_string': '[05/May/2025 11:43:04] "GET /static/css/header_and_footer/menu.css HTTP/1.1" 200 794'
      }
    return render(request, template_name='index.html', context=context)
    
