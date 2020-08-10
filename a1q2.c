#include <stdio.h>

int main()
{
	//define all variables
	double i ,fact = 1,n;
	//ask the user for the info
	printf("Enter a number:");
	scanf("%lf" , &n );
	//use condiotionals to eliminate negative no.
	if (n<0){
		printf("please enter a number greater than 0")
	}
	//using loop we recieve all numbers within range of n and multiply with each other for factoial
	else {
		for(i=1; i<=n; i++){
			fact = fact*i;
		}
	printf("factorial of %lf is : %lf", n , fact);
	}
return 0;
}