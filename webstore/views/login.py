"""
This is a Django view for handling user login and logout functionality, including session management
and password authentication.
    
:param request: The HTTP request object that contains information about the current request,
including any data submitted in the request
:return: The code is defining two views - `Login` and `logout`.


This code defines a Login view class that inherits from Django's View class. It handles both GET and POST requests for the login view. The GET request renders the login page, while the POST request processes the submitted login form. If the email and password match a customer in the database, the customer's ID is stored in the session, and the user is redirected to the return URL or the homepage. If the email or password is incorrect, an error message is displayed on the login page. The logout function clears the session data and redirects the user to the login page.

"""
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from webstore.models.customer import Customer
from django.views import View

# Login view class, inherits from Django's View class
class Login(View):
    # Class variable to store the return URL after successful login
    return_url = None

    # Handles GET requests for the login view
    def get(self, request):
        # Get the return URL from the request's GET parameters
        Login.return_url = request.GET.get('return_url')
        # Render the login.html template and return it as a response
        return render(request, 'login.html')

    # Handles POST requests for the login view
    def post(self, request):
        # Get the email and password from the request's POST data
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Get the customer object by email
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            # Check if the provided password matches the customer's password
            flag = check_password(password, customer.password)
            if flag:
                # Store the customer's ID in the session
                request.session['customer'] = customer.id

                # Redirect to the return URL if it's set, otherwise redirect to the homepage
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage_or_webstore')
            else:
                error_message = 'Invalid !!'
        else:
            error_message = 'Invalid !!'
        # Render the login.html template with the error message and return it as a response
        return render(request, 'login.html', {'error': error_message})

# Function to handle user logout
def logout(request):
    # Clear the session data
    request.session.clear()
    # Redirect to the login page
    return redirect('login')
