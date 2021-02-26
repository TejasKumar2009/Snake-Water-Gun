import random

player_name = str(input("Enter the player name:"))
print("\t\t\tSnake Water Gun")

your_points = 0
comp_points = 0
a = 0

comp1 = ["Snake","Water","Gun"]
comp2 = random.choice(comp1)

while(a<10):

    comp1 = ["Snake","Water","Gun"]
    comp2 = random.choice(comp1)
    you = str(input("\nEnter (s) for snake (w) for water and (g) for gun:\n"))

    if you=="s" and comp2=="Water":
        print("\n",player_name,"aapne nikala: snake")
        print("Computer ne nikala: Water\n")
        print(player_name,"Your 1 more point is added")
        your_points = your_points + 1
        print("Your points:",your_points)
        print("Computer Points:",comp_points)
        print(player_name," you Won")


    elif  (you=="s" and comp2=="Gun"):

        print("\n",player_name,"aapne nikala: snake")
        print("Computer ne nikala: Gun\n")
        print("Computer's 1 more point is added")
        comp_points = comp_points + 1
        print(player_name,"Your points:", your_points)
        print("Computer Points:", comp_points)
        print(player_name," you Lose")


    elif you=="w" and comp2=="Snake":
          print("\n",player_name,"aapne nikala: Water")
          print("Computer ne nikala: Snake\n")
          print("Computer's 1 more point is added")
          comp_points = comp_points + 1
          print(player_name,"Your points:", your_points)
          print("Computer Points:", comp_points)
          print(player_name," you lose")


    elif you=="w" and comp2=="Gun":
          print("\n",player_name,"aapne nikala: Water")
          print("Computer ne nikala: Gun\n")
          print(player_name,"Your 1 more point is added")
          your_points = your_points + 1
          print("Your points:", your_points)
          print("Computer Points:", comp_points)
          print(player_name," you Won")


    elif you=="g" and comp2=="Snake":
          print("\n",player_name,"aapne nikala: Gun")
          print("Computer ne nikala: Snake\n")
          print(player_name,"Your 1 more point is added")
          your_points = your_points + 1
          print("Your points:", your_points)
          print("Computer Points:", comp_points)
          print(player_name," you Won")


    elif you=="g" and comp2=="Water":
          print("\n",player_name,"aapne nikala: Gun")
          print("Computer ne nikala: Water\n")
          print("Computer's 1 more point is added")
          comp_points = comp_points + 1
          print(player_name,"Your points:", your_points)
          print("Computer Points:", comp_points)
          print(player_name," you Lose\n")

    elif you=="g" and comp2=="Gun":
        print("\n",player_name,"aapne nikala: Gun")
        print("Computer ne Nikala: Gun")
        print(player_name, " tie ho chuka hai dono ne Gun hi nikala hai\n")
        print(player_name,"Your points:", your_points)
        print("Computer Points:", comp_points)

    elif you=="s" and comp2=="Snake":
        print("\n",player_name,"aapne nikala: Snake")
        print("Computer ne Nikala: Snake")
        print(player_name, " tie ho chuka hai dono ne Snake hi nikala hai\n")
        print(player_name,"Your points:", your_points)
        print("Computer Points:", comp_points)

    elif you=="w" and comp2=="Water":
        print("\n",player_name,"aapne nikala: Water")
        print("Computer ne Nikala: Water")
        print(player_name, " tie ho chuka hai dono ne Water hi nikala hai\n")
        print(player_name,"Your points:", your_points)
        print("Computer Points:", comp_points)

    a = a + 1
    print("\n",10-a," no. of chances left\n")

    if a>10:
        print("game over")
    elif comp_points<your_points:
            print("You win",player_name," and Computer loose")
            print(f"Your Total points is {your_points} and computer points is {comp_points}")

    elif comp_points>your_points:
            print("You loose",player_name," and Computer win")
            print(f"Your Total points is {your_points} and computer points is {comp_points}")

    elif comp_points==your_points:
            print("Game tie",player_name)
            print(f"Your Total points is {your_points} and computer points is also {comp_points}")
#Game end
