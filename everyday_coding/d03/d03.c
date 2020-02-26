#include <stdio.h>

void	re(int num, int i, int j)
{
	int len;

	len = num * 2;
	if (j == len)
		return ;
	if (i < num)
	{
		printf("(");
		re(num, i + 1, j);
	}
	if (j < i)
	{
		printf(")");
		re(num, i, j + 1);
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
