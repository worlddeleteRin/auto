from django import template

from lamp.models import Category, Lamps, Type, Cars, Destination

register = template.Library()

@register.filter(name='key')
def key(d, key_name):
    return d[key_name]

@register.simple_tag
def cat_type_dist(category):
    lamps = category.lamps_set.all()
    types = lamps.values('ltype__name').distinct()
    return {'types': types,}

@register.simple_tag
def cat_brand_dist(category): 
    lamps = category.lamps_set.all()
    brands = lamps.values('brand__name').distinct()
    return {'brands': brands}

@register.simple_tag
def lamp_features(lamp):
    f = lamp.feature
    f = eval(f)
    f = f[0]
    return f

@register.simple_tag
def lamp_ftag(ftag):
    ftag = ftag.replace(" ", "_")
    return ftag



