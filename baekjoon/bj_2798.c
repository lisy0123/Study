#include <stdio.h>

int	main ()
{
	int n;
	int m;
	scanf("%d %d", &n, &m);

	int s[n];
	int i;
	int j;
	int k;
	int max;
	for (i = 0; i < n; i++)
		scanf("%d", &s[i]);

	max = 0;
	for (i = 0; i < n; i++)
	{
		for (j = i + 1; j < n; j++)
		{
			for (k = j + 1; k < n; k++)
			{

				if (s[i] + s[j] + s[k] <= m)
				{
					if (max < s[j] + s[k] + s[i])
						max = s[j] + s[k] +s[i];
				}
			}
		}
	}
	printf("%d", max);
	return (0);
}
