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