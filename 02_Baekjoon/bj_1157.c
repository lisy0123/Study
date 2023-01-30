#include <stdio.h>

int main ()
{
	int i;
	int n;
	int res;
	int count;
	int c[26] = {};
	char s[1000001];

	scanf("%s",s);

	i = 0;
	while (s[i] != 0)
	{
		if (s[i] >= 'a')
			c[(s[i] - 'a')]++;
		else
			c[(s[i] - 'A')]++;
		i++;
	}
	res = 0;
	count = 0;
	for (int j = 0; j < 26; j++)
	{
		if (c[j] == res)
			count++;
		if (c[j] > res)
		{
			res = c[j];
			n = j;
			count = 0;
		}
	}
	if (count == 0)
		printf("%c", n + 'A');
	else
		printf("?");
	return (0);
}
