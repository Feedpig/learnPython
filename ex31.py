print("""You enter a dark room with two doors
Do you go through door #1 or door #2?
      """)
promt = '>>>'
door = input(promt)

if door == '1':
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear")

    bear = input(promt)

    if bear == '1':
        print("The bear eats you face off. Good job!")
    elif bear == '2':
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing{bear} is probably better\nBear runs away")

elif door == '2':
    print("You stare into the endless abyss at Ctuhulhu's retina."
      "\n1. Blueberries."
      "\n2. Yellow Jacket clothespins."
      "\n3. Understanding revolvers yelling melodies")

    
    insanity = input(promt)
    if insanity == '1' or insanity == '2':
        print("Your body survives powered by a mind of jello")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck")
        print("Good job!")
    

else:
    print("You stumble aroud and fall on a knife and die. Good job!")