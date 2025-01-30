#include<stdio.h>
#include<conio.h>
int as(int p,int q);
int as(int p,int q)
{
	int c;
	c=p+q;
	return c;
}
int main()
{
	int a=5,b=6,c;
	c=as(a,b);
	printf("%d",c);
	
	getch();
}
