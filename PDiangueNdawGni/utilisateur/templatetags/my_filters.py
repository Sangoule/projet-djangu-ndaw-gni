from django import template

register = template.Library()

@register.filter(name='round_to_int')
def round_to_int(value):
    try:
        return int(round(float(value)))
    except (ValueError, TypeError):
        return value
