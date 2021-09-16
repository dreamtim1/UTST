def acc (E, uE, J, uJ):
    #to SI
    #note what units are entered!
    J /= 1000000
    uJ /= 1000000
    E /= 1
    uE /= 1
    # calculate resistance
    R = E / J
    # return resistance and accuracy
    return R, ((uE/E)**2 + (uJ/J)**2)**0.5 * R

for i in range(2):
    E, uE, J, uJ = map(float, input().split())
    print(acc(E, uE, J, uJ))
