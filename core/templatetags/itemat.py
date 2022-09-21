from django import template

register = template.Library()


@register.filter(name="itemat")
def itemat(dict, key):
    return dict[key]
