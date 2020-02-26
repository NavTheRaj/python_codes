import math

def median_calc(terms,n):
    terms.sort()
    pos=(n+1)/2-1
    if len(terms)%2!= 0 :
        
        median=(terms[math.ceil(pos)]+terms[math.floor(pos)])/2
        return median
    
    else:
        median=(terms[math.floor(pos)]+terms[math.ceil(pos)])/2
        return median




def main():

  list1=[]
  n_terms=int(input("Enter the number of terms to operate"))
  print("Enter the numbers now\n")
  for i in range(0,n_terms):
      item = int(input())
      list1.append(item)

  median=median_calc(list1,n_terms)

  print("The median is",median)

main()
