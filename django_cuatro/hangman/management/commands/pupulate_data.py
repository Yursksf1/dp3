# -*- coding: utf-8 -*-

# Django
from django.core.management.base import BaseCommand
from hangman.models import Word

import csv


class Command(BaseCommand):
    def handle(self, *args, **options):
        path = './hangman/management/commands/data_import.csv'
        is_first_row = True
        count_of_word_added = 0
        count_of_row = 0

        with open(path, newline='') as csvfile:
            spam_reader = csv.reader(csvfile, delimiter=';')
            for row in spam_reader:
                print(row[0] + ' - ' + row[1])

                count_of_row = count_of_row + 1
                if is_first_row:
                    is_first_row = False
                else:
                    w = Word()
                    w.hidden_word = row[1]
                    w.clue = row[0]
                    w.save()
                    count_of_word_added = count_of_word_added + 1

        print('numero de registros en el archivo', count_of_row)
        print('numero de registros de word agregados el archivo', count_of_word_added)

