#include <stdio.h>
#include <stdlib.h>

int main()
{
	char *c;
	int len;

	printf("Input: ");
	c = malloc(sizeof(char) * 100);
	scanf("%[^\n]", c);
	
	len = 0;
	while (c[len])
		len++;
	printf("Output: ");
	for (; len >= 0; len--)
		printf("%c",c[len]);
	free(c);
	return (0);
}
