# Mini-project report 
Members: Zjeger Zangana and Rodions Busurovs     
Program: Network security (NGDNS-eng)  
Course: 1DV501          
Date of submission: 2022-11-XX

## Introduction  
This is our mini project for the course 1DV501 - Network
security - eng. This mini project consists of 3 parts.
In part 1 use python's set class to count the number of unique words in the text files ``life_of_brian`` and ``swedish_news_2020`` that we use throughout all parts of the mini project. We also use python's dictionary class to produce a Top 10 list of the ten most frequently used words that we later in part 3 of our project repeat the computation using our own custom made hashset and BST implementation.

## Part 1: Count unique words 1

- Part 1 was by far the easiest part of the project, as unlike the latter two parts, we were to use in-built functions.

- The file, *part-1/word-count.py*, consists of two functions - **count(words)** and **top(words)**, 
both of which expect a string of words, separated by linebreak.

	- **count(words)**, a much easier function of the two, returns a one-liner - the
	length of a list of all words, split by linebreak, with every word lowercased,
	which is converted into a set to eliminate all duplicates, and then back into a
	list. Code below:

		```python
		return len(list(set(map(lambda w: w.lower(), words.split('\n')))))
		```

	- **top(words)** Converts a passed in string of words, separated by "\n",
	into a list of lowercased words, split by the linebreak character, filtered
	based on the length of a word *(i.e., only those words remain in list that
	are > 4 in length)*.

		All operations above are done with a one-liner:

		```python
		lst = [(i).lower() for i in filter(lambda w:len(w) > 4, words.split('\n'))]
		```
	
		- The function moves on to declare a dict() of *counter*, serving as a container
		for word counting. A for loop follows, where we add 1 to the value of word in
		dictionary, *if key of word is already **IN** the dictionary*, or add a new
		key-value pair of "word": 1, *if word is **NOT** in said dictionary. 
		
			Code snippet:

			```python
			counter = dict()

			for word in lst:
				if word in counter:
					counter[word] += 1
				else:
					counter[word] = 1
			```
		- The function then assigns to *top* the first 10 items from a list of container items, sorted numerically, in reverse, by an item's second index
		value *(every item is a tuple, [0] - key, [1] - value)*.
		- The function then returns *top*, joined by "\n", and mapped so every item
		is converted into an f-string that includes its key and value.

			Code snippet:

			```python
			top = list(sorted(counter.items(), key=lambda item: item[1],
               reverse=True)[0:10])
			
			return '\n'.join(list(map(lambda count: f'{count[0]}: {str(count[1])}',
                     top)))
			```
	
	- This is the output the file returns:

		- Unique words in news: 402315
		- Unique words in Brian: 2033

			| Top 10 news words: | Top 10 Brian words: |
			|--------------------|---------------------|
			| under: 54042       | brian: 368          |
			| säger: 47542       | crowd: 161          |
			| efter: 44090       | centurion: 121      |
			| kommer: 42852      | mother: 104         |
			| eller: 32080       | right: 99           |
			| också: 30477       | crucifixion: 78     |
			| sedan: 30396       | pilate: 68          |
			| andra: 28074       | pontius: 64         |
			| finns: 27583       | rogers: 52          |
			| många: 26818       | there: 44           |


## Part 2: Implementing data structures
- We were required to make a hash based set where the elements were to be stored in python lists that were stored in buckets which also basically a list. 
- The goal was to start with a bucket list size of 8 and ``rehash()`` whenever the number of elements in the buckets became the same as the number of buckets. This rehash would simply just double the bucket list size. There were code skeletons made for the hash based set by our tutors that required us to include certain functions. 
- We are allowed to add more functions if we wished so, howvever we were not allowed to remove any of the existing functions.
- We had to make a hash code for each string in the already existing list in ``hash_main.py``. We weren't given a goal for how good our hashcode had to be however, we were told to try to fill as many buckets as possible and not leave most buckets empty.
- We needed to make ``add()``, ``remove()``, ``contains()`` functions along with some other functions that would help us improve our hash algorithm later on for part 3 when we introduced the txt files to the hashset.
:
 	* The function ``add()`` calls the hash function for a specific word and what happens is that we iterate for each character in the word getting the ascci code for it, we also get the index of that character and to get the hashcode for it the ascii code of each letter is multiplied by 31 to the power of the index. The sum of that modolus the total amount of buckets gives us the hashcode, this way the smallest difference in the word would give a great difference in hashcode. The algorithm looks like this:

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
- Because the ascii code is multiplied by the prime number 31 to the power of the index, it creates uniqueness in the hashcode so there is as little collision as possible. 
	* I learnt this concept from Dr. Rob Edwards from San Diego State University where he explains how powerful the number 31 is for hashcodes with strings.
- Some lectures were about java, however the concept is similar and as I played around with the index numbers, I got that without increasing my computing time that algorithm produced the smallest empty bucket ratio and produced the least amount of collision.
- Once we have the hashcode for a word, the bucket at that postion is being checked for wheter the word is there or not with the code:
	```python
		if word not in self.buckets[hash_value]:
	```
 	* if the word is not in the bucket, we add it else we don't.
- The counter for the number of elements is then incremented by 1 and then checked if it was equal to the number of buckets.
	* If yes, the rehash function would be called.
-  Once this is called, a clone of the buckets is made, the existing buckets are then cleared and when the items in the clone buckets is pushed to the new buckets which iss twice the size. To clear the buckets we used an interesting code that many of our peers did not use. The code is shown below:
```python
	# clears the elments in the original buckets
        self.size = 0

```

- After completing all the functions every expected answer in the hash_main was correct.
 	
- For the BST based map:

	- Having tinkered a bit with this data structure before, implementing some of the more "known" methods was fairly straightforward.

	- By far one of the biggest roadblocks were ``to_string()``, even moreso than *as_lst*.

		- For a considerable time, the method would append multiple trailing parentheses,
		messing up the output (i.e. *{ ( ( ( ( (Adam, 27), (Ceve, 37)*...*(Zoe,41) ) ) ) )*).

		- For a while, a potential solution was for ``to_string()`` call ``as_lst()``, which would be the one to make the list,
		and then convert *that* into a joined string. Obviously, this was too slow.

		- A potential cause was there were too many trailing whitespaces, which the code would then split the string with
		in order to sort it alphabetically.
		
		- This was solved fairly easily by stripping the string of trailing whitespace, although that took much longer than we would
		like to admit.
	
	- ``put()`` and ``max_depth()`` took very little time to implement - the prior experience with BST's helped out a lot.
	
	- [This video by a freeCodeCamp contributor](https://youtu.be/5cU1ILGy6dM) helped tremendously in understanding 
	the basic principle of the BST, as well as the slides by our lecturer Jonas Lundberg.

		- ``put()`` method first checks whether the passed in key is *equal* to current node's key. If true, the value is
		reassigned. The method returns, and no further code is executed.

			```python
				def put(self, key, value):
					if self.key == key:
						self.value = value
						return
			```

			- If the test case fails, it moves onto checking whether the key is *greater than* the current node's key,
			alphabetically.
				- If true, the method then checks whether the right node *does not* exist, in which case the right node
				is assigned the value of **Node(*key, value*)**. The method returns. No further code is executed.

					```python
						if key > self.key:
							if not self.right:
								self.right = Node(key, value)
								return
					```

				- If above test case fails, method calls itself recursively on the existing right node.

					```python
						self.right.put(key, value)
					```
			- Else if is executed if the key is *less than or equal* to the current node's key, alphabetically.

				- The exact same code as in the test case for the right node is executed, only on the left node.

					```python
						elif key <= self.key:  # If key <= current key
							if not self.left:  # If left branch does not exist
								self.left = Node(key, value)
								return
							self.left.put(key, value)  # If left branch exists
					```
		- ``max_depth()`` is a lot less convoluted method than the one above:

			- Method first declares two variables of **depthL** and **depthR** with a starting value of *1*.

				```python
					depthL = 1
					depthR = 1
				```
			
			- If the left node exists, depthL is added the return value of max_depth(), recursively called on left node.
			Same applies to the right node.

				```python
					if self.left:
						depthL += self.left.max_depth()
					if self.right:
						depthR += self.right.max_depth()
				```

			- Every time the method is called, it then compares **depthL** and **depthR**, and returns one var that is the greatest.

				```python
					if depthL < depthR:
					return depthR
					else:
						return depthL
				```
			
			- This way, only the maximum depth is returned through a series of recursive operations, for every node. While hard to
			immediately grasp when thinking of it, it's fairly easy to understand through sketches, which our lecturer had recommended
			that we do, and which had helped.

	- There were, thankfully, virtually no differences between the test output and the result the BstMap would return.
	Errors that did occur, however, were caused by a temporary inability to, for instance, sort the output alphabetically,
	either in ``to_string()`` or ``as_lst()``, or the trailing whitespaces, which were dealt with as described above. 
	
	- The sorting errors were mostly caused by a misunderstanding of how the values were supposed to be sorted.
	Initially, I suspected that we had to compare both the *values* **AND** the *keys*, only then to figure out that it was as easy
	as just sorting the return value. Either way, the issues were resolved.

## Part 3: Count unique words 2
- How did you implement the Top-10 part of the problem? Feel free to show code fragments.

	- Originally overwhelmed with the requirements of the project, an inefficient solution was
	created where a hashSet of all unique words greater in length than 4 was created, whose
	elements were then appended, *one by one*, into a separate BstMap, and only then had their
	occurences counted. This was so slow, in fact, that the program would only go through 200-300
	words a second. This was quickly scrapped.

	- The final solution involves the function ``file_info(words)`` instantiating a BstMap **bin**
	and shuffling the passed in list of all words. A for loop follows, iterating over every
	word in *words*. The lowercased word is added to the bstMap using the ``add()`` method:

		```python
			bin = bst.BstMap()
			random.shuffle(words)

			for word in words:

				w = word.lower()
				bin.add(w, 1)
		```

	- ``add()`` method is nearly identical to ``put()``, but instead of overwriting the value of the same key,
	it **adds** the passed in value to the existing one:

		```python
			if self.key == key:
				self.value += value
				return
		```
	- A variable **topTen** is declared. Its value is the list of all key-value pairs in 
	**bin.as_sorted_lst()**, the key capitalized, and the value converted into a string.

		```python
			topTen = list(map(lambda w: [w[0].capitalize(), str(w[1])],
                  bin.as_sorted_lst()))
		```
		- ``as_sorted_lst()`` is different from ``as_lst()`` in that it does not sort the node keys by itself. That is done once, in the BstMap's method that calls the node one - for efficiency's sake - and is sorted numerically.

		- Another significant difference is that ``as_sorted_lst()`` does not append key-value pairs
		whose keys are <= 4 in length, or whose values are not > 1.

			```python
				if self.value > 1 and len(self.key) > 4:
					lst.append([self.key, self.value])
			```
	- **topTen**'s elements are then converted into f-strings, the entire list joined with *\n*, and then
	spliced from 0 to 10, giving the required top 10 elements of the list.

		```python
			topTen = '\n'.join(map(lambda pair: ': '.join(pair), topTen[0:10]))
		```
	
	- The value above is then returned alongside all other required results, as a multi-line f-string **res**.
		
		```python
			res = f"""
			Number of tree nodes: {bin.size()}
			Max depth: {bin.max_depth()}
			Leaf count: {bin.count_leafs()}
				"""
				return f"{res}\n{topTen}"
		```

		
- Present a unique word count and the Top-10 lists for each of the two files.
	
	- The results are identical to what part 1 returns, the only difference being that the words are
	returned as capitalized.
		| Top 10 news words: | Top 10 Brian words: |
		|--------------------|---------------------|
		| Under: 54042       | Brian: 368          |
		| Säger: 47542       | Crowd: 161          |
		| Efter: 44090       | Centurion: 121      |
		| Kommer: 42852      | Mother: 104         |
		| Eller: 32080       | Right: 99           |
		| Också: 30477       | Crucifixion: 78     |
		| Sedan: 30396       | Pilate: 68          |
		| Andra: 28074       | Pontius: 64         |
		| Finns: 27583       | Rogers: 52          |
		| Många: 26818       | There: 44           |


- Bucket list size is the current number of buckets in the hashset. The max bucket size shows how many collisions the bucket with the most amount of collisions have, meaning how many elements the biggest bucket has. The zero bucket ratio is a function that shows the percentage of empty buckets there is in the hashset. It calculates the ratio using the formula:

	```python
		ratio = empty_buckets / len(self.buckets)
	```
		


- The lower the max bucket size was and the smaller the zero bucket ratio the better the quality of the hash function. I used them to test several combinations of algorithms to find out which specific one produces the highest quality hash function.
- Looking at this one [lecture by Dr. Rob Edwards](https://www.youtube.com/watch?v=jtMwp0FqEcg&t=156s), just through trial and error and testing I came up with the golden algorithm.
- A good max bucket size would be anything from 1 to 20 for our purpose is good along with a zero bucket ratio between 20 to 45%. 	
	* However, there might be other limiting factors to why you would get a higher ratio even if your algorithm is good. One example would be if you have rehashed recently so the number of elements is much smaller than the number of buckets, so for obvious reasons the ratio would be quite high even though your hashfunction might be good.
- A	poor value for the max bucket size would be anything above 100 and  for the empty bucket ratio, taking into account that the ``rehash()`` could have recently been used I would say a poort value would be anything above 50%.


As for the Bst stuff:
- The greater the depth, the less efficient/balanced the tree - More recursions would need to be executed
	to reach the deepest leaf. Following this logic, I would say that max depths of 24 (for Brian) and 46
	(for News) are decent results - notice how, despite the list size increase from 13k to 15 million, the
	depth is less than two times the previous one.

	- Following this logic, the more leafs there are, the less nodes with children there will be. The less
	children there are, the less recursive calls there will be to find the deepest leaf. 

	- With the leaf counts for Brian and News being 680 and 132811, respectively, I would consider these
	values to be fairly efficient. Of note is the fact that both round up to the node-to-leaf ratio of 0.33,
	which seems to be the case for all balanced trees. 

## Project conclusions and lessons learned
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
- During the first few days of the project I (Zjeger) was faced with a family emergency which forced me to travel to Stockholm for a few days to deal with it. However I did not let that be a reason for my teammate to fail this project. He took care of part 1 of the project by himself and did a very good job. We divided part 2 and 3. I (Zjeger) felt I understood hashing the least so I wanted to take care of that so that I learn it. He took care of the BST. We communicated through social medias daily and we met on campus often to either catch up each other on progress, ask each other questions, give each other tips and also teach each other the things we did and learnt online.



### Zjeger Zangana

	-I was in charge of getting the hashing up and running. I did everything that was related to the hashset implementation. And because my partner had to be in charge of part 1 alone it was only fair I worked on the report as much as I could and left the the parts only he could fill.
	- I spent on average 3 hours a day working on the mini project. Mostly because I took my time, went through several lectures on hashing, hashcodes, the effectiveness of prime numbers, the importance of powers and some java lectures that was related to hashing.
	- I learnt how to micro manage a program and run certain parts of my program as this program required me to move step by step and to make sure everything works. I got more familiar with printing results on my way forward.
	- One thing I would do differently if I was to be in another project would be to ask more often rather than trying to solve it myself.

### Rodions Busurovs

	- One of my tasks was to implement part 1. Being the easiest of three parts, I would say it only took me some
	2-4 hours in total, excluding all the comments and formatting. As my partner took the responsibility of
	dealing with most of the report, I had a lot more time to focus on my part of the project.

	- Our lab assistant, Ola Flygt, by far contributed the most to helping me and my partner with issues that arose during our work.
	
	- I would say that I spent 2-4 hours a day working on the project, although there were days when practically
	no work was done, and days when I could easy spend 5 hours tinkering with the code, which is usually the
	way I work on other assignments.

	- Probably the most important lesson I've learnt from this project is the importance of face-to-face communication and coordination in any team, especially when involved in programming. Problems with git or roadblocks in code could only be solved in person, and no chat or video call would've
	been enough to resolve any of those issues.



