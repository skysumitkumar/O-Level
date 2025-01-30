#include<stdio.h>
#include<conio.h>
int main()
{
int entre first number,entre second number;
printf("entre first number");
scanf("%d",&first number);

printf ("entre second number");
scanf("%d",&first number);
int a=4;
switch(a)
{
	case 1:
		printf("%d",first number+second number);
		break;
	case 2:
		printf("%d",first number-second number);
		break;
	case 3:
		printf("%d",first number*second number);
		break;
	default:
		printf("%d",first number/second number);
		
}

getch();

}
