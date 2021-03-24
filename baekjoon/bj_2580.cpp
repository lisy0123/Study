#include <stdio.h>

using namespace std;

int arr[10][10] = {0,};
int zeroArr[100][2] = {0,};
int cnt = 0;
bool isSolve = false;

bool isPromising(int row, int col, int num)
{
	for(int i=0;i<9;i++)
    {
		if(arr[row][i]==num)
            return false;
	}
	for(int i=0;i<9;i++)
    {
		if(arr[i][col]==num)
            return false;
	}
	for(int i=(row/3)*3;i<(row/3)*3+3;i++)
    {
		for(int j=(col/3)*3;j<(col/3)*3+3;j++)
        {
			if(arr[i][j]==num)
                return false;
		}
	}
	return true;
}

void printData()
{
	for(int i=0;i<9;i++)
    {
		for(int j=0;j<9;j++)
			printf("%d ", arr[i][j]);
		printf("\n");
	}
}

void backtracking(int index)
{
	for(int j=1;j<=9;j++)
    {
		if(isPromising(zeroArr[index][0], zeroArr[index][1], j))
        {
			arr[zeroArr[index][0]][zeroArr[index][1]]=j;
			if(index+1==cnt)
            {
				printData();
				isSolve = true;
				return;
			}
			backtracking(index+1);
			arr[zeroArr[index][0]][zeroArr[index][1]]=0;
		}
	}
	
}


int main()
{
	for(int i=0;i<9;i++)
    {
		for(int j=0;j<9;j++)
        {
			scanf("%d", &arr[i][j]);
			if(arr[i][j]==0)
            {
				zeroArr[cnt][0] = i;
				zeroArr[cnt][1] = j;
				cnt++;
			}
		}
	}
	
	backtracking(0);
	if(!isSolve)
        printf("Error");
	
	return 0;
}