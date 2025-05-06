from django.shortcuts import redirect
from django.conf import settings
from django.urls import resolve

class LoginRequiredMiddleware:
    """
    Middleware для запрета доступа к сайту без авторизации.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.allowed_urls = [
            'login',
            'logout',
            'register',
            'admin:login',
            'admin:logout',
            'password_reset',
            'password_reset_done',
            'password_reset_confirm',
            'password_reset_complete',
            # Добавь сюда свои публичные страницы если надо
        ]

    def __call__(self, request):
        # Разрешить доступ к статическим файлам
        if request.path.startswith(settings.STATIC_URL) or request.path.startswith('/admin/'):
            return self.get_response(request)

        # Если пользователь не аутентифицирован и запрашивает неразрешённую страницу
        if not request.user.is_authenticated:
            current_url = resolve(request.path_info).url_name
            if current_url not in self.allowed_urls:
                return redirect(settings.LOGIN_URL)

        return self.get_response(request)