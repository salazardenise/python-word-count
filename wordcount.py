from string import punctuation
import sys

def strip_punctuation(s):
    """
    This function strips the string s of punctuation.

    source: https://www.quora.com/How-do-I-remove-punctuation-from-a-Python-string
    """
    return ''.join(c for c in s if c not in punctuation)

filename = "test.txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]

words_frequency = {}

for line in open(filename):
    words = line.rstrip().lower().split(" ")
    for word in words:
        word_stripped = strip_punctuation(word)
        words_frequency[word_stripped] = words_frequency.get(word_stripped, 0) + 1

## Print the dictionary - unordered
# for word, count in words_frequency.items():
#     print(f'{word} {count}')

## Print the dictionary - alphabetically
for word in sorted(words_frequency):
    print(f'{word} {words_frequency[word]}')