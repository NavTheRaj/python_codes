import matplotlib.pyplot as plt

def main():
    #x,y={(0,0),(1,3),(2,2),(3,5),(4,2)} GIVEN POINTS
    x_cords=[0,1,2,3,4]
    y_cords=[0,3,2,5,2]

    #BUILD A LINE GRAPH TO PLOT THE POINTS

    plt.plot(x_cords,y_cords)

    plt.show()

main()
