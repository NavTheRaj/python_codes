tax=0
sal=int(input("Enter the monthly salary"));

tot_sal=12*sal;

print("Monthly Salary->",sal,"\nAnnual Salary->",tot_sal);

if tot_sal<400000:
    tax=tax+tot_sal*1/100;
    print("Your annaul tax is->",tax)

elif tot_sal<500000:
    tax=tax+400000*1/100+(tot_sal-400000)*10/100;
    print("Your annaul tax is->",tax)


elif tot_sal<700000:
    tax=tax+400000*1/100+100000*10/100+(tot_sal-500000)*20/100;
    print("Your annaul tax is->",tax)


elif tot_sal<1900000:
    tax=tax+400000*1/100+100000*10/100+200000*20/100+(tot_sal-700000)*30/100;
    print("Your annaul tax is->",tax)


elif tot_sal>1900000:
    tax=tax+400000*1/100+100000*10/100+200000*20/100+1300000*30/100+(tot_sal-1900000)*36/100;

print("Your annaul tax is->",tax)

else:
    print("Invalid Input")
