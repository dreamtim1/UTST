def acc (E, uE, J, uJ):
    #to SI
    #note what units are entered!
    J /= 10**6
    uJ /= 10**6
    E /= 1
    uE /= 1
    # calculate resistance
    R = E / J
    # return resistance and accuracy
    return R, ((uE/E)**2 + (uJ/J)**2)**0.5 * R

def uJcalc(mrange, rdg, digit):
    if mrange in ['200uA', '2mA', '20mA']:
        return 1/100 * rdg + 2 * digit / (3**0.5)
    if mrange == '200mA':
        return 1.5/100 * rdg + 2 * digit / (3**0.5)
    if mrange == '10A':
        return 3/100 * rdg + 2 * digit / (3**0.5)
    else:
        return 'error'

def uEcalc(mrange, rdg, digit):
    if mrange in ['100uV', '2V', '20V', '200V']:
        return (0.5/100 * rdg + 2 * digit) / (3**0.5)
    if mrange == '600V':
        return 0.8/100 * rdg + 2 * digit / (3**0.5)
    else:
        return 'error'

mrange = '20V'
num = float(input())
digit = 0.01
print(uEcalc(mrange, num, digit), mrange)
