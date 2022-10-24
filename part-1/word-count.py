def count(words):
    return len(list(set(words.split('\n'))))


def top(words):
    lst = [(i).lower() for i in filter(lambda w:len(w) > 4, words.split('\n'))]

    counter = dict()

    for word in lst:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1

    top = list(sorted(counter.items(), key=lambda item: item[1],
               reverse=True)[0:4])

    return '\n'.join(list(map(lambda count: f'{count[0]}: {str(count[1])}',
                     top)))


news = open('words-data/news_15093933_words.txt')
brian = open('words-data/brian_13372_words.txt')
nTxt = news.read()
bTxt = brian.read()

print(f'''\nUNIQUE WORDS IN NEWS: {count(nTxt)}
UNIQUE WORDS IN BRIAN: {count(bTxt)}\n''')
print(f'TOP 4 NEWS WORDS:\n{top(nTxt)}\n\nTOP 4 BRIAN WORDS:\n{top(bTxt)}')

news.close()
brian.close()
