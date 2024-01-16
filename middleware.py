# middleware.py

from django.http import HttpResponse

class AllowIframingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.META.get('HTTP_REFERER') and 'ui.dev/amiresponsive' in request.META['HTTP_REFERER']:
            response['X-Frame-Options'] = 'ALLOW-FROM https://ui.dev/amiresponsive'
        return response
