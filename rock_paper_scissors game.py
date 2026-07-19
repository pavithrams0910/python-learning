user = input("Enter Rock, Paper, or Scissors: ")
computer = "Rock"

print("Computer chose:", computer)

if user == computer:
    print("It's a Tie!")
elif user == "Paper" and computer == "Rock":
    print("You Win!")
elif user == "Scissors" and computer == "Paper":
    print("You Win!")
elif user == "Rock" and computer == "Scissors":
    print("You Win!")
else:
    print("Computer Wins!")
