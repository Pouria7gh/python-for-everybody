### new line char ###

text = 'X\nY'
print(text)
print(len(text))

### file handle ###

handle = open('./mbox-short.txt', 'r')
print(handle)

# count = 0
# for line in handle:
#     count = count + 1
#     print(line, )

# print(count)

# txt = handle.read()
# print(len(txt))
# print(txt)
# print(txt[:20])

# for line in handle :
#     if line.startswith('From') :
#         print(line.strip())

for line in handle :
    if '@uct.ac.za' not in line :
        continue
    print(line.strip())