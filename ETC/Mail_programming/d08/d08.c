#include <stdio.h>

void	target(int a, int *n)
{
	int i;
	int j;
	int tmp;

	for (i = 0; i <= a; i++)
	{
		for (j = 0; j <= a; j++)
		{
			if (n[i] > n[j])
			{
				tmp = n[i];
				n[i] = n[j];
				n[j] = tmp;
			}
		}
	}
	tmp = 0;
	for (i = 0; i < a; i++)
	{
		if (n[i] == n[i+1])
			tmp++;
	}
	if (tmp == a)
		printf("Does not exist.");
	else
		printf("%d",n[1 + tmp]);
	return;
}

void	res(char *c)
{
	int a;
	int i;
	int s;
	int res;
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
			s = -1;
		else if (*c == '+')
			s = 1;
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
	n[i] = (s == -1) ? (res *= s) : res;
	if (--a != i)
	{
		printf("Input Array Nums Error");
		return;
	}
	target(a, n);
}

int	main ()
{
	char *c;

	printf("		ex) 1,2,3... << Write without space\n");
	printf("Input: ");
	scanf("%s", c);
	printf("Output: ");
	res(c);

	return (0);
}
