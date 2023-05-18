#1
'''
for x in range(5,31,5):
    if x==10 or x==15:
        continue
    print(x)
'''
#2
'''
months={
1:{'month':'January', 'rain':''},
2:{'month':'February', 'rain':''},
3:{'month':'March', 'rain':''},
4:{'month':'April', 'rain':''},
5:{'month':'May', 'rain':''}
}

for x in months:
    months[x]['rain'] = int(input("Enter the rainfall for " + months[x]['month'] + ": "))

sortedMonths = sorted(months.items(), key=lambda x:x[1]['rain'])
print(sortedMonths)

for new_s, new_val in sortedMonths:
    min = months[new_s]['rain']
    minMonth = months[new_s]['month']
    break
for new_s, new_val in sortedMonths:
    max = months[new_s]['rain']
    maxMonth = months[new_s]['month']
sum=0
for new_s, new_val in sortedMonths:
    sum += months[new_s]['rain']
print("The minimum rainfall of " + str(min) + " was in " + minMonth)
print("The maximum rainfall of " + str(max) + " was in " + maxMonth)
print("The total rainfall is " + str(sum))
'''
#3
'''
f = open("Q3Output.txt", "w")
s = "Sam works in a company abc in New York. He joined the company in 2022. Before joining ABC, he used to work for a small firm in Arizona. He worked there from 2019 to 2021. Before moving to Arizona Sam used to live in South Dakota and he has been living there since 2000's."
punc = ".,'"
for x in s:
    if x in punc:
        s = s.replace(x," ")
t = s.split() 
yearList = []

for x in t:
    if x.isdigit():
        yearList.append(x)

f.write("a. The list of years: ")
for x in yearList:
    f.write(x + ". ")
f.write("\n")
abcCount = 0
for x in t:
    if x.lower()=="abc":
        abcCount = abcCount + 1

f.write("b. 'abc' count: " + str(abcCount) + " ,\n")
f.write("c. Maximum of year list: " + str(max(yearList)) + ", Minimum of year list: " + str(min(yearList)) + "\n")

newstring = s.replace("h","_")
f.write("d. The new string: " + newstring + "\n")
f.close()
'''

#4
'''
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
'''

#5
files = ["File1.txt","File2.txt","File3.txt","File4.txt","File5.txt","File6.txt"]
output = open("Q5Output.csv", "w")
output.write("Filename,Substring\n")

for x in files:
    f = open(x, "r")
    s = f.read()
    output.write(x+",")
    data = s.split(".")
    for x in data:
        if x.find("lives")>0:
            output.write(x[x.find("lives")+6:] + "\n")
    f.close()
output.close()
