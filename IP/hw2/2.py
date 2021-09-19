while True:
    try:
        month = int(input('Enter the number of a month: '))
        if month > 12 or month < 1:
            print('The number of a month must be in the range [1-12]')
            continue
        break
    except:
        print('Please enter an integer number')

while True:
    try:
        year = int(input('Enter a year: '))
        if year < 1:
            print('Year must be positive')
            continue
        break
    except:
        print('Please enter an integer number')
