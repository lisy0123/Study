#include <stdio.h>
#include <string.h>

int main ()
{
	int n;
	int len;
	int sc;
	int score;
	char s[81];

	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%s", s);
		score = 0;
		sc = 0;
		for (int j = 0; j < strlen(s); j++)
		{
			if (s[j] == 'O')
			{
				sc++;
				score += sc;
			}
			else
				sc = 0;

		}
		printf("%d\n", score);
	}
	return (0);
}
