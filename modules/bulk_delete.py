import glob
from settings.deleted_words import deleted_words

# 現在のディレクトリ内のすべての.txtファイルを取得
txt_files = glob.glob('*.txt')
strings_to_remove = deleted_words

def deleteWordsInBulk(strings_to_remove, ):
    # テキストファイルを順番に読み込む
    for txt_file in txt_files:
        with open(txt_file, 'r') as file:
            # new_string_array = []
            # deleted_words = []
            file_contents = file.read()

            # 文字列の分割
            contents_list = file_contents.split(",")

            # 各文字列の前後の空白を削除
            editted_contents_list = [c.strip() for c in contents_list] 


            
            # 指定した単語を含む文字列を削除
            # まず元の配列の文字列と削除する文字列の比較
            # for string in strings_to_remove: # red
            #     for content in editted_contents_list:
            #         print('editted_contents_list', editted_contents_list)
            #         if string not in content:
            #             # 新しく生成する配列に追加する文字列が含まれているかどうかを確認
            #             print('string', string)
            #             print('content', content)
            #             print(new_string_array)
            #             if len(new_string_array) == 0:
            #                 new_string_array.append(content)
            #             else:
            #                 if content not in new_string_array:
            #                     new_string_array.append(content)
                                
            def remove_partial_matches(arr1, arr2):
                result = []
                for item1 in arr1:
                    is_partial_match = False
                    for item2 in arr2:
                        if item2 in item1:
                            is_partial_match = True
                            break
                    if not is_partial_match:
                        result.append(item1)
                return result
            
            filtered_array = remove_partial_matches(editted_contents_list, strings_to_remove)
            # print('filtered_array', filtered_array)

            # 各文字列の前後の空白を削除
            # print('new_string_array', new_string_array)
            stripped_editted_list = [n.strip() for n in filtered_array]
            new_contents = ', '.join([str(item) for item in stripped_editted_list])
            
            # filtered_array = [item for item in editted_contents_list if not any(re.search(re.escape(item), string) for string in strings_to_remove)]
            # print('filtered_array', filtered_array)
            
            # ファイルの更新
            with open(txt_file, 'w') as file:
                file.write(new_contents)

    # def ggg():
    #     # コマンドライン引数(2つ目以降を取得
    #     x=sys.argv[1:]
    #     print("値",x)
    #     print("型",type(x))
        
    # if __name__=='__main__':
    #     ggg()
