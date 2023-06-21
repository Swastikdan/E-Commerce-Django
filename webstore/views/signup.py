'''
The Signup class is a Django view that handles user sign up requests, validates user input, and
creates a new customer object if the input is valid.

This code defines a Signup class that inherits from Django's View class. It handles GET and POST requests for the signup view. The GET request renders the signup.html template. The POST request processes the submitted form data, creates a new Customer instance, and validates the customer data. If the validation passes, the customer's password is hashed, and the customer is registered. If the validation fails, an error message is displayed, and the user is returned to the signup form.

'''
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from webstore.models.customer import Customer
from django.views import View

# Signup class, inherits from Django's View class
class Signup(View):
    # Handles GET requests for the signup view
    def get(self, request):
        return render(request, 'signup.html')

    # Handles POST requests for the signup view
    def post(self, request):
        """
        This is a Python function that handles a POST request for user registration, validates the input
        data, creates a new customer instance, hashes the password, and registers the customer.
        
        :param request: The HTTP request object that contains information about the current request, such
        as the HTTP method, headers, and data
        :return: The code returns a redirect to the homepage if the customer instance is validated and
        registered successfully. If validation fails, it returns a render of the signup template with an
        error message and the values entered by the user.
        """
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        # Validation values
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        error_message = None

        # Create a new customer instance
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)

        # Validate the customer instance
        error_message = self.validateCustomer(customer)

        if not error_message:
            # If validation passes, hash the password and register the customer
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            # If validation fails, return the error message and values to the signup template
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    # Validate the customer instance, checking for required fields and certain length constraints
    def validateCustomer(self, customer):
        """
        This function validates customer information and returns an error message if any of the fields are
        missing or do not meet the required criteria.
        
        :param customer: The customer parameter is an object that contains information about a customer,
        such as their first name, last name, phone number, password, and email address. The function is
        designed to validate this information and return an error message if any of the information is
        missing or does not meet certain criteria
        :return: an error message if any of the validation checks fail, otherwise it returns None.
        """
        error_message = None
        if (not customer.first_name):
            error_message = "Please Enter your First Name !!"
        elif len(customer.first_name) < 3:
            error_message = 'First Name must be 3 char long or more'
        elif not customer.last_name:
            error_message = 'Please Enter your Last Name'
        elif len(customer.last_name) < 3:
            error_message = 'Last Name must be 3 char long or more'
        elif not customer.phone:
            error_message = 'Enter your Phone Number'
        elif len(customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(customer.password) < 5:
            error_message = 'Password must be 5 char long'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'

        return error_message

