from django import template

register = template.Library()

@register.filter(name='format_rupiah')
def rupiah(value):
    try:
        value = float(value)
        return "Rp{:,.0f}".format(value).replace(",", "X").replace(".", ",").replace("X", ".")
    except:
        return value