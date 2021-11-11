#include <stdio.h>

long choose(int n, int r)
{
	if (n == r || r == 0)
		return (1);
	return (choose(n - 1, r - 1) + choose(n - 1, r));
}

int	main ()
{
	int i, j;
	long res;

	scanf("%d %d", &i, &j);
	res = choose(i, j);
	printf("%ld", res);
	return (0);
}
