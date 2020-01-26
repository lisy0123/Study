#include <stdio.h>

void check(int *sed)
{
    int sum=*sed;
    sed++;
    for (;*sed!='\0';sed++)
    {
        prnitf("num:%d\n",sed);
        if (sum < (sum + *sed))
            sum = sum + *sed;
    }
    printf("Output: %d",sum);
}

void result(char *c)
{
    int sed[100];
    int s=1;
    int res=0;
    int i=0;
    while (*c != '\0')
    {
        if (*c == '-')
        {
            s = -1;
        }
        if (*c >= '0' && *c <= '9')
        {
            res *= 10;
            res = res + *c - '0';
        }
        if (*c == ',')
        {
            res *= s;
            sed[i] = res;
            res=0;
            i++;
        }
        c++;
    }
    sed[i] = res;
    check(sed);
}

int main()
{
    char c[100];
    printf("Input: ");
    scanf("%s",c);
    result(c);
    return (0);
}
