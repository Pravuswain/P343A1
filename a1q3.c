#include <studio.h>

int main()
{
	//define all variables 
	double i=1 , s=0, diff = 7 , s1 = 0 , s2 = 0, n;
	//ask user for the number
	printf("Enter number of terms:")
	scanf("%lf", &n)

	//use while loop with conditon
	while(diff > 0.001) {
		if(i <= n)
		{
			s2= 1/i;
			s1= s;
			s = s + s2;
			diff= s - s1;
			i++;

		};
		if(i>n)
		{
			s=s+0;
			s1=s;
			diff=0;
		};
	};
	if (diff<0.001){
		printf("Sum is %lf", s1);
	};
	return 0;
}