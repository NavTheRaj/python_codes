def takeSecond(elem):
    return elem[1]

def main():
    new_mat=[['Aarati',40,1412],['Akash',20,1001],['Janice',45,1401]]
    new_mat.sort(key=takeSecond)
    print(new_mat)

main()
