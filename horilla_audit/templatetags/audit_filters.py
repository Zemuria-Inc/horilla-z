from django import template
from django.core.paginator import Page, Paginator
from django.template.defaultfilters import register

from employee.models import Employee, EmployeeWorkInformation


@register.filter(name="fk_history")
def fk_history(instance, change):
    """
    This method is used to return str of the fk fields
    """
    value = "Deleted"
    try:
        value = getattr(instance, change["field_name"])
    except:
        value = instance.__dict__[change["field_name"] + "_id"]
        value = str(value) + f" (Previous {change['field']} deleted)"
        pass
    return value
