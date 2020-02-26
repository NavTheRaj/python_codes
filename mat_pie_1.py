import matplotlib.pyplot as plt

def main():
    #SET THE VALUES
    values=[20,50,40,50,90]

    labels=['Math','Science','Computer','English','Nepali']

    plt.legend()
    plt.title('Marks Obtained')
    #PLOT THE POINTS
    plt.pie(values,labels=labels)



    plt.show()

main()
