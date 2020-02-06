#include <stdio.h>

void res(int num, int i)
{
    if (num > 0)
    {
        if (num == i)
            printf("\"");
        for (int i = 0; i < num; i++)
            printf("(");
        for (int i = 0; i < num; i++)
            printf(")");
        printf("%d ", num);
        if (num == 1)
            printf("\"");
        res(num - 1, i);
    }
}

int main()
{
    int a;
    int i;

    printf("Input: ");
    scanf("%d", &a);
    printf("Output: [");
    i = a;
    res(a, i);
    printf("]");

    return (0);
}
