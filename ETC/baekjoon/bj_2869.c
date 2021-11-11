#include <stdio.h>

int	main ()
{
	int a;
	int b;
	int v;
	int count;

	scanf("%d %d %d", &a, &b, &v);
	count = (v - b - 1) / (a - b) + 1;
	printf("%d", count);
	return (0);
}
