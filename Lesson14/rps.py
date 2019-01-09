import random
import time

print('*' * 80)

print("Let's Play Rock, Paper, Scissors!!!")

print()

choice =  input("Choose one: rock, paper or scissors: ")
choice = choice.lower() 

computer_choice = random.choice(['rock', 'paper', 'scissors'])

print()
print("Rock...")
time.sleep(1)
print("Paper...")
time.sleep(1)
print("Scissors...")
time.sleep(1)
print("Says shoot!")

while choice == "rock" and computer_choice == "rock":
	time.sleep(1)
	print()
	print("You chose " + choice + " and the computer chose " + computer_choice + ".")
	time.sleep(1)
	print("It's a draw, try again!")
	time.sleep(1)
	print()
	time.sleep(1)
	choice =  input("Choose rock, paper or scissors: ")
	choice = choice.lower() 
	print()
	print("Rock...")
	time.sleep(1)
	print("Paper...")
	time.sleep(1)
	print("Scissors...")
	time.sleep(1)
	print("Says shoot!")

while choice == "scissors" and computer_choice == "scissors":
	time.sleep(1)
	print()
	print("You chose " + choice + " and the computer chose " + computer_choice + ".")
	time.sleep(1)
	print("It's a draw, try again!")
	time.sleep(1)
	print()
	time.sleep(1)
	choice =  input("Choose rock, paper or scissors: ")
	choice = choice.lower() 
	print()
	print("Rock...")
	time.sleep(1)
	print("Paper...")
	time.sleep(1)
	print("Scissors...")
	time.sleep(1)
	print("Says shoot!")

while choice == "paper" and computer_choice ==  "paper":
	print()
	time.sleep(1)
	print("You chose " + choice + " and the computer chose " + computer_choice + ".")
	time.sleep(1)
	print("It's a draw, try again!")
	print()
	time.sleep(1)
	choice =  input("Choose rock, paper or scissors: ")
	choice = choice.lower() 
	print()
	time.sleep(1)
	print("Rock...")
	time.sleep(1)
	print("Paper...")
	time.sleep(1)
	print("Scissors...")
	time.sleep(1)
	print("Says shoot!")

if choice == "rock" and computer_choice == "scissors": 
	print()
	time.sleep(1)
	print("You chose " + choice + " and the computer chose " + computer_choice + ".")
	time.sleep(1)
	print("Rock beats scissors!")
	print()
	time.sleep(1)
	print("You won!")

elif choice == "rock" and computer_choice == "paper": 
	print()
	time.sleep(1)
	print("You chose " + choice + " and the computer chose " + computer_choice + ".")
	time.sleep(1)
	print("Paper beats rock!")
	print()
	time.sleep(1)
	print("You lost!")

elif choice == "scissors" and computer_choice == "rock":
	print()
	time.sleep(1)
	print("You chose " + choice + " and the computer chose " + computer_choice + ".")
	time.sleep(1)
	print("Rock beats scissors!")
	print()
	time.sleep(1)
	print("You lost!")

elif choice == "scissors" and computer_choice == "paper":
	print()
	time.sleep(1)
	print("You chose " + choice + " and the computer chose " + computer_choice + ".")
	time.sleep(1)
	print("Scissors beats paper!")
	print()
	time.sleep(1)
	print("You won!")

elif choice == "paper" and computer_choice == "rock":
	print()
	time.sleep(1)
	print("You chose " + choice + " and the computer chose " + computer_choice + ".")
	time.sleep(1)
	print("Paper beats rock!")
	print()
	time.sleep(1)
	print("You won!")

else:
	print()
	time.sleep(1)
	print("You chose " + choice + " and the computer chose " + computer_choice + ".")
	time.sleep(1)
	print("Scissors beats paper!")
	print()
	time.sleep(1)
	print("You lost!")

print()
time.sleep(1)
print("Game over!")
print('*' * 80)










