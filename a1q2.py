#prompt 1
prompt = "\nEnter a number :"
#take input from user
n = int(input(prompt))
#define a factorial from 1
factorial = 1
#using conditions we trap zero and negative numbers by user
if n < 1:
	print("sorry, factorial of negative number doesnt exist")
elif n == 0:
	print("The factorial of 0 is 1")
else :
	#use loop arund the n using range of 1 to n+1 
	for i in range(1,n+1):
	#looping through factorial
		factorial = factorial*i
		print(factorial)
	print(f"the factorial of {n} is {factorial}")

