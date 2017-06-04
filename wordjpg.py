# -*- coding: utf-8 -*-
import os
import jieba
import jieba.analyse
import numpy as np
from PIL import Image
from wordcloud import WordCloud
#引入字体文件
font=os.path.join(os.path.dirname(__file__), "DroidSansFallbackFull.ttf")
f = open("index_des.txt", "r")
book = f.read()
f.close()
def cut():
    #自定义jieba字典
    word = ['爬虫','较强','较好','后端','高新','大数据']
    for seg in word:
        jieba.add_word(seg, True)
    #print seg_list[0]
    findword = jieba.analyse.extract_tags(book, topK = 100, withWeight=True)
    list1 = []
    list2 = []
    for wb, weight in findword:
        list1.append(wb)
        list2.append(weight)
    dict_word = dict(zip(list1, list2))
    #print dict_word
    return dict_word
def cloud(dict_word):
    #word_cloud = WordCloud().generate_from_frequencies(dict_word)
    #mask = np.array(Image.open("MaidDragon.png"))
    word_cloud = WordCloud(font_path = font, background_color = 'white').generate_from_frequencies(dict_word)
    word_cloud.to_file('description.jpg')
if __name__ == '__main__':
    dict_word = cut()
    cloud(dict_word)