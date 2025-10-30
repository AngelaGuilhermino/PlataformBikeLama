from django.shortcuts import redirect

class AdminLoginNextMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # If the admin login page is requested without a next parameter, add next=/
        if request.path == '/admin/login/' and request.method == 'GET' and 'next' not in request.GET:
            return redirect(f'{request.path}?next=/')
        return self.get_response(request)
