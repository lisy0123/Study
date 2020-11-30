#include <stdio.h>

int main ()
{
	int x;
	int y;
	int w;
	int h;
	int res;

	scanf("%d %d %d %d", &x, &y, &w, &h);
	w -= x;
	h -= y;
	res = x;
	if (res > y)
		res = y;
	if (res > w)
		res = w;
	if (res > h)
		res = h;
	printf("%d", res);
	return (0);
}
