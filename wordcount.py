from string import punctuation

def strip_punctuation(s):
    """
    This function strips the string s of punctuation.

    source: https://www.quora.com/How-do-I-remove-punctuation-from-a-Python-string
    """
    return ''.join(c for c in s if c not in punctuation)

words_frequency = {}

for line in open("test.txt"):
    words = line.rstrip().lower().split(" ")
    for word in words:
        word_stripped = strip_punctuation(word)
        words_frequency[word_stripped] = words_frequency.get(word_stripped, 0) + 1

for word, count in words_frequency.items():
    print(f'{word} {count}')