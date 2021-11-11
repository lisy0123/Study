#include <stdio.h>
#include <string.h>

int main ()
{
	int n;
	int c[26] = {};
	char  s[100];

	scanf("%s", s);
	for (int i = 0; i < strlen(s); i++)
	{
		n = s[i] - 97;
		if (c[n] == 0)
			c[n] = i + 1;
	}
	for (int j = 0; j < 26; j++)
	{
		if (c[j] != 0)
			printf("%d ", c[j] - 1);
		else
			printf("-1 ");
	}
	return (0);
}
