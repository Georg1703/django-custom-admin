from django import template
from store.models import Language

register = template.Library()


@register.simple_tag
def translate(product, language, field):

    lang = Language.objects.filter(name=language).first()

    if lang:
        elem = product.producttranslation_set.filter(product=product, lang=lang.id, field=field).first()

        if elem is not None:
            return elem

        lang = Language.objects.get(name='en')
        return product.producttranslation_set.filter(product=product, lang=lang.id, field=field).first()

    lang = Language.objects.get(name='en')
    return product.producttranslation_set.filter(product=product, lang=lang.id, field=field).first()
