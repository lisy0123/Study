#include <stdio.h>

void	error(int i)
{
	if (i == 1)
		printf("Type error!");
}

int	sum_fb(int *n, int x)
{
	int i;
	int res;
	int count;

	res = n[0];
	count = 0;
	for (i = 0; i < x; i++)
	{
		if (res > n[i])
		{
			count = i;
			res = n[i];
		}
	}
	printf("%d\n\n", count);
	return (count);
}

void	solved(int *n_f, int *n_b, int x)
{
	int start;
	int end;
	int i;
	int j;
	int k;
	int a;
	int count;

	count = x;
	i = sum_fb(n_f, x);
	start = n_f[i];
	end = n_b[sum_fb(n_b, x)];
	printf("{");
	while (count > 0)
	{
		a = 1;
		for (j = 0; j < x; j++)
		{
			printf("::%d %d %d %d\n", n_f[j], n_b[j], start, end);
			if (n_f[j] <= end && n_b[j] > end)
			{
				end = n_b[j];
				n_b[j] = 0;
			}
			else if (n_b[j] <= end)
			{
				n_b[j] = 0;
				count--;
			}
			if (n_f[j] > start)
			{
				if (n_f[j] <= end)
					n_f[j] = 999;
				if (n_b[j] >= end && n_f[j] == 999)
				{
					end = n_b[j];
					n_b[j] = 0;
				}
			}
			else if (n_f[j] == 999)
			{
				count--;
				a++;
			}
			printf("!!! %d %d %d \n", a, x, count);
			if (a == x)
			{
				start = n_f[j];
				end = n_b[j];
			}
		}
		printf("{%d,%d},", start, end);
		n_f[i] = 999;
		i = sum_fb(n_f, x);
		start = n_f[i];
		end = n_b[sum_fb(n_b, x)];
		count--;
	}
}

void	res(char *s)
{
	int i;
	char *tmp;

	tmp = s;
	i = 0;
	for (; *tmp; tmp++)
		i++;
	i /= 5;

	int n_f[i];
	int n_b[i];
	int sw;
	int x;
	int y;
	int res;
	int count;

	res = 0;
	sw = 0;
	x = 0;
	y = 0;
	count = 0;
	for (; *s; s++)
	{
		if (*s == '{')
			sw = 1;
		else if (*s == '}')
			continue;
		else if (*s >= '0' && *s <= '9')
		{
			res *= 10;
			res += (*s - '0');
		}
		else if (*s == ',')
		{
			tmp = s;
			tmp++;
			if (sw == 1)
			{
				n_f[x] = res;
				x++;
				sw = -1;
			}
			else if (sw == -1)
			{
				n_b[y] = res;
				y++;
			}
			else if (*tmp == '}')
				s++;
			else
			{
				error(1);
				return;
			}
			res = 0;
		}
		else
		{
			error(1);
			return;
		}
	}
	n_b[y] = res;
	solved(n_f, n_b, x);
}

int	main ()
{
	char *s;

	printf("       ex) {1,2},{3,4},{5,6},... << Write without space\n");
	printf("Input: ");
	scanf("%s", s);

	printf("Output: ");
	res(s);
	printf("");
	return (0);
}
