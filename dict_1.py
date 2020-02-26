#CREATE A DICTIONARY
std_info = {'Ram':1,'Shyam':2}
print(len(std_info))
search=input("Enter the name to search")
if search in std_info:           #SEARCHING DATA INSIDE THE DICTIONARY
    print(search,'->',std_info[search])#ACCESSING VALUE
    del std_info[search]
    print("Deleting..\n")
else:
    print(search+"is not in the dictionary")

print(len(std_info))
