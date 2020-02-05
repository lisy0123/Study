#include <stdio.h>

void res(int num, int i)
{
    for (; num > i; i++)
    {
    if (i == 0)
        printf("\"");
    if (i == num)
        printf("\"");
}

int main()
{
    int a;
    int i = 0;

    printf("Input: ");
    scanf("%d", &a);
    printf("Output: [");
    res(a, i);
    printf("]");

    return (0);
}
