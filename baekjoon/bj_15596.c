#include <stdio.h>

long long sum(int *a, int n)
{
	long long res;
	int i;

	res = 0;
	for (i = 0; i < n; i++)
		res += (long long)a[i];
	return (res)
}
