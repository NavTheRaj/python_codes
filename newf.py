with open("piedata.txt","w") as f:
    f.write('ram\nshyam\n')
    f.write(str(22))

f.close()

with open("piedata.txt","r") as fr:
    #print(fr.read())
    line1=fr.readline()  #To print the first line
    line1=line1.rstrip('\n')
    line2=fr.readline()
    line2=line2.strip('\n')
    print(line1)
    print(line2)
