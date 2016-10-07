fave_cars = []
entercar = ""

print ("Enter the make and model of each of your favorite cars. When you are finished, type done.")
while entercar != "done":
    entercar = raw_input("Enter a car to add it to the list. ")
    if entercar != "done":
        fave_cars.append(entercar)

fave_cars.sort()
for car in fave_cars:
    print car
print("\n")
