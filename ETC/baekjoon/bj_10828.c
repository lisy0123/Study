#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 
int st[10000];
int count = 0;
 
void push(int x)
{
    st[count] = x;
    count++;
}

void pop()
{
    if (count != 0)
        printf("%d\n", st[--count]);
    else
        printf("-1\n");
}

void size()
{
    printf("%d\n", count);
}

void empty()
{
    if (count == 0)
        printf("1\n");
    else
        printf("0\n");
}

void top()
{
    if (count != 0)
        printf("%d\n", st[count - 1]);
    else
        printf("-1\n");
}

int main()
{
    int n;
    int i;
    
    scanf("%d", &n);
    
    for (i = 0; i < n; i++)
    {
        char c[6];
        int x;

        scanf("%s", &c);
        if (!strcmp(c, "push"))
        {
            scanf("%d", &x);
            push(x);
        }
        else if (!strcmp(c, "pop"))
            pop();
        else if (!strcmp(c, "size"))
            size();
        else if (!strcmp(c, "empty"))
            empty();
        else if (!strcmp(c, "top"))
            top();
    }
    return 0;
}