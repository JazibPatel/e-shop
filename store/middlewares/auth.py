from django.shortcuts import render,redirect

def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        
        returnUrl = request.META['PATH_INFO']
        print(returnUrl)
        if not request.session.get('customer_id'):

            return redirect(f'login?return_url={returnUrl}')
       

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware