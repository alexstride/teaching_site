#This is a version of the program which some of you completed for prep.
#There are a number of errors in the code. Answer the questions on the relevant google form and fix the code as you go.

password = "cabbage

attempt = input("Please enter your password: "

wrongAttempts = 0

while attempt != password:
	wrongAttempts += 1
	if wrongAttempts < 3:
		print("Too many guesses; you are locked out")
		break
	attempt = input("That does not seem to be correct; please try again: ")
