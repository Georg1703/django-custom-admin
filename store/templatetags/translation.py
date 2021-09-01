from django import template

register = template.Library()


@register.filter
def translate(value):
    return value.producttranslation_set.filter(product=value, lang_id=1)