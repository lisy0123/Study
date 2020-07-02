#include <stdio.h>
#include <stdlib.h>

int main()
{
	char *c;
	int k;

	printf("Input:");
	c = malloc(sizeof(char)*100);
	scanf("%s",c);
	k = 0;
	while (c[k] != '\0')
		k++;
	for (; k >= 0; k--)
		printf("%c",c[k]);
	free(c);
	return (0);
}
