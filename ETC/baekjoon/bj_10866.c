#include <stdio.h>
#include <string.h>

int arr[5000];
int start = 2000;
int end = 2001;

void push_front(int x)
{
	arr[start--] = x;
}

void push_back(int x)
{
	arr[end++] = x;
}

int pop_front()
{
	if (arr[start + 1] == 0)
        return (-1);
	else
    {
		int r = arr[start + 1];
		arr[++start] = 0; 
		return (r);
	}
}

int pop_back()
{
	if (arr[end - 1] == 0)
        return (-1);
	else
    {
		int r = arr[end - 1];
		arr[--end] = 0;
		return (r);
	}
}

int front()
{
	if (arr[start+1] != 0)
        return (arr[start+1]);
	else
        return (-1);
}

int back()
{
	if (arr[end-1] != 0)
        return (arr[end-1]);
	else
        return (-1);
}

int size()
{
	return (end - start -1);
}

int empty()
{
	if ((end - start - 1) == 0)
        return (1);
	else
        return (0);
}
int main() 
{
	int N;
    int i;

	scanf("%d", &N);

	for (i = 0; i < N; i++)
    {
        int x;
        char str[11];
        
		scanf("%s", &str);

		if (!strcmp(str, "push_front"))
        {
			scanf("%d", &x);
			push_front(x);
		}
		else if (!strcmp(str, "push_back"))
        {
			scanf("%d", &x);
			push_back(x);
		}
		else if (!strcmp(str, "pop_front"))
			printf("%d\n", pop_front());
		else if (!strcmp(str, "pop_back"))
			printf("%d\n", pop_back());
		else if (!strcmp(str, "size"))
			printf("%d\n", size());
		else if (!strcmp(str, "empty"))
			printf("%d\n", empty());
		else if (!strcmp(str, "front"))
			printf("%d\n", front());
        else if (!strcmp(str, "back"))
			printf("%d\n", back());
	}
	return (0);
}