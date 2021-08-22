from django import template
from django.contrib.auth.models import User

register = template.Library()


@register.filter
def model_name(obj):
    try:
        return obj._meta.model_name
    except AttributeError:
        return None


@register.filter
def user_perms(user: User):
    if user.is_active:
        res_perms = (
            "prodil.change_resource",
            "prodil.view_resource",
            "prodil.add_resource",
            "prodil.delete_resource",
        )
        if any(i in res_perms for i in user.get_user_permissions()):
            print(True)
            return True
        return False
    pass
