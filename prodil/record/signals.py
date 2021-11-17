from django.db.models import F
from django.db.models.signals import pre_save
from django.dispatch import receiver

from prodil.record.models import Category


@receiver(pre_save, sender=Category, dispatch_uid="reorder-category")
def reorder(sender, instance: Category, **kwargs):
    if kwargs.get("raw"):
        # prevent fixture installing fail
        return

    if instance.id:
        pre_obj = Category.objects.get(id=instance.id)
        if pre_obj.order > instance.order:
            sender.objects.exclude(order__gte=pre_obj.order).exclude(order__lt=instance.order).update(
                order=F("order") + 1
            )
            return

        sender.objects.exclude(order__lte=pre_obj.order).exclude(order__gt=instance.order).update(order=F("order") - 1)
