year = eval(input("Enter your birth year:"))

if year % 12 == 0 :
    animal = 'Monkey'
    print("Year of the", animal)
elif year % 12 == 1:
    animal = "Rooster"
    print("Year of the", animal)
elif year % 12 == 2:
    animal = "Dog"
    print("Year of the", animal)
elif year % 12 == 3:
    animal = "Pig"
    print("Year of the", animal)
elif year % 12 == 4:
    animal = "Rat"
    print("Year of the", animal)
elif year % 12 == 5:
    animal = "Ox"
    print("Year of the", animal)
elif year % 12 == 6:
    animal = "Tiger"
    print("Year of the", animal)
elif year % 12 == 7:
    animal = "Rabbit"
    print("Year of the", animal)
elif year % 12 == 8:
    animal = "Dragon"
    print("Year of the", animal)
elif year % 12 == 9:
    animal = "Snake"
    print("Year of the", animal)
elif year % 12 == 10:
    animal = "Horse"
    print("Year of the", animal)
elif year % 12 == 11:
    animal = "Sheep"
    print("Year of the", animal)
    
else:
    print("Invalid year. Enter a valid birth year included in the Chinese zodiac cycle.")