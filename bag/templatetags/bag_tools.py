from django import template


# bag tools price calcalutor dependency

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
