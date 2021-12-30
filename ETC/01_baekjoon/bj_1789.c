#include <stdio.h>

int main ()
{
	long long int s;
	int n;
	int res;
	long long int sum;

	scanf("%lld", &s);
	res = 0;
	sum = 0;
	n = 1;
	while (1)
	{
		sum += n;
		res++;
		if (sum > s)
		{
			res--;
			break;
		}
		n++;
	}
	printf("%d", res);
	return (0);
}
