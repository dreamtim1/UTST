while True:
    try:
        month = int(input('Enter the number of a month: '))
        if month > 12 or month < 1:
            print('The number of a month must be in the range [1-12]')
            continue
        break
    except:
        print('Please enter an integer number')

if month == 2:
    while True:
        try:
            year = int(input('Enter a year: '))
            if year < 1:
                print('Year must be positive')
                continue
            break
        except:
            print('Please enter an integer number')
else:
    year = 0

if year:
    if not year % 4 == 0:
        common = True
    elif not year % 100 == 0:
        common = False
    elif year % 400 == 0:
        common = False
    else:
        common = True

if month == 2:
    if common:
        print(' That month has 28 days in it (a common year).')
    else:
        print(' That month has 29 days in it (a leap year).')
elif month in [1, 3, 5, 7, 8, 10, 12]:
    print(' That month has 31 days in it.')
else:
    print(' That month has 30 days in it.')
