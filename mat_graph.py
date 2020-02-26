import matplotlib.pyplot as plt

def main():
    #SET UP THE CO ORDINATES
    x_cords=[0,1,2,3,4,5]
    y_cords=[7,0,4,5,4.5,-2]

    #ADD THE POINTS IN PLOT FUNCTION
    plt.plot(x_cords,y_cords,marker='^')

    #SET UP THE TITLE OF GRAPH
    plt.title('Sample Data')

    #SET UP THE LABELS OF GRAPH
    plt.xlabel('This is the x-axis')
    plt.ylabel('This is the y-axis')

    #SET THE LIMITATIONS OF GRAPH
    plt.xlim(xmin = -3,xmax = 10)
    plt.ylim(ymin = -3, ymax = 10)

    #SHOW THE GRIDSLINES IN GRAPH
    plt.grid(True)
    #USING XTICKS AND YTICKS
    plt.xticks([1,2,3,4,5],['2016','2017','2018','2019','2020','2021'])
    plt.yticks([7,0,4,5,4.5,-2],['$1M','$2M','$3M','$4M','$5M','$6M'])

    #USING MARKER IN COORDINATES

    #SHOW THE GRAPH
    plt.show()

main()

