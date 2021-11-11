#include <stdio.h>

void	solved(int *n_f, int *n_b, int x)
{
	int i;
	int j;
	int count;

	count = 0;
	i = 0;
	while (i < (x - count))
	{
		if ((i + 1) < (x - count))
		{
			if (n_b[i] >= n_f[i + 1])
			{
				count++;
				if (n_b[i] < n_b[i + 1])
					n_b[i] = n_b[i + 1];
				if (n_f[i] > n_f[i + 1])
					n_f[i] = n_f[i + 1];
				for (j = (i + 1); j < (x - count); j++)
				{
					if ((j + 1) <= (x - count))
					{
						n_f[j] = n_f[j + 1];
						n_b[j] = n_b[j + 1];
					}
				}
				i = 0;
			}
			else
				i++;
		}
		else
			i++;
	}
	printf("{");
	for (i = 0; i < (x - count); i++)
	{
		printf("{%d,%d}", n_f[i], n_b[i]);
		if (i < (x - count - 1))
			printf(", ");
	}
	printf("}");
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

	res = 0;
	sw = 0;
	x = 0;
	y = 0;
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
				printf("Error!");
				return;
			}
			res = 0;
		}
		else
		{
			printf("Error!");
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
	return (0);
}
