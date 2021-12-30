#include <stdio.h>

int main ()
{
	int n;
	int i;
	int j;

	scanf("%d", &n);

	int nums;
	int tmp;
	int check;
	float res[n];
	
	for (i = 0; i < n; i++)
	{
		scanf("%d ", &nums);
		tmp = 0;
		int score[nums];
		for (j = 0; j < nums; j++)
		{
			scanf("%d", &score[j]);
			tmp += score[j];
		}
		tmp = tmp / nums;
		check = 0;
		for (j = 0; j < nums; j++)
		{
			if (tmp < score[j])
				check += 1;
		}
		res[i] = (float)check / nums * 100;
	}
	for (i = 0; i < n; i++)
		printf("%.3f%%\n", res[i]);
	return (0);
}
