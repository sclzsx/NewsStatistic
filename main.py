# 以一个社区为单位，关键词出现的新闻篇数占该社区总新闻篇数的比例
import numpy as np
import pandas as pd

# df1 = np.array(pd.read_excel('community_news.xlsx', sheet_name='社区新闻原始数据'))
# df2 = np.array(pd.read_excel('community_news.xlsx', sheet_name='结果'))
#
# names2 = df2[:,1]
# total_nums2 = df2[:,2]
#
# names1 = df1[:,2]
# contents1 = df1[:,5]
# print(contents1)

import docx

# 获取文档对象
file = docx.Document("keywords.docx")
# print("段落数:" + str(len(file.paragraphs)))  # 段落数为13，每个回车隔离一段


# key_country, key_company, key_public, key_others = [], [], [], []
# keywords = [key_country, key_company, key_public, key_others]
keywords = []
k = 0
tmp = []
for i in range(len(file.paragraphs)):
    text = file.paragraphs[i].text
    tmp.append(text)

    if len(text) == 0:
        k = k + 1
        keywords.append(tmp)
        tmp = []

keywords[0] = keywords[0]
print(keywords[0])
if __name__ == '__main__':
    pass
