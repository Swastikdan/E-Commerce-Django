
# This is a middleware function in Django that checks if a user is authenticated and redirects them to
# the login page if not.
    
# :param get_response: get_response is a parameter that represents the next middleware or view
# function in the Django middleware chain. It is a callable that takes a request object and returns a
# response object. The auth_middleware function wraps this callable with its own functionality to
# perform authentication checks before passing the request to the next middleware or view
# :return: The auth_middleware function returns the middleware function.

from django.shortcuts import redirect
def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        print(request.session.get('customer'))
        returnUrl = request.META['PATH_INFO']
        print(request.META['PATH_INFO'])
        if not request.session.get('customer'):
           return redirect(f'login?return_url={returnUrl}')

        response = get_response(request)
        return response

    return middleware