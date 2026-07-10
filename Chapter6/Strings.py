fruit = 'banana'
letter = fruit[1]
print(letter)

x = 3
w = fruit[x - 1]
print(w)

print('len', len(fruit))

for char in fruit :
    print(char)

print('*************************')

index = 0
while index < len(fruit):
    print(fruit[index].upper())
    index = index + 1

print('*************************')

count = 0
for char in fruit :
    if char == 'a' :
        count = count + 1

print(count)

print('*************************')

s = 'Monty python'
print(s[0:5])
print(s[6:12])
print(s[6:20])
print(s[:2])
print(s[8:])

print('*************************')

a = 'Hello'
b = 'there'

print(a + b)
print(a + ' ' + b)

print('n in fruit:', 'n' in fruit)
print('n not in fruit:', 'n' not in fruit)
print('m in fruit:', 'm' in fruit)
print('nan in fruit:', 'nan' in fruit)

print('*************************')

upper = 'HELLO THERE'
lower = upper.lower()

print('upper:', upper)
print('lower:', lower)

print('UPPER CASE CONSTANT STRINT'.lower())

print('\n*************************\n')

stuff = 'hello'
print(dir(stuff))

print('\n*************************\n')

print(fruit.find('nana'))
print(fruit.find('nanaa'))

print('\n*************************\n')

greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')
print(nstr)
nstr = greet.replace('o', 'x')
print(nstr)

print('\n*************************\n')

greet = '    Hello world    '
print(greet.rstrip())
print(greet.lstrip())
print(greet.strip())

print('\n*************************\n')

line = 'Please have a nice day.'
print(line.startswith('Please'))
print(line.startswith('p'))

print('\n*************************\n')

email = 'From stephen.marquard@uct.az.za Sat Jan 5 09:14:16 2008'
atIndex = email.find('@')
spaceAfterAt = email.find(' ', atIndex)
host = email[atIndex+1 : spaceAfterAt]
print(host)

print('\n*************************\n')

text = 'laba laba dub dub: 0.3451  '
colPos = text.find(':')
numStr = text[colPos+1 : ].strip()
print(float(numStr))

print('\n*************************\n')