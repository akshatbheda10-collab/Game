

one1 = (input("You are stranded all anlone in a middle of a small remote island for "
                   "\nthe past 3 days, you are being chased by a lion, you see the ocean upcoming "
                   "\nand also a wood door that leads down to somewhere write 1 to still run and 2 to go in the wood door: "))

if one1 == "2":
    q = print("Door 1 is red")
    w = print("Door 2 is blue")
    e = print("Door 3 is green")
    He_he = input("which door would you like to go in? \n Write 1 for door 1\n Write 2 for door 2\n Write 3 for door 3    ")
    if He_he == "2":
        print("Nice the room is full of flowers")
        print("you have exited the room with flowers all over you, now there is 3 dishes infront of you, which one would you chose")
        r=print("Dish 1 has blue milk")
        t=print("Dish 2 has red water")
        t=print("Dish 3 has pink bread")
        Bob = input("which wone would you like to chose?")
        if Bob == "3":
            print("The pink was just food die you ate it and the door to the next room appered")
            print("now there are 3 houses")
          
            x = print("House 1 is a old, ugly wood house")
            c = print("House 2 is a veryice modern house")
            v = print("House 3 is a old but clean house")
            z = input("which houses would you like to chose?")
            if z == "1":
                print("House 1 has a golden key and a gold door, you go in and beat the game")
            elif z == "2":
                print("House 2 has 3 hungery lions, they eat you, good game")
            elif z == "3":
                print("House 3 has many explocives, the smallest one kills you good game")
        elif Bob == "2":
            print("The water was accutly poision")
        elif Bob == "1":
            print("The blue milk was a poision")
    elif He_he == "3":
        print("Room 3 is full of deadly snakes with posion the smallest killed you, Good Game")
    elif He_he == "1":
        print("Room 1 had fire you have died, Good Game ")
else:
    print("The loin chases you into the forest and it is way faster, you get eaten, Game Over")
