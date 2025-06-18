
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from electronic_store.models import Order, Invoice


@receiver(post_migrate)
def create_permissions(**kwargs) -> None:
    """
    Створює групи користувачів і призначає їм відповідні права доступу після міграції

    Права доступу визначені в словнику `permissions`, де ключі — назви груп, а значення —
    словники моделей і списки дій, які дозволені для цих груп

    :param kwargs: Додаткові аргументи сигналу post_migrate (не використовуються)
    :return: None
    """

    permissions = {
        "Касир": {
            Order: ["add", "change", "view"],
            Invoice: ["add", "view"]
        },
        "Продавець-консультант": {
            Order: ["change", "view"],
        },
        "Бухгалтер": {
            Order: ["view"],
            Invoice: ["view"],
        }
    }

    for group_name, group_permissions in permissions.items():
        group, _ = Group.objects.get_or_create(name=group_name)
        for model, actions in group_permissions.items():
            content_type = ContentType.objects.get_for_model(model)
            for action in actions:
                permission, _ = Permission.objects.get_or_create(
                    codename=f"{action}_{model._meta.model_name}",
                    name=f"Can {action} {model._meta.verbose_name}",
                    content_type=content_type
                )
                group.permissions.add(permission)