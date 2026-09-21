print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?\n"))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    wants_photos = input("Do you want to take the photos? Type y for yes and n for no:\n")
    if wants_photos == "y":
        bill += 3
        print(f"Your final bill is ${bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
