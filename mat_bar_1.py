import matplotlib.pyplot as plt

def main():
    #CREATE X CO ORDS
    x_cord=[0,10,20,30]
    #CREATE Y CORDS
    y_cord=[100,200,300,400]
    #PLOTTING THE POINTS
    #plt.plot(x_cord,y_cord,color='r')
    plt.bar(x_cord,y_cord,5,color=('r','c','b','g'))#5 is bar width
    #NOW DISPLAYING THE BAR
    plt.show()

main()
