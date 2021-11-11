#include <stdio.h>
#include <string.h>

int	main ()
{
	char s[1000001];
	char p[1000001];
	char *ptr;

	scanf("%s", s);
	scanf("%s", p);
	ptr = strstr(s, p);
	if (ptr != NULL)
		printf("1");
	else
		printf("0");
	return (0);
}
