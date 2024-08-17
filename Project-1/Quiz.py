import os
clear = lambda: os.system('cls')
clear()

print("Quiz \nYou will be asked 5 questions on computer related topics.")

confirmation = input('Are you ready to begin? (yes/no): ')

score = 0
feedback = ''

if confirmation.lower() == 'yes':
  print("Question no.1: ")
  print("What is the purpose of the GPU?: \na) To process information \nb) To render graphics \nc) To perform mathematical operations")
  question1Ans = input("Enter your answer: ")
  if question1Ans.lower() == 'b':
    print("You guessed correctly!")
    score += 1
  elif question1Ans.lower() == 'a' or 'c':
    print("You guess incorrectly! the answer was b)")
    feedback += 'Question 1 was wrong \n'
  elif question1Ans.lower() != 'a' and 'b' and 'c':
    print("Invalid input.")
  
  print("Question no.2:")
  print("What part of the computer is known as it's brain?: \na) CPU \nb) GPU \nc) PSU")
  question2Ans = input("Enter your answer: ")
  if question2Ans.lower() == 'a':
    print("You guessed correctly!")
    score += 1
  elif question2Ans.lower() == 'b' or 'c':
    print("You guessed incorrectly! The answer was a)")
    feedback += 'Question 2 was wrong \n'
  elif question2Ans.lower() != 'a' and 'b' and 'c':
    print("Invalid input")
  print("Would you like to increase the difficulty?:")
  difficulty = input("(yes/no): ")
  if difficulty.lower() == 'yes':
    print("Difficulty has been increased.")

    print("Question no.3:")
    print("What is the function of the OS?: \na) To handle software and hardware resources \nb) To render graphics \nc) To run programs")
    question3Ans = input("Enter your answer: ")
    if question3Ans.lower() == 'a':
      print("You guessed correctly!")
      score += 2
    elif question3Ans.lower() == 'b' or 'c':
      print("You guessed incorrectly! The answer was a)")
      feedback += 'Question 3 was wrong \n'
    elif question3Ans.lower() != 'a' and 'b' and 'c':
      print("Invalid input")

    print("Question no.4:")
    print("Name the biggest microchip producer: \na) AMD \nb) Intel \nc) TSMC")
    question4Ans = input("Enter your answer: ")
    if question4Ans.lower() == 'c':
      print("You guessed correctly!")
      score += 2
    elif question4Ans.lower() == 'a' or 'b':
      print("You guessed incorrectly! The answer was c)")
      feedback += 'Question 4 was wrong \n'
    elif question4Ans.lower() != 'a' and 'b' and 'c':
      print("Invalid input")

    print("Final question:")
    print("Which company's CEO is Lisa Su?: \na) AMD \nb) Nvidia \nc) MSI")
    question5Ans = input("Enter your answer: ")
    if question5Ans.lower() == 'a':
      print("You guessed correctly!")
      score += 2
    elif question5Ans.lower() == 'a' or 'b':
      print("You guessed incorrectly! The answer was c)")
      feedback += 'Question 5 was wrong'
    elif question5Ans.lower() != 'a' and 'b' and 'c':
      print("Invalid input")

    print("The quiz has ended!")

  elif difficulty.lower() == 'no':
    print("Difficulty has not been increased.")

    print("Question no.3:")
    print("What is the display of a PC known as?: \na) Monitor \nb) Screen c) Display \nd) All of the above")
    question3Ans = input("Enter your answer: ")
    if question3Ans.lower() == 'd':
      print("You guessed correctly!")
      score += 1
    elif question3Ans.lower() == 'a' or 'b' or 'c':
      print("You guessed incorrectly! The answer was d)")
      feedback += 'Question 3 was wrong \n'
    elif question3Ans.lower() != 'a' and 'b' and 'c':
      print("Invalid input")

    print("Question no.4:")
    print("What is the name of the hardware used to control the cursor?: \na) Mouse \nb) Keyboard \nc) Scroll wheel")
    question4Ans = input("Enter your answer: ")
    if question4Ans.lower() == 'a':
      print("You guessed correctly!")
      score += 1
    elif question4Ans.lower() == 'c' or 'b':
      print("You guessed incorrectly! The answer was a)")
      feedback += 'Question 4 was wrong \n'
    elif question4Ans.lower() != 'a' and 'b' and 'c':
      print("Invalid input")

    print("Final question:")
    print("What is the full form of PSU?: \na) Power supply unit \nb) Penguin Scuba Unit \nc) Pineapple Supply unit")
    question5Ans = input("Enter your answer: ")
    if question5Ans.lower() == 'a':
      print("You guessed correctly!")
      score += 1
    elif question5Ans.lower() == 'c' or 'b':
      print("You guessed incorrectly! The answer was a)")
      feedback += 'Question 5 was wrong'
    elif question5Ans.lower() != 'a' and 'b' and 'c':
      print("Invalid input")

  print("The quiz has ended!")
  
  print(f"You got {score} marks.")

  if score >= 1 and score <= 2:
    print("You should work on your computer trivia.")
  elif score > 2 and score <= 3:
    print("You are good at computer trivia but should try and improve")
  elif score > 3 and score <= 4:
    print("You are decent at computer trivia.")
  elif score >= 5 and score <= 6:
    print("You are pretty good at computer trivia.")
  elif score > 6:
    print("You used google or are really good at computer trivia.")
  
  print("Here's a more detailed summary of how you did:")
  print(feedback)

  with open("quiz_summary.txt", "r+") as highScore:
    read = highScore.read()
    readInt = int(read)

    if score > readInt:
      print("You have set a new high score! \nWould you like to save it?")
      saveInput = input("(yes/no): ")
      if saveInput.lower() == 'yes':
        highScore.seek(0)
        highScore.truncate()
        highScore.write(str(score))
        print("High score saved.")
      else:
        print("High score has not been saved.")
    else:
      print(f"The high score is {readInt}. You scored {score}. Sadly, no new high score was set.")


elif confirmation.lower() == 'no':
  print("Goodbye!")
  quit()

  # our quiz project is now complete!
  # you can add as many questions, answers, score whatever you want!
  # a link to the code would be in the description and/or comments
  # goodbye!
