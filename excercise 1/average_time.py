

import speed_calculator
running_distance = float(input("Ile km przebiegłeś"))
running_time = float(input("Jaki czas"))

speed = speed_calculator.speed(running_distance, running_time)
print("Twoja średnia rędkośc to", speed, "km/h")

