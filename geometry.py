import random
import circle


def display():
    choice = int(
        input(
            "\n1.Area of Circle\n2.Circumeference of circle\n3.Total Surface area\n4.Quit\n "
        )
    )
    return choice


def main():
    radius = random.randint(1, 5)
    print(radius)
    n = display()
    while n<4:
     if n == 1:
        area = circle.area(radius)
        print("\nThe area of circle is->", area)
        display()
     elif n == 2:
        circum = circle.circumference(radius)
        print("\nThe circumference of circle is->", circum)
        display()
     elif n == 3:
        height = int(input("\nEnter the height of cylinder:"))
        tsa = circle.area(radius) + circle.circumference(radius) * height
        print("The total surface area of cylinder is->", tsa)
        display()
     elif n == 4:
        print("Exiting..")
        exit()
     else:
        print("\nInvaild input")
        display()
        


main()

