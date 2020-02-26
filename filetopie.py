data=[]
for i in range(0,5):
    x=int(input())
    data.append(x)

fname=input("Enter the filename")

with open(fname,"w") as fn:
    fn.write(str(data))
fn.close()


with open("filepie.txt","r") as fr:
    lines = fr.read().splitlines()
print(lines)
fr.close()
