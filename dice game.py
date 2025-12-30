

import random



print("hello, let play a game pick a random number between 1 and 20 and roll 20 side dice if it lands on your number you win!")
while True:
 guess = int(input("so what the number: "))

 number = random.randint(1, 20)


 print(number)
 if (number < guess):
    print("sorry, your number it too big!, press enter to play agen: ")

 elif (number > guess):
    print("sorry, your number is too small, press enter to play agen: ")
    
 elif (number == guess):
       print("you... Guess Correct!")
       break

 exit = (input())
     





