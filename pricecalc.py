


markprice=int(input("Enter marked price\n"));

vat=int(input("Enter vat in percentage\n"));

dis=int(input("Enter dicount in percentage\n"));

result=markprice-dis/100*markprice;

result=result+13/100*result;

print ("Final selling price is",result);
