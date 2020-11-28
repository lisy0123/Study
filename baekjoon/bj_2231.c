#include <stdio.h>

int main ()
{
	int n;
	int num;
	int tmp;
	int res;

	scanf("%d", &n);
	num = 0;
	while (num < n)
	{
		res = num;
		tmp = num;	
		while (tmp != 0)
		{
			res += (tmp % 10);
			tmp /= 10;
		}
		if (res == n)
		{
			printf("%d", num);
			return (0);
		}
		num++;
	}
	printf("0");
	return (0);
}
