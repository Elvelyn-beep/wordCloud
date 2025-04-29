# coding:utf-8

from collections import Counter
from os import path
import jieba
jieba.load_userdict(path.join(path.dirname(__file__), 'userdict//userdict.txt'))  # 导入用户自定义词典

def word_segment(text):
    
    # 分词并统计词频
    jieba_word = jieba.cut(text, cut_all=False)  # 精准模式分词
    word_list = list(jieba_word)  # 转换为列表
    
    # 计算词频
    word_freq = Counter(word_list)
    
    # 写入统计文件
    with open('doc//统计.txt', 'w', encoding='utf-8') as fw:
        for k, v in word_freq.items():
            fw.write("%s,%d\n" % (k, v))
    
    # 返回用空格连接的分词结果
    return ' '.join(word_list)
