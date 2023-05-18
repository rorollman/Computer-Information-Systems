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