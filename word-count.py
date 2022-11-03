from bst import BstMap as bst
import random

# Opening the files
brian = open('words-data/brian_13372_words.txt')
news = open('words-data/news_15093933_words.txt')


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
                  filter(lambda w: len(w[0]) > 4, bin.as_sorted_lst())))

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


print(file_info(brian.read().split('\n')))
print(file_info(news.read().split('\n')))
brian.close()
news.close()
