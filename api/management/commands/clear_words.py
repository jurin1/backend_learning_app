from django.core.management.base import BaseCommand
from api.models import Word

class Command(BaseCommand):
    help = 'Clears all words from the database'

    def handle(self, *args, **options):
        Word.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully cleared all words from the database'))