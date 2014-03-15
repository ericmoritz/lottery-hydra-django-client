from django.template import Library, defaultfilters
from django.utils.translation import ungettext
from django.conf import settings

register = Library()

# A tuple of standard large number to their converters
intword_converters = (
    (6, lambda number: (
        ungettext('%(value).1f mil', '%(value).1f mil', number),
        ungettext('%(value)s mil', '%(value)s mil', number),
    )),
    (9, lambda number: (
        ungettext('%(value).1f bil', '%(value).1f bil', number),
        ungettext('%(value)s bil', '%(value)s bil', number),
    ))
)

@register.filter(is_safe=False)
def format_jackpot(value):
    """
    Converts a large integer to a friendly text representation. Works best
    for numbers over 1 million. For example, 1000000 becomes '1.0 million',
    1200000 becomes '1.2 million' and '1200000000' becomes '1.2 billion'.
    """
    try:
        value = int(value)
    except (TypeError, ValueError):
        return value

    if value < 1000000:
        return value

    def _check_for_i18n(value, float_formatted, string_formatted):
        """
        Use the i18n enabled defaultfilters.floatformat if possible
        """
        if settings.USE_L10N:
            value = defaultfilters.floatformat(value, 1)
            template = string_formatted
        else:
            template = float_formatted
        return template % {'value': value}

    for exponent, converters in intword_converters:
        large_number = 10 ** exponent
        if value < large_number * 1000:
            new_value = value / float(large_number)
            converted_value = _check_for_i18n(new_value, *converters(new_value))
            if '.0' in converted_value:
            	converted_value = converted_value.replace('.0','')

            return converted_value

    return value
