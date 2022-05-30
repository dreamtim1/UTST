score = int(input('Enter score: '))

course = input('Enter course type (differentiated (d)/non-differentiated (n)): ')

grades =  {91: 'A', 81: 'B', 71: 'C', 61: 'D', 51: 'E', 0: 'F'}
result = 'The score must be in the range of 0 to 100.'

if course == 'n':
    if score >= 51 and score <= 100:
        print('PASSED')
    elif score >= 0 and score <= 100:
        print('FAILED')
    else:
        print(result)

elif course == 'd':
    for el in sorted(grades):
        if score >= el:
            result = grades[el]
    print(result)

else:
    print('The course type is not recognised.')
