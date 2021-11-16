with open('temps.txt') as f:
    data = f.readlines()

datelist = [str(el) for el in data]

print(min(templist))
print(max(templist))
print(sum(templist) / len(templist))
