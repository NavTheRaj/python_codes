n = int(input("Enter the limit value for dictionary:"))
d = {}

for i in range(n):
  #  print("Key"+int(i))
    print('Iteration',i+1)
    keys = input('Key->') # here i have taken keys as strings
   # print("Value"+int(i))
    values = input('Values->') # here i have taken values as integers
    d[keys] = values

print(d)


