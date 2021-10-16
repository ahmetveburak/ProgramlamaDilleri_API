from django.conf import settings
from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    def handle(self, *args, **options):
        if settings.DEBUG is False:
            self.stderr.write(self.style.ERROR("You must enable DEBUG mode to run this command."))
            return

        fixtures = [  # order is important!
            "user",
            "author",
            "category",
            "resource",
        ]
        for fixture in fixtures:
            self.stdout.write(f"Inserting fixture '{fixture}'...")
            call_command(
                "loaddata",
                f"fixtures/{fixture}",
                format="yaml",
            )
