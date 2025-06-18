
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group


class Command(BaseCommand):
    help = "створює тестових користувачів та призначає їм групи доступу"

    def add_arguments(self, parser):
        parser.add_argument(
            "-p", "--password",
            type=str,
            required=True,
            help="пароль для всіх тестових користувачів"
        )

    def handle(self, *args, **options):
        password = options["password"]

        users_info = [
            ("cashier", "Касир"),
            ("consultant", "Продавець-консультант"),
            ("accountant", "Бухгалтер"),
        ]

        for username, group_name in users_info:
            user, created = User.objects.get_or_create(username=username)
            user.set_password(password)
            user.is_staff = True
            user.save()

            group = Group.objects.get(name=group_name)
            user.groups.clear()
            user.groups.add(group)

            action = "створено" if created else "оновлено"
            self.stdout.write(f"\nкористувача '{username}' {action} та додано до групи '{group_name}'\nпароль: {password}")

        self.stdout.write(self.style.SUCCESS("тестові користувачі успішно зареєстровані"))
