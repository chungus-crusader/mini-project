from dataclasses import dataclass
from typing import List
import HashSet as hset


@dataclass
class HashSet:
    buckets: List[List] = None
    size: int = 0

    def init(self):
        self.size = 0
        self.buckets = [[] for i in range(8)]


    # Computes hash value for a word (a string)
    def get_hash(self, word):
        sum_of_ascii_codes = 0
        # add the ascii codes for each character in the string
        for char in str(word):
            sum_of_ascii_codes += ord(char)
        # return the hash value which is 
        # the sum of adcii codes modolus bucket size
        return sum_of_ascii_codes % len(self.buckets)


    # Doubles size of bucket list
    def rehash(self):
        pass    # Placeholder code ==> to be replaced


    # Adds a word to set if not already added
    def add(self, word):
        # we get the hash value for the word we want to add
        hash_value = self.get_hash(word)
        # check if the word is not already added
        if word not in self.buckets[hash_value]:
            # if it is we add a new list with the word in it       
            self.buckets[hash_value].append(word)


    # Returns a string representation of the set content
    def to_string(self):
        for i in self.buckets:
            return str(i)


    # Returns current number of elements in set
    def get_size(self):
        return len(self.buckets)


    # Returns True if word in set, otherwise False
    def contains(self, word):
        # get the hash value for the word to be checked
        hash_value = self.get_hash(word)
        # returns True if the word is in that bucket
        # returns False if it is not
        return word in self.buckets[hash_value]
        0


    # Returns current size of bucket list
    def bucket_list_size(self):
        pass    # Placeholder code ==> to be replaced

    # Removes word from set if there, does nothing
    # if word not in set
    def remove(self, word):
        hash_value = self.get_hash(word)
        if word in self.buckets[hash_value]:
            self.buckets[hash_value].remove(word)

    # Returns the size of the bucket with most elements
    def max_bucket_size(self):
        pass    # Placeholder code ==> to be replaced

    # Returns the ratio of buckets of lenght zero.
    # That is: number of zero buckets divided by number of buckets
    def zero_bucket_ratio(self):
        pass    # Placeholder code ==> to be replaced


# Program starts
# Initialize word set
words = hset.HashSet()   # Create new empty HashSet
words.init()             # Initialize with eight empty buckets

# Add names to word set. Notice: a) contains duplicate names,
# b) more than eight names ==> will trigger rehash
names = ["Ella", "Owen", "Fred", "Zoe", "Adam", "Ceve", "Adam", "Ceve", "Jonas", "Ola", "Morgan", "Fredrik", "Simon", "Albin", "Jonas", "Amer", "David"]
for name in names:
    words.add(name)

print("\nto_string():", words.to_string())  # { Adam David Amer Ceve Owen Ella Jonas Morgan Fredrik Zoe Fred Albin Ola Simon }
print("get_size():", words.get_size())             # 14
print("contains(Fred):", words.contains("Fred"))   # True
print("contains(Bob):", words.contains("Bob"))     # False

# Hash specific data
mx = words.max_bucket_size()
print("\nmax bucket:", mx)                # 2
buckets = words.bucket_list_size()
print("bucket list size:", buckets)     # 16
zero_buckets_ratio = words.zero_bucket_ratio()
print("zero bucket ratio:", round(zero_buckets_ratio, 2))  # 0.38

# Remove elements
delete = ["Ceve", "Adam", "Ceve", "Jonas", "Ola"]
for s in delete:
    words.remove(s)
print("\nget_size:", words.get_size())   # 10
print("to_string():", words.to_string())   # { David Amer Owen Ella Morgan Fredrik Zoe Fred Albin Simon }
