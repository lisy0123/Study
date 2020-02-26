#include <stdio.h>

void	re(int num, int open, int close)
{
	int len;

	len = num * 2;
	if (close == len)
		return ;
	if (open != 0 && close == num)
		printf(", ");
	if (open < num)
	{
		printf("(");
		re(num, open + 1, close);
	}
	if (close < open)
	{
		printf(")");
		re(num, open, close + 1);
	}
}

void	res(int num)
{
	if (num)
	{
		printf("[");
		re(num, 0, 0);
		printf("]");
	}
	else
		printf("No Output");
}

int main()
{
	int a;
	
	printf("Input: ");
	scanf("%d", &a);
	printf("Output: ");
	res(a);
	
	return (0);
}
