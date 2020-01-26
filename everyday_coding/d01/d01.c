#include <stdio.h>

int main(int ac, char **av)
{
    if (ac != 2)
        return (0);
    for (int i=1; i<=av[1][0];i++)
        printf("%d",i);
    return (0);
}
