score = int(input('Enter the number of points: '))
if score < 0:
    print('You cannot obtain negative points')
elif score > 100:
    print('You cannot obtain so many points')
elif score < 66:
    print('The obtained points are not enough to be considered for admission')
else:
    print('The obtained points are enough to be considered for admission')
