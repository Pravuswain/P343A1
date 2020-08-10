#first make a loopof numbers begining from 1
curr_no = 0
#create an empty set to gather alll numbers
data = []
while curr_no < 100:
	#increment by +1 to prevent infinite loops
	curr_no += 1
	#put the set of numbers inside data set
	data.append(curr_no)
#using summation function and printing the result
result = sum(data)
print(result)
