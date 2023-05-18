f = open("Q3Output.txt", "w")
s = "Sam works in a company abc in New York. He joined the company in 2022. Before joining ABC, he used to work for a small firm in Arizona. He worked there from 2019 to 2021. Before moving to Arizona Sam used to live in South Dakota and he has been living there since 2000's."
punc = ".,'"

newstring = s.replace("h","_")
newstring = newstring.replace("H","_")

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


f.write("d. The new string: " + newstring + "\n")
f.close()