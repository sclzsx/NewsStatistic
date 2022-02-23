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

# # 输出每一段的内容
# for para in file.paragraphs:
#     print(para.text)

# 输出段落编号及段落内容
key_country = []
for i in range(len(file.paragraphs)):
    text = file.paragraphs[i].text
    keywords = []
    keywords.append(text)
    if len()
    # print("第" + str(i) + "段的内容是：" + file.paragraphs[i].text)

if __name__ == '__main__':
    pass
