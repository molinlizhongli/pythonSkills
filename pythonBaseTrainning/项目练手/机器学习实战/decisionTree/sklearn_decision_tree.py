# _*_ coding = utf-8 _*_
# @Date : 2021/12/10
# @Time : 13:22
# @NAME ：molin


from sklearn.preprocessing import  LabelEncoder, OneHotEncoder
from six import StringIO
from sklearn import tree

import pandas as pd
import  numpy as np
import  pydotplus

if __name__ == '__main__':
    # 加载文件
    with open('../dataset/decision_tree_lenses.txt','r')as f:
        # 处理数据
        lenses = [inst.strip().split('\t') for inst in f.readlines()]
    # 提取每组数据的类别，放在列表中
    lenses_target = []
    for each in lenses:
        lenses_target.append(each[-1])
    # print(lenses_target)
    # 特征标签
    lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
    # 保存lenses数据的临时列表
    lenses_list = []
    # 保存lenses数据的字典，用于生成pandas
    lenses_dict = {}
    # 提取信息，生成字典
    for each_label in lensesLabels:
        for each in lenses:
            lenses_list.append(each[lensesLabels.index(each_label)])
        lenses_dict[each_label] = lenses_list
        lenses_list = []
    # print(lenses_dict)
    # 生成pandas数据帧
    lenses_pd = pd.DataFrame(lenses_dict)
    # print(lenses_pd)
    # 创建LabelEncoder对象，用于序列化
    le = LabelEncoder()
    # 为每一列进行序列化，转成容易被计算机识别的字符
    for col in lenses_pd.columns:
        lenses_pd[col] = le.fit_transform(lenses_pd[col])
    # print(lenses_pd)

    # 创建决策树分类算法类
    clf = tree.DecisionTreeClassifier(max_depth=4)
    # 使用数据，构建决策树
    clf = clf.fit(lenses_pd.values.tolist(), lenses_target)

    dot_data = StringIO()
    # 绘制决策树
    tree.export_graphviz(clf, out_file=dot_data,
                         feature_names=lenses_pd.keys(),
                         class_names=clf.classes_,
                         filled=True,
                         rounded=True,
                         special_characters=True)
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    # 保存决策树结果，存放pdf中
    graph.write_pdf("tree.pdf")
    print(clf.predict([[1, 1, 1, 0]]))
