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
		printf("True");
	else
		printf("False");
}

int	main ()
{
	int num;

	printf("Intput: ");
	scanf("%d", &num);
	printf("Output: ");
	if (num < 0)
		printf("False");
	else if (num == 0)
		printf("True");
	else
		res(num);
	return (0);
}
