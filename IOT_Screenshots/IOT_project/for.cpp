#include<stdio.h>
#include<conio.h>

int main()
{
	int a,sum=0,fact=1;
	
	for(a=1;a<=10;a++)
	{
		printf("%d\n",a);
	}
	
	for(a=1;a<=10;a++)
	{
		printf("2*%d =%d\n",a,2*a);
	}
	for(a=1;a<=5;a++)
	{
		sum=sum+a;
	}
	printf("%d\n",sum);
	
	for(a=1;a<=5;a++)
	{
		fact=fact*a;
	}
	printf("%d",fact);
	getch();
}
