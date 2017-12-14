from collections import Counter

text = "The brown jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox " \
       "jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy " \
       "dog."

# breaks up string into a list of individual words
words = text.split()

counter = Counter(words)
top_three = counter.most_common(3)
print(top_three)
