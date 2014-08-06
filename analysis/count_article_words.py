# encoding=utf-8
"""

"""
import requests
import jieba
import jieba.analyse
import jieba.posseg as pseg
from readability.readability import Document


def text_from_url(url):
    html = requests.get(url)
    return Document(html.content).summary()


def text_from_file(path):
    f = open(path)
    content = f.read()
    f.close()
    return content


def statistic_words_number(text):
    d = {}
    # words = jieba.cut(text)
    words = pseg.cut(text)
    for w in words:
        word = w.word
        print w.word.encode('utf-8'), w.flag
        if w.flag in ['ns', 'n']:
            d[word] = d.get(word, 0) + 1
    d = d.items()
    d = sorted(d, key=lambda x: x[1], reverse=True)
    return d


def top_words(text, topn=20):
    return jieba.analyse.extract_tags(text,topn)


def cut():
    text = u'玫琳凯的护肤品适合脸上有红血丝的人用吗?'
    print ','.join(jieba.cut(text))


def word_pseg(text):
    words = pseg.cut(text)
    for w in words:
       print w.word, w.flag


def test():
    # url = 'http://www.huxiu.com/article/38942/1.html'
    text = text_from_file('xiaoshuo/haizi.txt')
    # words = top_words(text, topn=100)
    # word_pseg(text)
    # cut()
    words = statistic_words_number(text)
    # for w in words:
    #     print w


if __name__ == '__main__':
    test()