distance = float(input("Enter distance in KM: "))
age = int(input("Enter passenger age: "))
print("1. Sleeper")
print("2. AC")
choice = int(input("Select class: "))

if distance <= 100:
    fare = distance * 1
else:
    fare = 100 + (distance - 100) * 2

if choice == 2:
    fare = fare * 2

if age >= 60:
    fare = fare * 0.90

reservation = 50
total = fare + reservation

print("Base Fare:", fare)
print("Reservation Fee:", reservation)
print("Total Railway Fare:", total)