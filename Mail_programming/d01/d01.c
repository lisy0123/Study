#include <stdio.h>

void check(int *sed, int a)
{
    int sum = sed[0];
    int res = sed[0];

    for (int i = 1; i<=a; i++)
    {
        if (sed[i] < sum + sed[i])
            sum +=sed[i];
        else
            sum = sed[i];
        if (res < sum)
            res = sum;
    }
    printf("Output: %d", res);
}

int num(int res, int s)
{
    if (s == -1)
        return (res *= -1);
    else
        return (res);
}

void result(char *c, int a)
{
    a -= 1;
    int sed[a];
    int s = 0;
    int res = 0;
    int i = 0;

    for (;*c; c++)
    {
        if (*c == '-')
        {
            if (s != -1)
                s = -1;
            else
                s = 1;
        }
        else if (*c == '+')
        {
            if (s == -1)
                s = -1;
            else 
                s = 1;
        }
        else if (*c >= '0' && *c <= '9')
        {
            res *= 10;
            res = res + *c - '0';
        }
        else if (*c == ',')
        {
            sed[i] = num(res, s);
            res = 0;
            s = 1;
            i++;
        }
        else
        {
            printf("Type Error");
            return;
        }
    }
    sed[i] = num(res, s);
    if (a != i)
    {
        printf("Input Array Nums Error");
        return;
    }
    check(sed, a);
}

int main()
{
    int a;
    int k;

    printf("Input Array Nums: ");
    scanf("%d", &a);
    k = a * 2 - 2;
    char c[k];
	printf("       ex) 1,2,3... << Write without space\n");
    printf("Input: ");
    scanf("%s", c);
    result(c, a);
    return (0);
}
