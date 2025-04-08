from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Test if the Command class is loaded correctly.'

    def handle(self, *args, **kwargs):
        self.stdout.write('Command class loaded successfully.')
