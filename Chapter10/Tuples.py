x = ('pouria', 'slm', 'hello')
print(x[2])

y = (1, 2, 3)
print(y)
print(max(y))

### Tuples are not mutable ###
# y[2] = 50

(x, y) = ('fred', 2)

print(x)
print(y)

a = (1, 2, 30)
b = (2, 2, 3)
print(b > a)

print('********')

d = {'a': 10, 'c':22, 'b':1}
print(d.items())
print(sorted(d.items()))

for k,v in sorted(d.items()) :
    print(k, v)

temp = [(v, k) for k,v in d.items()]

# temp = list()
# for k,v in d.items() :
#     temp.append((v, k))

print(sorted(temp, reverse=True))