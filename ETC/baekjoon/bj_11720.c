#include <stdio.h>

int main()
{
	int n;
	int res;
	char s[1001];

	scanf("%d", &n);
	res = 0;
	scanf("%s", s);
	for (int i = 0; i < n; i++)
		res += (s[i] - 48);
	printf("%d", res);
	return (0);
}
