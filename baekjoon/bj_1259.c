#include <stdio.h>

void	res(int num)
{
	int tmp;
	int res;

	res = num;
	tmp = 0;
	while (num > 0)
	{
		tmp *= 10;
		tmp += num % 10;
		num /= 10;
	}
	if (tmp == res)
		printf("yes\n");
	else
		printf("no\n");
}

int	main ()
{
	int num;

	while (1)
	{
		scanf("%d", &num);
		if (num == 0)
			break;
		res(num);
	}
	return (0);
}
