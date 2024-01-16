# middleware.py

from django.http import HttpResponse

class AllowIframingFromAmIResponsiveMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = HttpResponse()
        
        if request.META.get('HTTP_REFERER') and 'amiresponsive.ui.dev' in request.META['HTTP_REFERER']:
            response['X-Frame-Options'] = 'ALLOW-FROM https://ui.dev/amiresponsive'

        response = self.get_response(request) 
        return response