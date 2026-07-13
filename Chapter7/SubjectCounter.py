print('Enter the file name:')

fileNameIsCorrect = False
while not fileNameIsCorrect :
    fileName = input('File name >')
    try :
        handle = open(fileName, 'r')
        fileNameIsCorrect = True
    except :
        print('Please enter a valid file name.')

count = 0
for line in handle :
    if 'Subject' not in line :
        continue
    count = count + 1

print('There were', count, 'subject lines in', fileName)