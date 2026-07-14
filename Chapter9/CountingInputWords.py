text = input("Enter a line of text: ")

counts = dict()
words = text.split()

for word in words :
    counts[word] = counts.get(word, 0) + 1

print(counts)