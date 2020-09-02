from django import template

register = template.Library()

@register.filter(name='cutter') # Use of decorator :D
def cut_string(value, arg):
    """
    This function cuts out the arg from the string
    """
    return value.replace(arg, '')

# register.filter('cutter', cut_string)
