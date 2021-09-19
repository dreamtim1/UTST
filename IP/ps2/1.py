name = input(' Enter your last name: ')
s, m = False, False
if input(' Are you single or married (s/m)? ') == 's':
    s = True
if input(' Are you male or female (m/f)? ') == 'm':
    m = True
if m:
    gr = 'Mr'
elif s:
    gr = 'Miss'
else:
    gr = 'Mrs'
print('Nice to have you here, ' + gr + ' ' + name)
