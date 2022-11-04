def count(words):  # Func to count total number of words

    # Convert file content, split by linebreak, into set
    # Eliminate all duplicates, then go back to list

    return len(list(set(map(lambda w: w.lower(), words.split('\n')))))


def top(words):  # Func to count the top 10 most frequent uniques

    # Lst = every word in file split by linebreak,
    # lowercased, and filtered based on
    # whether the length of word is 4 or not

    lst = [(i).lower() for i in filter(lambda w:len(w) > 4, words.split('\n'))]

    # Dictionary of all items
    counter = dict()

    for word in lst:
        if word in counter:  # +1 to word value if word key exists
            counter[word] += 1
        else:
            counter[word] = 1  # Word value = 1 if key is new

    # Top = items of counter, sorted numerically in reverse (5, 4, 3...)
    # Sorting key = pair value
    # First 10 elements (0-9)

    top = list(sorted(counter.items(), key=lambda item: item[1],
               reverse=True)[0:10])

    # Join the top by linebreak and map every element so it becomes a string
    return '\n'.join(list(map(lambda count: f'{count[0]}: {str(count[1])}',
                     top)))


# Opening and reading some files
news = open('words-data/news_15093933_words.txt')
brian = open('words-data/brian_13372_words.txt')
nTxt = news.read()
bTxt = brian.read()

# Function calls with some output
print(f'''\nUnique words in news: {count(nTxt)}
Unique words in Brian: {count(bTxt)}\n''')
print(f'Top 10 news words:\n{top(nTxt)}\n\nTop 10 Brian words:\n{top(bTxt)}')

news.close()
brian.close()
