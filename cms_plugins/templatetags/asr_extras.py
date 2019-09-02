from django import template

register = template.Library()


@register.filter(name='phone_number')
def phone_number(number):
    """Convert a 10 character string into (xxx) xxx-xxxx."""

    return f"({number[0:3]}) {number[3:6]}-{number[6:10]}"


@register.filter(name="linked_phone_number")
def linked_phone_number(number):
    numbers_only = [num for num in number if num.isdigit()]
    numbers_only = "".join(numbers_only)
    phonenumber = phone_number(numbers_only)

    return f"<a href='tel:+1{numbers_only}'>{phonenumber}</a>"
