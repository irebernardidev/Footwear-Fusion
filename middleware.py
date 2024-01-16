from django.http import HttpResponse


class AllowIframingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.META.get('HTTP_ORIGIN') == 'https://ui.dev/amiresponsive':
            response = HttpResponse()
            response['X-Frame-Options'] = 'allow-from https://ui.dev/amiresponsive'

        response = self.get_response(request) 
        return response