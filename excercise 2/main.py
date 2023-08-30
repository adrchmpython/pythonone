import math

def calculate(a, b):
    return math.sqrt(math.pow(a, 2)+ math.pow(b, 2))


a = float(input("Podaj d…ugość boku a"))
b = float(input("Podaj długość boku b"))

c = calculate(a, b)
print("Długość przeciwprostokątnej wynosi",c,)

