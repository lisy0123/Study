#include <stdio.h>

void	target(int a, int *num, int tg)
{
	int i;
	int j;

	for (i = 0; i <= a; i++)
	{
		j = i;
		for (; j <= a; j++)
		{
			printf("%d %d %d\n", num[i], num[j], num[i]+num[j]);
			if ((num[i] + num[j]) == tg)
			{
				printf("[%d %d]", i, j);
				return;
			}
		}
	}
	printf("No Answer!");
}

void	res(char *c, int tg)
{
	int a;
	int num;
	int res;
	int s;
	int i;
	char *tmp;

	a = 1;
	tmp = c;
	for (; *c; c++)
	{
		if (*c == ',')
			a++;
	}

	int n[a];

	s = 0;
	i = 0;
	res = 0;
	c = tmp;
	for (; *c; c++)
	{
		if (*c == '-')
		{
			if (s != -1)
				s = -1;
			else
				s = 1;
		}
		else if (*c == '+')
		{
			if (s == -1)
				s = -1;
			else
				s = 1;
		}
		else if (*c >= '0' && *c <= '9')
		{
			res *= 10;
			res += (*c - '0');
		}
		else if (*c == ',')
		{
			n[i] = (s == -1) ? (res *= -1) : res;
			res = 0;
			s = 0;
			i++;
		}
		else
		{
			printf("Type Error");
			return;
		}
	}
	n[i] = (s == -1) ? (res *= -1) : res;
	if (--a != i)
	{
		printf("Input Array Nums Error");
		return;
	}
	target(a, n, tg);
}

int	main ()
{
	int tg;

	char *c;
	printf("       ex) 1,2,3... << Write without space\n");
	printf("Input: ");
	scanf("%s", c);
	printf("Target: ");
	scanf("%d", &tg);

	printf("Output: ");
	res(c, tg);
	return (0);
}
