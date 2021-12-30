import sys, random
#these are the representation for the hands, i did my best :)
#rock paper scissor game
rock = '''
-------------
 | | |       (---)
 | | |       (---)
 | | |       (---)
 | | |       (---)
 | | |       (-)
-----------
'''

paper = '''
-------------
 | | |       (--------)
 | | |       (--------)
 | | |       (----------)
 | | |       (---------)
 | | |       (------)
-----------
'''

scissors = '''
-------------
 | | |       (---)
 | | |       (---)
 | | |       (----------)
 | | |       (---------)
 | | |       (--)
-----------
'''



user = int(input("Choose 0 for rock, 1 for paper and 2 for scissors\n"))

#check the usr input
if user not in [0, 1, 2]:
    print("wrong choice")
    sys.exit()

computer = random.randint(0,2)

choices = [rock,paper,scissors]

print("You chose\n")
print(choices[user])

print("Computer chose\n")
print(choices[computer])

if user == 0 and computer == 2:
    print("You win!")
elif computer == 0 and user == 2:
    print("You lose!")
elif computer > user:
    print("You lose!")
elif user > computer:
    print("You win!")
elif user == computer:
    print("Tied!")
