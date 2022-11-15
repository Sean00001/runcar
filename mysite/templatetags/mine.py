# from django import template
# from django.utils.safestring import mark_safe
# register = template.Library()
#
# @register.filters
# def select(value):
#     """Removes all values of arg from the given string"""
#     Photo = Photo.objects.filter(car=value)
#     Photos = Photo.objects.get(image)
#     return Photos
#
# <!--{% load mine %}-->
#
# <!--                      <div class="carousel-item">-->
# <!--                         <img src={{Cars|select}} class="d-block w-100 h-100" alt="...">-->
# <!--                      </div>-->