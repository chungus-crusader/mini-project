''' coment or code eg.
'''

[this file] = blue text saying this file

''golden text to name txt files I assume
''

## header
### smaller header
-filled bullet point
tab then * = sub bullet point (empty)

<img src="http://XXXXXX.png" width="400"/>



### About Markdown

Markdown is an easy-to-use plain text formatting syntax created by John Gruber.

To write a text in Markdown you need a Markdown editor. Fortunately VS Code comes with an easy-to-use Markdown editor. Hence, open a markdown file (.md file) in VS code and press ``preview`` in the upper right corner and you will see the Markdown code side-by-side with a view showing the rendered text.

To get started using Markdown we suggest that you open the file you are currently reading (ProjectTemplate.md), or (better) [this file](https://homepage.lnu.se//staff/jlnmsi/python/2021/Macdown.zip), in a Markdown editor and compare the rendered result with the given markdown code. Then Google various markdown tutorials to understand markdown symbols that are not obvious from the given examples. A few examples:

Python code markup:

```python
def max(a,b):
	if a > b:
		return a
	else:
		return b
```

Inserting images (using HTML markup):

<img src="http://homepage.lnu.se/staff/jlnmsi/python/2020/cos_sin.png" width="400"/>


This is a table with left- , center-, and right-allgned columns:

| Left Aligned  | Center Aligned  | Right Aligned |
|:------------- |:---------------:| -------------:|
| col 3 is      | some wordy text |         $1600 |
| col 2 is      | centered        |           $12 |
| zebra stripes | are neat        |            $1 |

The left- and right-most pipes (`|`) are only aesthetic, and can be omitted. The spaces don’t matter, either. Alignment depends solely on `:` marks in the lines under the column titles.

## Regarding the report template

The template below is in English. Feel free to write your report in Swedish or English. 

We expect each team to present their report as their README.md in the Gitlab repository.

Try to be short and precise. We expect more than 2000, but less than 4000, words. 

Assume that the reader knows about Python. Give a reference and explain techniques introduced that we havn't presented in the course.

In what follow we give you the **mandatory report headlines** and brief comments about what we expect each section to contain. Make sure to remove our comments (and the Markdown intro above) in your final report.


************************

# Mini-project report 
Members: Zjeger Zangana and Mickey Mouse  
Program: Network security (NGDNS-eng)  
Course: 1DV501 
Date of submission: 2022-11-XX

## Introduction  
This is our mini project for the course 1DV501 - Network
security - eng. This mini project consists of 3 parts.
In part 1 use python's set class to count the number of unique words in the text files ``life_of_brian`` and ``swedish_news_2020`` that we use throughout all parts of the mini project. We also use python's dictionary class to produce a Top 10 list of the ten most frequently used words that we later in part 3 of our project repeat the computation using our own custom made hashset and BST implementation.

## Part 1: Count unique words 1
The text should include:
- How many words did each of the two text files 
``life_of_brian`` and ``swedish_news_2020`` have?
- How did you implement the Top-10 part of the problem. Feel free to show code fragments.
- Present a unique word count and the Top-10 lists for each of the two files.

## Part 2: Implementing data structures
- Give a brief presentation of the given requirements
	* We were required to make a hash based set where the elements were to be stored in python lists that were stored in buckets which also basically a list. The goal was to start with a bucket list size of 8 and rehash whenever the number of elements in the buckets became the same as the number of buckets. This rehash would simply just double the bucket list size. There were code skeletons made for the hash based set by our tutors that required us to include certain functions. We are allowed to add more functions if we wished so, howvever we were not allowed to remove any of the existing functions. We had to make a hash code for each string in the already existing list in ``hash_main.py``. We weren't given a goal for how good our hashcode had to be so we just tried to make it as good as possible; however, we were told to try to fill as many buckets as possible and not leave most buckets empty. We needed to make an add, remove, contains function along with some other functions that would help us improve our hashfunction later on for part 3 when we introduced the txt files to the hashset.
- For the hash based word set (HashSet), present (and explain in words):
 	* The function ``add`` calls the hash function for a specific word and what happens is that we iterate for each character in the word getting the ascci code for it, we also get the index of that character and to get the hashcode for it we run it through this algorithm: 
	```python
	def get_hash(self, word):
        ascii_and_prime = 0
		for char in str(word):
            i = word.index(char)
            asciii = ord(char)
            ascii_and_prime += asciii * 31**i
			mod = len(self.buckets)
        return ascii_and_prime % mod
	```
	basically the ascii code is multiplied by the prime number 31 to the power of the index. What this does is create uniqueness in the hashcode so there is as little collision as possible. I learnt this concept from Dr. Rob Edwards from San Diego State University where he explains how powerful the number 31 is for hashcodes with strings. Some lectures were about java, however the concept is similar and as I played around with it with the index numbers I got that without increasing my computing time that algorithm produced the smallest empty bucket ratio and produced the least amount of collision. Once we have the hashcode, the bucket at that postion is being checked for wheter the word is there or not with the code:
	```python
		if word not in self.buckets[hash_value]:
	```
 	if it was we didnt add it, if it wasn't the word was added to that bucket. The counter for the number of elements was incremented by 1 and then checked if it was equal to the number of buckets. If yes, the rehash function would be called. Once this was called a clone of the buckets was made, the existing buckets were cleared and when the items in the clone buckets was pushed to the new buckets which was twice as many.
	* After completing all the functions every expected answer was correct in the hash_main besides the empty bucket ratio which had a very small difference.
 	
- For the BST based map (BstMap), present (and explain in words):
 	* Python code for the two functions ``put`` and ``max_depth``.
 	* Point out and explain any differences from the given results in ``bst_main.py``.

## Part 3: Count unique words 2
- How did you implement the Top-10 part of the problem. Feel free to show code fragments.
- Present a unique word count and the Top-10 lists for each of the two files.
* What is the bucket list size, max bucket size and zero bucket ratio for HashSet, and the total node count, max depth and leaf count for BstMap, after having added all the words in the two large word files? (Hence, eight different numbers.)
	* Bucket list size is the current number of buckets in the hashset. The max bucket size shows how many collisions the bucket with the most amount of collisions have, meaning how many elements the biggest bucket has. The zero bucket ratio is a function that shows the percentage of empty buckets there is in the hashset. It calculates the ratio using the formula:
	```python
		ratio = empty_buckets / len(self.buckets)
	```
		

* Explain how max bucket size and zero bucket ratio can be used to evaluate the quality of your hash function in HashSet. What are optimal/reasonable/poor values in both cases?
	* The lower the max bucket size was and the smaller the zero bucket ratio the better the quality of the hash function. I used them to test several combinations of algorithms to find out which specific one produces the highest quality hash function and with some lectures by Dr. Rob Edwards and several arguments about which prime number creates the most uniqueness on stack overflow, just through trial and error and testing I came up with the golden algorithm. A good max bucket size would be anything from 1 to 20 for our purpose is good along with a zero bucket ratio between 20 to 45%. However, there might be other limiting factors to why you would get a higher ratio even if your algorithm is good. One example would be if you have rehashed recently so the number of elements is much smaller than the number of buckets, so for obvious reasons the ratio would be quite high. Poor value would be a max bucket size above 100 and a percentage above 50%.
* Explain how max depth and leaf count can be used to evaluate the efficiency of the BstMap. What are optimal/reasonable/poor values in both cases?


## Project conclusions and lessons learned
We separate technical issues from project related issues.
### Technical issues 
- What were the major technical challanges as you see it? What parts were the hardest and most time consuming?
	* Due to the fact that me and my partner were using different operating systems we struggled with the encoding on the txt file.
	There was also some issues with my (Zjeger's) git which didnt allow me to push work in the beginning.
- What lessons have you learned? What should you have done differently if you now were facing a similar problem.
	* The way I tackled the git problem was bad and time consuming, I learnt that something that I might not know, my partner could so shotting him a text would have been way more efficient. Instead of trying to solve it myself in the future I can just include my partner on a problem of mine.
- How could the results be improved if you were given a bit more time to complete the task.
	* I believe we tried really hard for this project and its not the outcome that would really change that much but I believe I personally could dig deeper into hashfunctions and find an even stronger algorithm that use less computation.

### Project issues
- Describe how your team organized the work. How did you communicate? How often did you communicate?
	* During the first few days of the project I (Zjeger) was faced with a family emergency which forced me to travel to Stockholm for a few days to deal with it. However I did not let that be a reason for my teammate to fail this project. He took care of part 1 of the project by himself and did a very good job. We divided part 2 and 3. I (Zjeger) felt I understood hashing the least so I wanted to take care of that so that I learn it. He took care of the BST. We communicated through social medias daily and we met on campus often to either catch up each other on progress, ask each other questions, give each other tips and also teach each other the things we did and learnt online.
- For each individual team member: 
 	* Describe which parts (or subtasks) of the project they were responsible for. Consider writing the report as a separate task. 
	Try to identify main contributors and co-contributors.

 - Estimate hours spend each week (on average)
 - What lessons have you learned? What should you have done differently if you now were facing a similar project.

### Zjeger Zangana
I was in charge of getting the hashing up and running. I did everything that was related to the hashset implementation. And because my partner had to be in charge of part 1 alone it was only fair I worked on the report as much as I could and left the the parts only he could fill. I spent on average 3 hours a day working on the mini project. Mostly because I took my time, went through several lectures on hashing, hashcodes, the effectiveness of prime numbers, the importance of powers and some java lectures that was related to hashing. I learnt how to micro manage a program and run certain parts of my program as this program required me to move step by step and to make sure everything works I got more familiar with printing results on my way forward. One thing I would do differently if I was to be in another project would be to ask more often rather than trying to solve it myself.

