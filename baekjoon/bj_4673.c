#include <stdio.h>

int main()
{
    int tmp;
    int num;
    int res[10001];
    int check;

    for (int i = 1; i < 10001; i++)
    {
        tmp = i;
        num = i;
        while (1)
        {
            if (i == 0)
                break;
            num += (i%10);
            i = i / 10;
        }
        i = tmp;
        res[i] = num;
    }
    for (int i = 1; i < 10001; i++)
    {
		check = 0;
		for (int j = 1; j < 10001; j++)
		{
			if (i == res[j])
				check = 1;
		}
        if (!check)
            printf("%d\n", i);
    }
    return (0);
}

