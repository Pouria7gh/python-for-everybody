nums = [1, 2, 3]
print(nums)

colors = ['red', 'yellow', 'blue']
print(colors)

stuff = [2.909, 'slm', 24, False]
print(stuff)

arrayInArray = [1, [2, 3], 5]
print(arrayInArray)

emptyList = []
print(emptyList)

### string are not mutable ###

name = 'bob'
# name[0] = 'B'
# name = 'B' + name[1:]
name = name.capitalize()
print(name)

### lists are mutables ###

numbers = [1, 10, 3, 4]
print(numbers)

numbers[1] = 2
print(numbers)

print(len(numbers))
print(len(name))

### range function ###

print(range(10))

### list manipulation ###

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print("a:", a)
print("b", b)
print("c:", c)

print('c[1:4]:', c[1:4])
print('c[1:]:', c[1:])
print('c[-2]:', c[-2])
print('c[-3:-1]:', c[-3:-1])

stuff = ['hello']
print(stuff)
stuff.append('yellow')
print(stuff)

print(1 in c)
print(2 in c)
print(100 in c)
print(100 not in c)

unordered = [8, 5, 1, 9, 3]
print(unordered)
unordered.sort()
print(unordered)
unordered.insert(2, 4)
print(unordered)

print(len(c))
print(min(c))
print(max(c))
print(sum(c))
print(sum(c)/len(c))

### lists and strings ###

abc = 'with three words'
stuff = abc.split()
print(stuff)