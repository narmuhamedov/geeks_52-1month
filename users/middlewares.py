from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest

child_club = 'Детский клуб'
teenager_club = 'Подростковый клуб'
adult_club = 'Взрослый клуб'

############
class AgeClubMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            age = int(request.POST.get('age'))
            if age < 7:
                return HttpResponseBadRequest('age must be at least 7')
            elif age >= 7 and age < 12:
                request.club = child_club
            elif age >= 12 and age < 18:
                request.club = teenager_club
            elif age >= 18 and age <= 60:
                request.club = adult_club
            else:
                return HttpResponseBadRequest('Вы слишком опытны вам это покажется скучным')
        elif request.path == '/register/' and request.method == 'GET':
            setattr(request, 'club', 'клуб не определен')
