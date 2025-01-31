import csv
from django.core.management.base import BaseCommand
from api.models import Word

class Command(BaseCommand):
    help = 'Loads words from text files into the database'

    def add_arguments(self, parser):
        parser.add_argument('file_paths', nargs='+', type=str, help='Path to the text files')

    def handle(self, *args, **options):
        for file_path in options['file_paths']:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    reader = csv.reader(file, delimiter=';')
                    # Skip the header row if it exists
                    next(reader, None)
                    for row in reader:
                        if len(row) == 4:
                            word, translation, example, sentenceTranslation = row
                            oxford_list = file_path.split('/')[-1].split('.')[0]
                            Word.objects.create(
                                word=word,
                                translation=translation,
                                example=example,
                                sentenceTranslation=sentenceTranslation,
                                oxford_list=oxford_list
                            )
                            self.stdout.write(self.style.SUCCESS(f'Successfully loaded word: {word} from {oxford_list}'))
                        else:
                            self.stdout.write(self.style.WARNING(f'Skipping row in {file_path} due to incorrect format: {row}'))
            except FileNotFoundError:
                self.stdout.write(self.style.ERROR(f'File not found: {file_path}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error loading file {file_path}: {e}'))