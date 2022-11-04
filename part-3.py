from bst import BstMap as bst
from hash import final_hash as hset
import random


def file_info(words):  # Function to return required file info
    bin = bst.BstMap()
    random.shuffle(words)  # Shuffling split word list for more balanced tree

    for word in words:

        # Lowering every wordm before adding to bin
        # Add method is different from put

        w = word.lower()
        bin.add(w, 1)

    """
    topTen = all words greater than 4 in length,
    uppercased, sorted numerically using as_sorted_lst()
    (based on occurences)
    as_sorted_lst() is different from as_list()
    """

    topTen = list(map(lambda w: [w[0].capitalize(), str(w[1])],
                  bin.as_sorted_lst()))

    # top 10 (no pun intended) of all topTen elements
    # Joined with a linebreak

    topTen = '\n'.join(map(lambda pair: ': '.join(pair), topTen[0:10]))

    #  Result max depth, count leafs, size
    res = f"""
Number of tree nodes: {bin.size()}
Max depth: {bin.max_depth()}
Leaf count: {bin.count_leafs()}
    """
    return f"{res}\n{topTen}"


def start_hashing(lst):  # Function to return unique word count
    words = hset.HashSet()   # Create new empty HashSet
    words.init()    # initialize with eight empty buckets
    for name in lst:
        # made the words in txt files lowercase
        words.add(name.lower())
    count = words.get_size()    # number of unique words
    mx = words.max_bucket_size()    # max bucket
    buck_list_size = words.bucket_list_size()  # bucket list size
    zero_buckets_ratio = words.zero_bucket_ratio()  # zero bucket ratio
    return mx, buck_list_size, zero_buckets_ratio, count


# Opening the files
brian = open('words-data/brian_13372_words.txt')
news = open('words-data/news_15093933_words.txt')
brianTxt = brian.read().split('\n')
newsTxt = news.read().split('\n')
brian.close()
news.close()


# displaying Life of brian results
print(file_info(brianTxt))

mxb_brian, bls_brian, zbr_brian, b_count = start_hashing(brianTxt)
print('\nThe number of unique words in life of Brian is:', b_count)
print('The max bucket size of life of Brian is:', mxb_brian)
print('Tbe bucket list size in life of Brian is:', bls_brian)
print('The zero bucket ratio for life of Brian is:', zbr_brian)


# displaying News results
print(file_info(newsTxt))

mxb_news, bls_news, zbr_news, news_count = start_hashing(newsTxt)
print('\nThe number of unique words in life of Swedish News:', news_count)
print('The max bucket size of Swedish News is:', mxb_news)
print('Tbe bucket list size in Swedish News is:', bls_news)
print('The zero bucket ratio for Swedish News is:', zbr_news)
