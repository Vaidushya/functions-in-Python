r = float(input("Enter radius: "))

def circle_circumdaira(r):
    2*3.14159265359*r

print(circle_circumdaira(9))

def weather_condition():
    print("weather is pleasent in",spring)
    print("weather is same in",autumn)

spring = "autumn"
autumn = "winter"

weather_condition()

def add(p,q):
    return(p + q)

def subtract(p,q):
    return(p - q)

def multiply(p,q):
    return(p * q)

def divide(p,q):
    return(p / q)


print("Please select operation:")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

choice = input("Please enter choice (a/b/c/d):")

n_1 = int(input("Please enter the first number: "))
n_2 = int(input("Please enter the second number: "))

if(choice == 'a'):
    print(n_1, "+", n_2, "=", add(n_1, n_2))
elif(choice == 'b'):
    print(n_1, "-", n_2, "=", subtract(n_1, n_2))
elif(choice == 'c'):
    print(n_1, "*", n_2, "=", multiply(n_1, n_2))
elif choice == 'd':
  print(n_1, "/", n_2, "=", divide(n_1, n_2))
else:
  print("This is an invalid input")