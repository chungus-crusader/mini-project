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
    # wrds = [w.lower() for w in words]
    random.shuffle(words)

    for word in words:
        w = word.lower()
        bin.add(w, 1)

    topTen = list(map(lambda w: [w[0].capitalize(), str(w[1])],
                  filter(lambda w: len(w[0]) > 4, bin.as_sorted_lst())))

    topTen = '\n'.join(map(lambda pair: ': '.join(pair), topTen[0:10]))

    res = f"""
Number of tree nodes: {bin.size()}
Max depth: {bin.max_depth()}
Leaf count: {bin.count_leafs()}
    """
    return f"{res}\n{topTen}"
# print(unique(brian.read().split('\n')).size)
# print(unique(news.read().split('\n')).size)
print(count_top(news.read().split('\n')))
brian.close()
news.close()
