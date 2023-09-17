from modules.bulk_delete import deleteWordsInBulk
from settings.deleted_words import deleted_words
from settings.path import path_to_txtFolder

print('start execution')
deleteWordsInBulk(deleted_words, path_to_txtFolder)