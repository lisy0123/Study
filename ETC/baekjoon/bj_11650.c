#include <stdio.h>

int	cmp(const int (*a)[], const int (*b)[])
{
	if ((*a)[0] == (*b)[0])
	{
		if ((*a)[1] > (*b)[1])
			return (1);
		else if ((*a)[1] < (*b)[1])
			return (-1);
		else
			return (0);
	}
	else
	{
		if ((*a)[0] > (*b)[0])
			return (1);
		else if ((*a)[0] < (*b)[0])
			return (-1);
		else
			return (0);
	}
}

int	main ()
{
	int n;
	int i;

	scanf("%d", &n);

	int x[n-1][2];
	
	for (i = 0; i < n; i++)
		scanf("%d %d", &x[i][0], &x[i][1]);
	qsort(x, n, 8, cmp);
	for (i = 0; i < n; i++)
		printf("%d %d\n", x[i][0], x[i][1]);

	return (0);
}
