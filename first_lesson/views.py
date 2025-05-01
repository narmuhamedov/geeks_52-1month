from django.shortcuts import render

def fist_page_view(request):
  if request.method == 'GET':

    context = {
      'emoji': "🥺",
      'text': 'Привет это мой первый урок на Django',
      'run_string': 'Hello World'
      }
    return render(request, template_name='index.html', context=context)
    
