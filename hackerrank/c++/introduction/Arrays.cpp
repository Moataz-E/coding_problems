#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;

    int numbers[n];
    for (int i = 0; i < n; i++)
    {
        cin >> numbers[i];
    }

    for (int i = (n-1); i >= 0; i--)
    {
        cout << numbers[i] << ' ';
    }

    cout << endl;
    return 0;
}
