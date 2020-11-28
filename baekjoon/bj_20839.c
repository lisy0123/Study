#include <stdio.h>

int main()
{
	int n,i,j;
	int res;

	scanf("%d",&n);

	i=n/5;
	n%=5;
	while (i>=0)
	{
		if (!(n%3))
		{
			j=n/3;
			n%=3;
			break;
		}
		i--;
		n+=5;
	}
	if (n==0)
		printf("%d",i+j);
	else
		printf("-1");
	return (0);
}
