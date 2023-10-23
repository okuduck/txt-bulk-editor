import glob
import sys
import os

# pucacheを生成しないように設定
sys.dont_write_bytecode = True

from modules import read_data_from_txt_file, sort_strings_in_file, delete_words, convert_array_into_string
from modules_for_change_scale import downscale_images
from dotenv import load_dotenv

# .envから設定情報を取得
load_dotenv()
folder_path = os.getenv('PATH_TO_TAG_FOLDER')
path_to_split_commandline = os.getenv('PATH_TO_SPLIT_COMMANDLINE')

def delete_words_from_txt():
    print('start execution')
    deleted_strings_path = 'deleted_strings.txt'
    remained_strings_path = 'remained_strings.txt'
    strings_to_remove_path = 'strings_to_remove.txt'

    # 削除する単語の配列を生成
    strings_to_remove = read_data_from_txt_file(strings_to_remove_path)
    remained_array = []
    deleted_array = read_data_from_txt_file(deleted_strings_path)
    # print('strings_to_remove', strings_to_remove)

    # 各ファイルの単語を削除
    txt_files = glob.glob(folder_path + '/*.txt')
    for txt_file in txt_files:
        try:
            with open(txt_file, "r") as file:
                contents_list = file.read().split(",")
                editted_contents_list = [c.strip() for c in contents_list]

                # 元ファイルの配列から、指定した単語を削除
                result = delete_words(arr1 = editted_contents_list, arr2 = strings_to_remove) 
                for word in result.remained:
                    remained_array.append(word)
                for word in result.deleted:
                    deleted_array.append(word)
            
                # ファイルの上書き
                with open(txt_file, 'w') as outfile:
                    editted_array = [o.strip() for o in result.remained]
                    new_string = ', '.join([str(item) for item in editted_array])
                    outfile.write(new_string)

        except FileNotFoundError:
            print(f"ファイル '{txt_file}' が見つかりません。")

    with open(remained_strings_path, 'w') as outfile:
        remained_string = convert_array_into_string(remained_array)
        outfile.write(remained_string)
    with open(deleted_strings_path, 'w') as outfile:
        deleted_string = convert_array_into_string(deleted_array)
        outfile.write(deleted_string)

    # # stringsファイルのソート、重複する単語の削除
    sort_strings_in_file(file_path = deleted_strings_path)
    sort_strings_in_file(file_path = remained_strings_path)
    sort_strings_in_file(file_path = strings_to_remove_path)

def delete_txt_files():
    print('start execution')
    file_list = os.listdir(folder_path)
    print('file_list', file_list)

    for filename in file_list:
        # ファイルが.txt拡張子を持つ場合にのみ削除
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            os.remove(file_path)

def join_commandline():
    
    with open(path_to_split_commandline, "r") as commandline_file:
        commandline_list = commandline_file.read().strip().split("\n")
        stripped_list = []
        for string in commandline_list:
            stripped_list.append(string.strip())
        commandline_string = " ".join(stripped_list)
        print('commandline_string: ', commandline_string)

# どの関数を実行するか
if len(sys.argv) != 2:
    print("使い方: python main.py {関数名}")
else:
    function_name = sys.argv[1]
    if function_name == 'delete_txt_files':
        delete_txt_files()
    elif function_name == 'delete_words_from_txt':
        delete_words_from_txt()
    elif function_name == 'join_commandline':
        join_commandline()
    elif function_name == 'downscale_images':
        downscale_images(folder_path, folder_path, 512)
    elif function_name == 'upscale_images':
        downscale_images(folder_path, folder_path, 1024)
    else:
        print("指定した関数が見つかりません")