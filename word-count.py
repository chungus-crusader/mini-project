from hash import HashSet as hsh
from bst import BstMap as bst
import random

brian = open('words-data/brian_13372_words.txt')
news = open('words-data/news_15093933_words.txt')


def unique(words):
    hshSet = hsh.HashSet()
    hshSet.init()
    for word in words:
        hshSet.add(word)
    return hshSet


def count_top(words):
    bin = bst.BstMap()

    wrds = [w.lower() for w in words]
    random.shuffle(wrds)

    for word in wrds:
        bin.add(word, 1)

    topTen = bin.as_sorted_lst()  # sorted(lst, key=lambda i: i[1])

    return topTen[0:9]
# print(unique(brian.read().split('\n')).size)
# print(unique(news.read().split('\n')).size)
print(count_top(news.read().split('\n')))
brian.close()
news.close()
