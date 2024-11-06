# Task 3

with open("alte-date/input.txt", 'r') as f:
    text = f.read()

with open("alte_date/words.txt", 'r') as f:
    search_words=f.read()

for i in search_words:
    fist = text.index(i)
    last=text.rindex()