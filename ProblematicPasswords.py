#This is a version of the program which some of you completed for prep.
#There are a number of errors in the code. Answer the questions on the relevant google form and fix the code as you go.

#The first error is in the following line
password = cabbage

#The second error is in the following line
attempt = input("Please enter your password: "

wrongAttempts = 0

while attempt != password:
	wrongAttempts += 1
	# the final error is in the following line
	if wrongAttempts < 3:
		print("Too many guesses; you are locked out")
		break
	attempt = input("That does not seem to be correct; please try again: ")
