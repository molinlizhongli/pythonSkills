# _*_ coding = utf-8 _*_
# @Date : 2021/12/28
# @Time : 13:46
# @NAME ：molin

'''
    英文的可以通过非字母和非数字进行切分，汉字呢？第三方分词组件jieba已经给我们做了切分
    数据集 dataset中的SogouC
'''

import os
import jieba
import  random

def TextProcessing(folder_path,test_size=0.2):
    folder_list = os.listdir(folder_path)
    data_list = []
    class_list = []

    for folder in folder_list:
        new_folder_path = os.path.join(folder_path, folder)
        files = os.listdir(new_folder_path)

        j = 1
        for file in files:
            if j > 100:
                break
            with open(os.path.join(new_folder_path, file), 'r', encoding='utf-8') as f:
                raw = f.read()

            word_cut = jieba.cut(raw, cut_all=False)
            word_list = list(word_cut)

            data_list.append(word_list)
            class_list.append(folder)
            j += 1
        # print(data_list)
        # print(class_list)

    data_class_list = list(zip(data_list, class_list))
    random.shuffle(data_class_list)
    index = int(len(data_class_list)*test_size)+1
    train_list = data_class_list[index:]
    test_list = data_class_list[:index]
    train_data_list, train_class_list = zip(*train_list)
    test_data_list, test_class_list = zip(*test_list)

    all_words_dict = {}
    for word_list in train_data_list:
        for word in word_list:
            if word in all_words_dict.keys():
                all_words_dict[word] += 1
            else:
                all_words_dict[word] = 1
    all_words_tuple_list = sorted(all_words_dict.items(),key=lambda f:f[1],reverse=True)
    all_words_list, all_words_nums = zip(*all_words_tuple_list)
    all_words_list = list(all_words_list)
    return all_words_list,train_data_list,test_data_list,train_class_list,test_class_list

# 函数说明:读取文件里的内容，并去重

    
if __name__ == '__main__':
    folder_path = '../dataset/SogouC/Sample'
    all_words_list,train_data_list,test_data_list,train_class_list,test_class_list = TextProcessing(folder_path,test_size=0.2)
    print(all_words_list)