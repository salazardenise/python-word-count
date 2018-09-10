# put your code here.

words_frequency = {}

for line in open("twain.txt"):
    line = line.rstrip()
    words = line.split(" ")
    for word in words:
        words_frequency[word] = words_frequency.get(word, 0) + 1

for word, count in words_frequency.items():
    print(f'{word} {count}')