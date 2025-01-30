#include<stdio.h>
#include<conio.h>
int main()
{
	int DOB,AGE;
	printf("entre your DOB");
	scanf("%d",&DOB);
	AGE=2022-DOB;
	printf("%d\n",AGE);
	if(AGE>=18)
	{
		printf("eligible for voting");
	}
	else
	{
		printf("not eligible for voting");
	}
	
	getch();
	
}
