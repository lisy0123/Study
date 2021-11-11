#include <iostream>

using namespace std;

long long S;

int maxN(void)
{
	int num = 1;
	int result = 0;
	long long sum = 0;

	while (1)
	{
		sum += num;
		result++;
		if (sum > S)
		{
			result--; 
			break;
		}
		num++;
	}
	return result;
}

int main(void)
{
	cin >> S;
	cout << maxN() << endl;
	return 0;
}
