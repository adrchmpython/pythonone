from orders import create_new_order

print ("Witaj w naszym sklepie")
product_name = input ("podaj nazę produktu")
quantity = input("Podaj ilość produktu")

result = create_new_order(product_name, quantity)
if result is not None :
    total_price = result["total price"]
    print("Łączna wartość wynosi" ,total_price,)


