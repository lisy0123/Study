#include <stdio.h>
#include <string.h>

int main ()
{
	int n;
	int r;
	char s[21];
	scanf("%d",&n);

	for (int i = 0; i < n; i++)
	{
		scanf("%d %s", &r, s);
		for (int l = 0; l < strlen(s); l++)
		{
			for (int j = 0; j < r; j++)
				printf("%c", s[l]);	
		}
		printf("\n");
	}
	return (0);
}
