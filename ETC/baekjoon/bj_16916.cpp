#include <iostream>
#include <string.h>
 
using namespace std;
 
int main(int argc, const char * argv[]) 
{
	ios_base::sync_with_stdio(false);
    cin.tie(0);
    string s, p;
    cin >> s >> p;
    char* ptr = strstr((char*)s.c_str(), (char*)p.c_str());
    if (ptr != NULL)
        cout << 1 << "\n";
	else
        cout << 0 << "\n";
    return 0;
}

