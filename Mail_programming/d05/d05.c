#include <stdio.h>

void	res(char *num, int tg)
{
	while (num != 0)
	{

		num++;
	}
}

int	main ()
{
	char num[];
	int tg;

	printf("Input: ");
	scanf("%s", num);
	printf("Target: ");
	scanf("%d", &tg);
	printf("Output: ");
	res(num, tg);
	return (0);
}
