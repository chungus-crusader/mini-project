from hash import final_hash as hset


def start_hashing(lst):
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


# used encoding='utf8' so the txt file error goes away
with open('brian_13372_words.txt', encoding='utf8') as f:
    brian = f.read().split('\n')
# displaying Life of brian results
mxb_brian, bls_brian, zbr_brian, b_count = start_hashing(brian)
print('The number of unique words in life of Brian is:', b_count)
print('The max bucket size of life of Brian is:', mxb_brian)
print('Tbe bucket list size in life of Brian is:', bls_brian)
print('The zero bucket ratio for life of Brian is:', zbr_brian)

with open('news_15093933_words.txt', encoding='utf8') as f:
    news = f.read().split('\n')
# displaying Swedish News results
mxb_news, bls_news, zbr_news, news_count = start_hashing(news)
print('The number of unique words in life of Swedish News:', news_count)
print('The max bucket size of Swedish News is:', mxb_news)
print('Tbe bucket list size in Swedish News is:', bls_news)
print('The zero bucket ratio for Swedish News is:', zbr_news)
