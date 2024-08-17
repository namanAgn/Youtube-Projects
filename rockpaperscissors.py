# Today, we will be making the classic rock paper scissors game!

import random

def main():
  computerMove = random.randint(1,3)

  print("Rock Paper scissors")
  print("1 for Rock \n2 for Paper \n3 for scissors")
  playerMove = int(input("Choose your move: "))
  if playerMove == 1 and computerMove == 1:
    print("You picked rock, Computer picked rock. It is a tie.")
  elif playerMove == 1 and computerMove == 2:
    print("You picked rock. Computer picked paper. Computer wins.")
  elif playerMove == 1 and computerMove == 3:
    print("You picked rock. Computer picked scissors. You win.")
  elif playerMove == 2 and computerMove == 1:
    print("You picked paper. Computer picked rock. You win.")
  elif playerMove == 2 and computerMove == 2:
    print("You picked paper. Computer picked paper. It's a tie.")
  elif playerMove == 2 and computerMove == 3:
    print("You picked paper. Computer picked scissors. Computer wins.")
  elif playerMove == 3 and computerMove == 1:
    print("You picked scissors. Computer picked rock. Computer wins.")
  elif playerMove == 3 and computerMove == 2:
    print("You picked scissors. Computer picked paper. You win.")
  elif playerMove == 3 and computerMove == 3:
    print("You picked scissors. Computer picked scissors. It's a tie.")
  playAgain = input("Do you want to play again? (y/n): ")
  if playAgain == 'y':
    print("Initiallizing...")
    main()
  elif playAgain == 'n':
    print("Goodbye!")
    quit()
main()