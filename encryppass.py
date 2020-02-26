#TASK
#ENCRYPT THE 5 DIGIT PASSWORD
#USING A DICTIONARY
#0:'^'
#1:'@'
#2:'$'
#3:'*'
#....9:'&'

password={0:')',1:'!',2:'@',3:'#',4:'$',5:'%',6:'^',8:'*',9:'('}
decryp=encryp=""

def encrypt(user_p):
    for num in user_p:
        encryp+=password[int(num)]
	return encryp

def decrypt(encrypt_pass):
    for line in encrypt_pass:
        decryp +=str( list(password.keys())[list(password.values()).index(line)])
	return decryp

def main():
	user_p=input("Enter your 5 digit password\n")
	print('Your input password',user_p)
	encrypt_pass=encrypt(user_p)
	decrypt_pass=decrypt(encrypt_pass)
	print("Encrypted Password=>",encrypt_pass)
	print("Decrypted Password=>",decrypt_pass)
	print("------------THANK YOU!!------------\n")
