import glob
import os
import re

# 単語の削除
class DeletedWordsValues:
    def __init__(self, value1, value2):
        self.remaained = value1
        self.deleted = value2
def delete_words(arr1, arr2):
    remained = []
    deleted = []
    for item1 in arr1:
        item1 = item1.strip()
        if item1:
            is_partial_match = False
            for item2 in arr2:
                item2 = item2.strip()
                if item1 == item2:
                    is_partial_match = True
                    deleted.append(item1)
                    break
                # else:
                #     text = item1
                #     pattern = r'\b' + re.escape(item2) + r'\b'
                #     match = re.search(pattern, text)
                #     if match:
                #         is_partial_match = True
                #         deleted.append(item1)
                #         break
            if not is_partial_match:
                remained.append(item1)
    editted_deleted = remove_duplicate_elements(deleted)
    return DeletedWordsValues(remained, editted_deleted)
            
# ファイルからデータを読み取り、コンマごとに改行してリストに格納する関数
def read_data_from_txt_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read().strip()  # ファイルからテキストを読み取る
            data_list = data.split('\n')  # 改行文字で分割してリストに変換
            data_list = [item.strip(',') for item in data_list]  # コンマを削除
            return data_list
    except FileNotFoundError:
        print(f"ファイル '{file_path}' が見つかりません。")

# 重複する単語の削除と、アルファベット順への並び替え
def sort_strings_in_file(file_path):
    with open(file_path, 'r') as file:
        original = file.read().split('\n')
        stripped_list = [o.strip() for o in original]
        editted_list = remove_duplicate_elements(stripped_list)
        sorted_list = sorted(editted_list)
        with open(file_path, 'w') as outfile:
            for sorted_word in sorted_list:
                outfile.write(sorted_word + '\n')
    
# リストの重複する要素を削除
def remove_duplicate_elements(original_list):
    unique_list = []
    [unique_list.append(item) for item in original_list if item not in unique_list]
    return unique_list

# 配列の各要素を整形して、改行で文字列に変換
def convert_array_into_string(original):
    editted_array = [o.strip() for o in original]
    new_string = '\n'.join([str(item) for item in editted_array])
    return new_string
