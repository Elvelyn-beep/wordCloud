 
# coding:utf-8
from os import path
import chnSegment
import plotWordcloud

if __name__ == '__main__':
    d = path.dirname(__file__)
    # 指定 encoding='utf-8' 读取文件
    with open(path.join(d, 'doc//大连.txt'), 'r', encoding='utf-8') as f:
        text = f.read()
    
    # 若是中文文本，则先进行分词操作
    text = chnSegment.word_segment(text)
    
    # 生成词云
    plotWordcloud.generate_wordcloud(text)
