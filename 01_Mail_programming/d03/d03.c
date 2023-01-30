#include <stdio.h>
#include <math.h>

void	final(int code)
{
	int p;
	int dec;
	int an;
	int n;
	int i;

	code /= 10;
	p = 1;
	dec = 0;
	while (code > 0)
	{
		p *= 2;
		if (code % 10 == 1)
			dec += p;
		code /= 10;
	}
	an = 0;
	n = 0;
	i = 1;
	while (n < dec)
	{
		an = (int)(pow(2, 2 * i - 1));
		n = n + an;
		i++;
	}
	if (n != dec)
		printf("\", \"");
}

void	decode(int code)
{
	int num;

	num = code;
	while (code != 0)
	{
		if ((code % 10) == 1)
			printf(")");
		else if ((code % 10) == 0)
			printf("(");
		code = code / 10;
	}
	final(num);
}


void	check(int open, int close, int code)
{
	if (code == 0)
	{
		code = 1;
		check(open - 1, close, code);
	}
	else
	{
		if (open != 0)
		{
			if (open < close)
			{
				code *= 10;
				check(open - 1, close, code + 1);
				check(open, close - 1, code);
			}
			else if (open == close)
			{
				code *= 10;
				check(open - 1, close, code + 1);
			}
		}
		else if (close != 0)
		{
			code *= 10;
			check(open, close - 1, code);
		}
		else
			decode(code);
	}
}

void	res(int num)
{
	if (num)
	{
		printf("[\"");
		check(num, num, 0);
		printf("\"]");
	}
	else
		printf("No Output");
}

int	main()
{
	int num;
	
	printf("Input: ");
	scanf("%d", &num);
	printf("Output: ");
	res(num);
	
	return (0);
}
