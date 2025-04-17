import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

list=[rock, paper, scissors]
user1 = int(input("what to choose 0 for Rock, 1 for Scissors, 2 for Paper  "))
if user1 >=3 or user1 < 0:
    print("you typed an invalid number, you lose!")
else:
    print(list[user1])
    # print(f"user choosed {user1}")

    user2 = random.randint(0, 2)
    print(f"Computer choosed: ")
    print(list[user2])

    if user1 ==0 and user2== 2: # 0 Rock, 2 Scissor
        print("you win!")
    elif user2 ==0 and user2== 2:
        print("you lose")
    elif user2 > user1:
        print("you lose")
    elif user1 > user2:
        print("you win")
    elif user2 == user1:
        print("It's a draw")
