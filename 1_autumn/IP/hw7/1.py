with open('temps.txt') as f:
    data = f.readlines()

templist = [int(el) * 9/5 + 32 for el in data]

print(min(templist))
print(max(templist))
print(sum(templist) / len(templist))
