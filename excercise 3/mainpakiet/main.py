import calculations

def ask_for_value (message) :
    input_value = input(message)
    return int(input_value)

initial_value = ask_for_value("Podaj wartość początkową")
percentage = ask_for_value("Podaj procent")
years = ask_for_value("Podaj liczbę lat")

final_value = calculations.calculation(initial_value, percentage, years)
print("Po", years, "latach twoja lokata będzie warta", final_value,)

    