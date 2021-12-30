#include <stdio.h>

int main ()
{
	int n[5];
	int res;

	scanf("%d %d %d %d %d", &n[0], &n[1], &n[2], &n[3], &n[4]);
	res = 0;
	for (int i = 0; i < 5; i++)
		res += (n[i] * n[i]);
	res %= 10;
	printf("%d", res);
	return (0);
}
