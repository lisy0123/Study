#include <stdio.h>

int main ()
{
	int n;
	double max;
	double s[1001] = {};
	double res;

	scanf("%d\n", &n);

	max = 0;
	res = 0;
	for (int i = 0; i < n; i++)
	{
		scanf("%lf", &s[i]);
		if (s[i] > max)
			max = s[i];
	}
	for (int j = 0; j < n; j++)
	{
		s[j] = s[j]/max*100;
		res += s[j];
	}
	printf("%lf", res/n);
	return (0);
}
