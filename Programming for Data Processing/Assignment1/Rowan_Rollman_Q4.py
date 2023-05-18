a = {5:'New York', 2: 'Dallas', 6: 'San Marcos'} 
b = {7: 'Texas', 4: 'San Francisco'}
c = {3: 'Phoenix', 1: 'Arizona'}
c.update(b)
c.update(a)
print("New Dictionary:")
print(c)

myKeys = list(c.keys())
myKeys.sort()
sortedDict = {i: c[i] for i in myKeys}
for k,v in sortedDict.items():
    print(str(k) + " :: " + v)