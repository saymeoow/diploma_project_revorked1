from datetime import datetime, time

from django.shortcuts import redirect


class PathMethodTimeMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        timee = datetime.now()

        response = self.get_response(request)

        print(f'Путь запроса: {request.path}\n'
              f'Метод запроса: {request.method}\n'
              f'Время обработки запроса: {timee}')
        return response


class IsAuthenticateMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated or request.path == '/auth/login/' or request.path == '/auth/register/':
            ...
        else:
            return redirect('/auth/login/')
        return response

