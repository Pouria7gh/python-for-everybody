# sval = input("your age:")
# try:
#     ival = int(sval)
# except:
#     ival = -1

# print('Your age:', ival)

shour = input('Hours:\n')
try:
    fhour = float(shour)
except:
    print('Error, please enter numeric input')
    quit()

srate = input('Rate:\n')
try:
    frate = float(srate)
except:
    print('Error, please enter numeric input')
    quit()

pay = frate * fhour
print('Pay:', pay)