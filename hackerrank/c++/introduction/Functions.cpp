#include <iostream>

using namespace std;

int max_of_four(int a, int b, int c, int d)
{
    return max(a, max(b, max(c,d)));
}

int main()
{
    int a;
    int b;
    int c;
    int d;

    cin >> a;
    cin >> b;
    cin >> c;
    cin >> d;

    cout << max_of_four(a,b,c,d) << endl;
    return 0;
}
