from django import template

register = template.Library()

@register.filter("add_form_classes")
def add_form_classes(form_field):
    """
    Adds bootstrap classes to form components
    """
    widget = form_field.field.widget
    widget_name = widget.__class__.__name__
    widget_classes = widget.attrs.get("class", "")
    widget_classes = set(widget_classes.split(" ")) if widget_classes else set()
    if widget_name == "Select":
        widget_classes.add("form-select")
    else:
        widget_classes.add("form-control")
    return form_field.as_widget(attrs={"class": " ".join(widget_classes)})


@register.filter("hidden_plate")
def hidden_plate(plate):
    return f"{plate[0]}****{plate[-2:]}"