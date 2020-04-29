#include <stdio.h>

void	decode(int code)
{
	while (code != 0)
	{
		if ((code % 10) == 1)
			printf(")");
		else if ((code % 10) == 0)
			printf("(");
		code = code / 10;
	}
	if ()
	printf(", ");
}


void	re(int open, int close, int code)
{
	if (code == 0)
	{
		code = 1;
		re(open - 1, close, code);
	}
	else
	{
		if (open != 0)
		{
			if (open < close)
			{
				code *= 10;
				re(open - 1, close, code + 1);
				re(open, close - 1, code);
			}
			else if (open == close)
			{
				code *= 10;
				re(open - 1, close, code + 1);
			}
		}
		else if (close != 0)
		{
			code *= 10;
			re(open, close - 1, code);
		}
		else
			decode(code);
	}
}

void	res(int num)
{
	if (num)
	{
		printf("[");
		re(num, num, 0);
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
