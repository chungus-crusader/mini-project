from dataclasses import dataclass
from typing import List


@dataclass
class HashSet:
    buckets: List[List] = None
    size: int = 0

    def init(self):
        self.size = 0
        self.buckets = [[] for i in range(8)]

    # Computes hash value for a word (a string)
    def get_hash(self, word):
        hash = 0
        for c in word:
            hash += ord(c)
        hash = hash % len(self.buckets)
        return hash

    # Doubles size of bucket list
    def rehash(self):
        temp = [item for bucket in self.buckets for item in bucket]
        self.size = 0
        self.buckets = [[] for i in range(len(self.buckets) * 2)]
        for item in temp:
            self.add(item)

    # Adds a word to set if not already added
    def add(self, word):
        if self.size == len(self.buckets):
            self.rehash()
            self.add(word)
        else:
            # if type(word) == str:
            hash = (self.get_hash(word))
            if word not in self.buckets[hash]:
                self.buckets[hash].append(word)
                self.size += 1
            # else:
            #     hash = self.get_hash(word[0])
            #     same = map(lambda i: i[0] == word[0], self.buckets[hash])
            #     tru = filter(lambda i: i is True, same)
            #     if tru:
            #         self.buckets[hash][same.index(tru)][1] += 1
            #     else:
            #         self.buckets[hash].append(word)
            #         self.size += 1

    # Returns a string representation of the set content
    def to_string(self):
        s = '{ '
        s += ' '.join([' '.join(i) for i in self.buckets if i])

        return s + ' }'

    # Returns current number of elements in set
    def get_size(self):
        return self.size

    # Returns True if word in set, otherwise False
    def contains(self, word):
        return any([word in b for b in self.buckets])

    # Returns current size of bucket list
    def bucket_list_size(self):
        return len(self.buckets)

    # Removes word from set if there, does nothing
    # if word not in set
    def remove(self, word):
        for bucket in self.buckets:
            if word in bucket:
                bucket.remove(word)
                self.size -= 1
                break

    # Returns the size of the bucket with most elements
    def max_bucket_size(self):
        max = 0
        for bucket in self.buckets:
            if len(bucket) > max:
                max = len(bucket)
        return max
