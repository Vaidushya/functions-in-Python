def squre_peri(x):
    perimeter = 4*x
    print("Perimeter of square is ", perimeter)

def rec_peri():
    perimeter = 2(l + b)
    return perimeter

def circle_circumdaira(r):
    c = 2*3.14159265359*r
    print("circumference of circle is", c)

r = float(input("Enter radius of circle: "))
circle_circumdaira(r)

x = int(input("Enter side of square->"))
squre_peri(x)

l = int(input("Enter length of rectangle->"))
b = int(input("Enter width of rectangle->"))
print(rec_peri(l, b))