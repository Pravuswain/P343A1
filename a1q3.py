#prompt1
prompt1 = "\nsum of series of 1/n.Enter n :"
#set the input as integer
n = int(input(prompt1))
#define sum1 and sum2 to prepare a loop
sum1 = 0
sum2 = 0
#using for loop and setting a range
for i in range(1,n+1):
	sum1 = sum1 +(1/i)
#sum of preceding series
for j in range(1,n):
	sum2 = sum2 +(1/j)

#set conditions as asked by the question
def difference(sum2):
#here we are taking differnce between preceding term and current term
	if sum2 <= sum1:
		return sum1-sum2
	else:
		return sum2-sum1
#then with conditiona we print aum only for desired series i.e. where the sum doesnt changes more than 0.001 from preceding term
if difference(sum2) <= 0.001:
	print(sum1)
else:
	print("the sum changes by more than 0.001")
