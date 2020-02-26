#TASK
#ENCRYPT THE 5 DIGIT PASSWORD
#USING A DICTIONARY
#0:'^'
#1:'@'
#2:'$'
#3:'*'
#....9:'&'

password={0:')',1:'!',2:'@',3:'#',4:'$',5:'%',6:'^',8:'*',9:'('}
print("-----------------------------------\n")
user_p=input("Enter your 5 digit password\n")
print('Your input password',user_p)
print("-----------------------------------\n")
decrypt=encrypt=""

print("Encrypting...\n")
print("-----------------------------------\n")
for num in user_p:
    encrypt+=password[int(num)]
print("Encrypted Password=>",encrypt)
print("-----------------------------------\n")
print("Decrypting...\n")
print("-----------------------------------\n")
for line in encrypt:
    decrypt +=str( list(password.keys())[list(password.values()).index(line)])
print("Decrypted Password=>",decrypt)
print("------------THANK YOU!!------------\n")
