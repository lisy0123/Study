#include <stdio.h>

void re(int num)
{
	int i;

	if (num > 0)
	{
		i = num;
		while (i > 0)
		{
			printf("(");
			i--;
		}
		num--;
		re(num);
	}
}

void res(int num, int i)
{
	i = 0;
	if (num)
	{
		printf("[");
		re(num);
		printf("]");
	}
	else
		printf("No Output");
}

int main()
{
    int a;
    int i;

    printf("Input: ");
    scanf("%d", &a);
    printf("Output: ");
	i = a;
    res(a, i);

    return (0);
}
