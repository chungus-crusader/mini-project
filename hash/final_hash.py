from dataclasses import dataclass
from typing import List


@dataclass
class HashSet:
    buckets: List[List] = None  # type: ignore
    size: int = 0

    def init(self):
        self.size = 0
        self.buckets = [[] for i in range(8)]

    # Computes hash value for a word (a string)
    def get_hash(self, word):
        ascii_and_prime = 0
        # for each letter multiply its ascii code with
        # the constant 7 + the index and multiply all with 31
        for char in str(word):
            i = word.index(char)
            asciii = ord(char)
            # the hash calculation for each letter
            ascii_and_prime += asciii * 31**i
            # ascii_and_prime += (asciii * (i+7)**3) * 31
        # return the hash value which is
        # the sum of the hash for
        # each letter modolus bucket size
        mod = len(self.buckets)
        return ascii_and_prime % mod

    # Doubles size of bucket list
    def rehash(self):
        # create a clone of our current buckets
        clone_buckets = self.buckets
        # doubles size of bucket list
        self.buckets = [[] for i in range(len(self.buckets)*2)]
        # clears the elments in the original buckets
        self.size = 0
        # iterating for each element for each list in the clone bucket
        # adding them to the new set of values
        for bucket in clone_buckets:
            for elements in bucket:
                self.add(elements)

    # Adds a word to set if not already added
    def add(self, word):
        # we get the hash value for the word we want to add
        hash_value = self.get_hash(word)
        # check if the word is not already added
        if word not in self.buckets[hash_value]:
            # if it is not added we add it
            self.buckets[hash_value].append(word)
            # since we added 1 item to the list we increase self.size by 1
            self.size += 1
            b_len = len(self.buckets)
            if self.size >= b_len:
                self.rehash()

    # Returns a string representation of the set content
    def to_string(self):
        # we concatenate our string with 1 space in between
        joined = ' '.join([' '.join(i) for i in self.buckets if i])
        # returning the string with curly brackets
        return f'{{ {joined} }}'

    # Returns current number of elements in set
    def get_size(self):
        return self.size

    # Returns True if word in set, otherwise False
    def contains(self, word):
        # get the hash value for the word to be checked
        hash_value = self.get_hash(word)
        # returns True if the word is in that bucket
        # returns False if it is not
        return word in self.buckets[hash_value]

    # Returns current size of bucket list
    def bucket_list_size(self):
        return len(self.buckets)

    # Removes word from set if there, does nothing
    # if word not in set
    def remove(self, word):
        # getting the hashvalue for the word
        hash_value = self.get_hash(word)
        # checking if the word is there
        if word in self.buckets[hash_value]:
            # if it is there it will be removed
            self.buckets[hash_value].remove(word)
            # since we removed 1 element we have to reduce the self.size by 1
            # so our total number of elements is correct
            self.size -= 1

    # Returns the size of the bucket with most elements
    def max_bucket_size(self):
        max_bucket_size = max(len(x) for x in self.buckets)
        return max_bucket_size

    # Returns the ratio of buckets of lenght zero.
    # That is: number of zero buckets divided by number of buckets
    def zero_bucket_ratio(self):
        empty_buckets = 0
        for bucket in self.buckets:
            # if the bucket isn't filled we add 1 to our empty_bucket counter
            if not bucket:
                empty_buckets += 1
        ratio = empty_buckets / len(self.buckets)
        return ratio
