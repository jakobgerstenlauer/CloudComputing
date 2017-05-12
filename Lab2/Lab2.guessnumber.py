import random
randomNumber = random.randrange(0,20)
print("Random number between 0 and 20 has been generated")
guessed = False
while guessed==False:
    userNumber = int(input("Introduce your guess number: "))
    if userNumber==randomNumber:
        guessed = True
	print("Yes, " + str(randomNumber) + " is correct!")
        print("Excellent, Well done!")
    elif (userNumber > 20) | (userNumber < 0):
	print("Haha, you're a real joker! The random number is between 0 and 20! Try again.") 
    elif userNumber > randomNumber:
        print("Try one more time, a bit lower")
    elif userNumber < randomNumber:
        print("Try one more time, a bit higher")

