   
# The above code defines two custom filters for Django templates, one to format a number as currency
# and another to multiply two numbers.
    
# :param number: The first parameter of the "currency" filter function, which represents a number that
# needs to be formatted as a currency
# :return: The `currency` filter returns a string that concatenates the string "Rs " with the input
# `number` converted to a string.
   
from django import template
register = template.Library()

@register.filter(name='currency')
def currency(number):
    return "Rs "+str(number)


@register.filter(name='multiply')
def multiply(number , number1):
    return number * number1

