#include <stdio.h>

int	main ()
{
	int num;
	int h;
	int w;
	int n;
	int j;
	int res;

	scanf("%d", &num);
	while (num--)
	{
		scanf("%d %d %d", &h, &w, &n);
		res = 0;
		for (j = 0; j < n; j++)
		{
			if (n % h == 0)
				res = h * 100 + (n / h);
			else
				res = (n % h) * 100 + (n/h + 1);
		}
		if (res <= (h * 100 + w))
			printf("%d\n", res);
	}
	return (0);
}
