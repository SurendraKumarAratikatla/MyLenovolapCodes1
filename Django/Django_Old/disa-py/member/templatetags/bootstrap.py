from django.template import Context
from django.template.loader import get_template
from django import template

register = template.Library()

@register.filter
def bootstrap(element):
    element_type = element.__class__.__name__.lower()
    #print element, element_type
    if element_type == 'boundfield':
        template = get_template("bootstrapform/field.html")

        context = Context({'field': element})
    else:
        has_management = getattr(element, 'management_form', None)
        if has_management:
            template = get_template("bootstrapform/formset.html")
            context = Context({'formset': element})
        else:
            template = get_template("bootstrapform/form.html")
            context = Context({'form': element})
    print context
    return template.render(context)

@register.filter
def is_checkbox(field):
    return field.field.widget.__class__.__name__.lower() == "checkboxinput"


@register.filter
def is_radio(field):
    return field.field.widget.__class__.__name__.lower() == "radioselect"


@register.filter
def cus_date(value):
    import datetime as dtime
    from datetime import datetime
    if not value:
        return None
    if type(value) is dtime.date:
        return value
    try:
        the_date = datetime.strptime(value, "%Y-%m-%d")
    except ValueError:
        the_date = datetime.strptime(value, "%d %B, %Y")
    return the_date

@register.filter
def cus_datetime(value):
    import datetime as dtime
    from datetime import datetime
    if not value:
        return datetime.now()
    if type(value) is dtime.datetime:
        return value
    try:
        the_date = datetime.strptime(value, "%Y-%m-%d %H:%M")
    except ValueError:
        the_date = datetime.strptime(value, "%d %B, %Y %H:%M")
