from django import template
from store.models import Language

register = template.Library()


@register.filter
def get_lang(value, language):
    lang = Language.objects.filter(name=language).first()
    elem = value.filter(lang=lang)
    return elem


@register.simple_tag
def translate_prod(product, language, field):

    lang = Language.objects.filter(name=language).first()

    if lang:
        elem = product.producttranslation_set.filter(product=product, lang=lang.id, field=field).first()

        if elem is not None:
            return elem

        lang = Language.objects.get(name='en')
        return product.producttranslation_set.filter(product=product, lang=lang.id, field=field).first()

    lang = Language.objects.get(name='en')
    return product.producttranslation_set.filter(product=product, lang=lang.id, field=field).first()\


@register.simple_tag
def translate_property(property, language, field):

    lang = Language.objects.filter(name=language).first()

    if lang:
        elem = property.propertytranslation_set.filter(property=property, lang=lang.id, field=field).first()

        if elem is not None:
            return elem.value

        lang = Language.objects.get(name='en')
        return property.propertytranslation_set.filter(property=property, lang=lang.id, field=field).first()

    lang = Language.objects.get(name='en')
    return property.propertytranslation_set.filter(property=property, lang=lang.id, field=field).first()


@register.simple_tag
def translate_tag(tag, language):

    lang = Language.objects.filter(name=language).first()

    if lang:
        elem = tag.tagtranslation_set.filter(tag=tag, lang=lang.id).first()

        if elem is not None:
            return elem.value

        lang = Language.objects.get(name='en')
        return tag.tagtranslation_set.filter(tag=tag, lang=lang.id).first()

    lang = Language.objects.get(name='en')
    return tag.tagtranslation_set.filter(tag=tag, lang=lang.id).first()
