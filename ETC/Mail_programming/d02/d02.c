#include <stdio.h>

void res(int a)
{
	int num = 0;
	int nums = 0;
	int s;
	int sum = 0;

	for (;num < a;)
	{
		if (num % 2 == 0)
			sum += num;
		if (num == 0)
			num = 1;
		else
		{
			s = num;
			num += nums;
			nums = s;
		}
	}
	printf("Output: %d",sum);
}

int main()
{
	int N;

	printf("Input: N = ");
	scanf("%d", &N);
	res(N);
	return (0);
}
