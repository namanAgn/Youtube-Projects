
import random
import time

outcomes = [1,2,3,4,5,6]

print("Dice rolling game.")
print("Would you like to roll a dice?: ")
confirmation = input("(yes/no): ")
if confirmation.lower() == 'yes':
  outcome = random.choice(outcomes)
  if outcome == 1:
    print("And the outcome is...")
    time.sleep(1)
    print(f"{outcome}!")
    print("+---+")
    print("| 1 |")
    print("+---+")
  elif outcome == 2:
    print("And the outcome is...")
    time.sleep(1)
    print(f"{outcome}!")
    print("+---+")
    print("| 2 |")
    print("+---+")
  elif outcome == 3:
    print("And the outcome is...")
    time.sleep(1)
    print(f"{outcome}!")
    print("+---+")
    print("| 3 |")
    print("+---+")
  elif outcome == 4:
    print("And the outcome is...")
    time.sleep(1)
    print(f"{outcome}!")
    print("+---+")
    print("| 4 |")
    print("+---+")
  elif outcome == 5:
    print("And the outcome is...")
    time.sleep(1)
    print(f"{outcome}!")
    print("+---+")
    print("| 5 |")
    print("+---+")
  elif outcome == 6:
    print("And the outcome is...")
    time.sleep(1)
    print(f"{outcome}!")
    print("+---+")
    print("| 6 |")
    print("+---+")


