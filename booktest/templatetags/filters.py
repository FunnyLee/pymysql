from django.template import Library

register = Library()


@register.filter
def mod(value, num):
    '''自定义过滤器'''
    return value % num == 0
