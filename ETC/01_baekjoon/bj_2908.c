#include <stdio.h>
#include <math.h>

int power(int tmp, int n)
{
	int res;

	res = 0;
	for (int i = 0; i < 3; i++)
	{
		tmp = n % 10;
		res += tmp * (int)(pow(10, 2 - i));
		n /= 10;
	}
	return (res);
}

int main ()
{
	int n1;
	int n2;
	int tmp1;
	int tmp2;

	tmp1 = 0;
	tmp2 = 0;
	scanf("%d %d", &n1, &n2);
	tmp1 = power(tmp1, n1);
	tmp2 = power(tmp2, n2);
	if (tmp1 > tmp2)
		printf("%d", tmp1);
	else
		printf("%d", tmp2);
	return (0);
}
