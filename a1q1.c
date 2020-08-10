#include <studio.h>

int main() {
//define all variables to be used
	int n , i , sum = 0;
	//askuser for the info
	printf("Emter a number");
	//use conditions to trap the negative integer 
	if( n < 0 ){
		printf("please enter a posituve integer");

	}
	else {
		//use loop to continue the series till n and add  using sum function
		for ( i = 1; i <= n; ++i)
		{
			sum += i;
		}
	printf("Sum =%d ", sum);
	}
	return 0;
}