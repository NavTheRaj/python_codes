import random 

def get_input():
    random_list=[]
    for i in range(30):
        a=random.randrange(1,100)
        random_list.append(a)
        #random_list.append(random.randrange(1,100))
    return random_list

def slicing_fun(new_tuple):
    new_list=[]
    my_tuple=new_tuple[:3]+new_tuple[9:20]+new_tuple[-3:]
    new_list=list(my_tuple)
    print('The list after adding the elements is',new_list)
    return sum(new_list)
    

def main():
    random_list=get_input() #generating list of 30 numbers
    random_list.sort()  #sorting the list
    new_tuple=tuple(random_list)  #converting random_list to tuple
    print(new_tuple)
    print('--------------------------------------------\n')
    print('The first three elements are::',new_tuple[:3])
    print('--------------------------------------------\n')
    
    print('The elements from index 10 to 20 are::',new_tuple[9:20])
    print('--------------------------------------------\n')
    print('The last three elements are::',new_tuple[-3:])
    print('--------------------------------------------\n')
    
    total_sum=slicing_fun(new_tuple)
    print('--------------------------------------------\n')
    print('The sum is',total_sum)
    print('--------------------------------------------\n')
main()


