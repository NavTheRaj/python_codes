

def main():
    status=input("Are you married or unmarried ? \nIf married then type c else type s =")
    salary=float(input("\nEnter your monthly income ="))
    salary=salary*12

    while salary<=0:
      x=input("you enetred negative number or zero .\nDo you want to enter salary again ? \nI yes then type else type n ")
      if(x=="y" or x== "Y"):
       salary=float(input("\nEnter your monthly income ="))
       salary=salary*12
      elif(x=='n' or x=='N'):
       exit() 

    if(status=="c"or status=="C"):
     couple(salary)
    elif(status=="s" or status=="S"):
      single(salary)
#For the calculation of tax and annual income of a couple   
def couple(salary):
    if(salary<=450000):
      tax= .01*salary
      salary =salary -tax
    elif(salary <=500000):
      tax1=(salary - 450000)*0.1
      tax2 =.01*450000
      tax=tax1+tax2
      salary =salary -tax
    elif(salary <=700000):
      tax1=(salary - 550000)*.2
      tax2=.1*100000
      tax3=.01*450000
      tax= tax1+tax2+tax3
      salary =salary -tax
    elif(salary<=2000000):
      tax1=(salary -750000)*.30
      tax2=200000*.2
      tax3=100000*.1
      tax4=.01*400000
      tax=tax1+tax2+tax3+tax4
      salary =salary -tax
    elif(salary>2000000):
      tax1=(salary-2000000)*.36
      tax2=1250000*.3
      tax3=2000000*.2
      tax4=100000*0.1
      tax5=450000*.01
      tax=tax1+tax2+tax3+tax4+tax5
      salary=salary-tax
    print("\nThe annual salary without tax is =",('%.2f'%(salary + tax)))
    print("The annual tax amount is = ",'%.2f'%(tax))
    print("The annual salary after tax deduction is = ",'%.2f'%(salary))
   #print("The monthly tax amount is =",'%.2f'%(tax/12))
    print("The monthly tax is =",'%.2f'%(tax/12),"\n")
  # print("The monthly salary after tax deduction is =",'%.2f'%(salary/12),"\n")
    print("The monthly salary after tax deduction is =",'%.2f'%(salary/12),"\n")

#function for calculatinng tax and annual income of single individual
def single(salary):
    if(salary<=400000):
      tax= .01*salary
      salary =salary -tax
    elif(salary <=500000):
       tax1=(salary - 400000)*0.1
       tax2 =.01*400000
       tax=tax1+tax2
       salary =salary -tax
    elif(salary <=700000):
       tax1=(salary - 500000)*.2
       tax2=.1*100000
       tax3=.01*400000
       tax= tax1+tax2+tax3
       salary =salary -tax
    elif(salary<=2000000):
      tax1=(salary -700000)*.30
      tax2=200000*.2
      tax3=100000*.1
      tax4=.01*400000
      tax=tax1+tax2+tax3+tax4
      salary =salary -tax
    elif(salary>2000000):
      tax1=(salary-2000000)*.36
      tax2=1300000*.3
      tax3=2000000*.2
      tax4=100000*0.1
      tax5=4000000*.01
      tax=tax1+tax2+tax3+tax4+tax5
      salary=salary-tax
    print("\nThe annual salary without tax is =",'%.2f'%(salary + tax))
    print("The annual tax amount is = ",'%.2f'%tax)
    print("The annual salary after tax deduction is = ",'%.2f'%salary)
   #print("The monthly tax amount is =",t'%.2f'%(tax/12))
    print("The monthly tax is =",'%.2f'%(tax/12),"\n")

    print("The monthly salary after tax deduction is =",'%.2f'%(salary/12),"\n")

main()
