# def thing():
#     print('Hello')
#     print('Fun')

# thing()
# print('Zip')
# thing()

### MAX and MIN ###

# text = 'Hello world'
# big = max(text)
# print(big)

# tiny = min(text)
# print(tiny)

def greet(lang) :
    if lang == 'es' :
        return "Hola"
    elif lang == 'fa' :
        return 'Dorod'
    else :
        return 'Hello'

print(greet('fa'), 'Pouria')
print(greet('en'), 'Michael')
print(greet('es'), 'Sally')