import glob
from modules import read_data_from_txt_file, sort_strings_in_file, delete_words, convert_array_into_string
from settings import folder_path

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