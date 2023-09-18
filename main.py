from modules.modules import deleteWordsInBulk
from settings.settings import strings_to_remove, folder_path


print('start execution')
deleteWordsInBulk(strings_to_remove, folder_path)