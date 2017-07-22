from django import template

register = template.Library()

# REGISTER FILTER WITH DECORATORS
@register.filter(name='cut')

def cut(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')

# REGISTER WITH DEFULT WAY
# register.filter('cut', cut)
